init -1 python:
    import time, ssl, json, certifi
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
    from urllib.parse import quote

    KEY_STATUS_URL_BASE = "https://verifier.gaming-mods.com/validate_key"

    # Persistent fields
    if not hasattr(persistent, "entered_key"):
        persistent.entered_key = ""
    if not hasattr(persistent, "current_activation"):
        persistent.current_activation = "Free"
    # Server-driven expiry timestamp (epoch seconds)
    if not hasattr(persistent, "expires_at_timestamp"):
        persistent.expires_at_timestamp = None

    # API response buffer
    key_response = {"ok": False, "valid": False, "message": "", "expires_at": None}

    # Internal: defer UI operations until ready to avoid init-time crashes
    ui_ready = False
    pending_notify = None

    def membership_active():
        exp = persistent.expires_at_timestamp
        if exp is None:
            return False
        return (time.time() < float(exp)) and (persistent.current_activation == "YouTubeSubscriber")

    def membership_remaining_seconds():
        exp = persistent.expires_at_timestamp
        if exp is None:
            return 0
        remaining = int(float(exp) - time.time())
        return max(0, remaining)

    def safe_notify(msg):
        """
        Queue notify messages during init; show when UI is ready.
        """
        global pending_notify
        if ui_ready:
            renpy.notify(msg)
        else:
            pending_notify = msg

    def flush_pending_notify():
        """
        Show any queued notify once UI is ready.
        """
        global pending_notify
        if pending_notify:
            renpy.notify(pending_notify)
            pending_notify = None

    def enforce_overlay():
        """
        Only modify overlays; no notify here to avoid init-time UI calls.
        """
        if membership_active():
            if "cheats_overlay" not in config.overlay_screens:
                config.overlay_screens.append("cheats_overlay")
        else:
            if "cheats_overlay" in config.overlay_screens:
                config.overlay_screens.remove("cheats_overlay")

    def inject_cheats_overlay():
        """
        Enforce overlays and notify safely (after UI is ready).
        """
        was_active = "cheats_overlay" in config.overlay_screens
        enforce_overlay()
        now_active = "cheats_overlay" in config.overlay_screens
        if was_active and not now_active:
            safe_notify("⛔ Cheats expired. Re‑verify to unlock again.")

    # ---------- HTTP helpers ----------

    def _build_request_url(key, extra_query=None):
        # Prefer requesting specific fields to get expires_at from backend.
        qs = ""
        if extra_query:
            # extra_query should be like "fields=valid,message,expires_at" or "legacy=1"
            qs = "?" + extra_query
        return KEY_STATUS_URL_BASE + "/" + key + qs

    def _call_backend(url):
        # Use a neutral UA to avoid backend legacy trimming bound to "RenPy-Client".
        ctx = ssl.create_default_context(cafile=certifi.where())
        req = Request(url, headers={
            "User-Agent": "GameClient/1.0",
            "Accept": "application/json"
        })
        resp = urlopen(req, timeout=15, context=ctx)
        data = json.loads(resp.read().decode())
        return data

    # ---------- Startup verification (deferred via start callback) ----------
    #
    # On every game open, if a key is saved, verify it against the backend.
    # If valid, keep cheats unlocked and refresh expires_at; otherwise disable.
    #
    def verify_on_startup():
        global key_response
        entered_key = (persistent.entered_key or "").strip()
        if not entered_key:
            # No key saved → ensure cheats are disabled
            persistent.current_activation = "Free"
            persistent.expires_at_timestamp = None
            inject_cheats_overlay()
            return

        try:
            key = quote(entered_key, safe="")
            # First, try to fetch expires_at explicitly
            url1 = _build_request_url(key, extra_query="fields=valid,message,expires_at")
            data = _call_backend(url1)

            ok = bool(data.get("ok"))
            valid = bool(data.get("valid"))
            msg = data.get("message", "") or ""
            exp = data.get("expires_at")

            # If backend returned without expires_at, try a second call asking full payload
            if exp is None and ok and valid:
                try:
                    url2 = _build_request_url(key, extra_query=None)
                    data2 = _call_backend(url2)
                    exp = data2.get("expires_at", exp)
                except Exception:
                    pass

            key_response = {"ok": ok, "valid": valid, "message": msg, "expires_at": exp}

            if ok and valid:
                persistent.current_activation = "YouTubeSubscriber"
                # Store server expiry if provided; if missing, keep cheats but no countdown
                if exp is not None:
                    try:
                        persistent.expires_at_timestamp = float(exp)
                    except Exception:
                        # Malformed expiry → treat as invalid to avoid locking cheats endlessly
                        persistent.expires_at_timestamp = None
                        persistent.current_activation = "Free"
                inject_cheats_overlay()
            else:
                # Invalid or expired → disable cheats
                persistent.current_activation = "Free"
                persistent.expires_at_timestamp = None
                inject_cheats_overlay()

        except HTTPError as e:
            # Map codes to user-friendly messages; do not notify during init.
            if e.code == 410:
                key_response = {"ok": False, "valid": False, "message": "Key expired. Request a new one.", "expires_at": None}
            elif e.code == 400:
                key_response = {"ok": False, "valid": False, "message": "Invalid or unknown key.", "expires_at": None}
            elif e.code == 404:
                key_response = {"ok": False, "valid": False, "message": "Key not found.", "expires_at": None}
            else:
                key_response = {"ok": False, "valid": False, "message": "HTTP {}".format(e.code), "expires_at": None}
            # Reflect disabled state without notify in init
            persistent.current_activation = "Free"
            persistent.expires_at_timestamp = None
            enforce_overlay()
        except URLError:
            key_response = {"ok": False, "valid": False, "message": "No internet connection.", "expires_at": None}
            enforce_overlay()
        except Exception as e:
            key_response = {"ok": False, "valid": False, "message": "Key check error: {}".format(e), "expires_at": None}
            persistent.current_activation = "Free"
            persistent.expires_at_timestamp = None
            enforce_overlay()

    # Run after init phase, at the start of the first interaction
    def _startup_after_ui():
        global ui_ready
        ui_ready = True
        verify_on_startup()
        flush_pending_notify()

    # Schedule post-init callback (safe alternative to invoke_in_main_thread)
    config.start_callbacks.append(_startup_after_ui)

    # ---------- Manual key validation (from prompt) ----------

    def check_generated_key():
        global key_response
        entered_key = (persistent.entered_key or "").strip()

        if not entered_key:
            renpy.show_screen("subscription_confirmation_screen",
                              message="❌ Please paste your generated key.")
            return

        key_response = {"ok": False, "valid": False, "message": "", "expires_at": None}
        renpy.show_screen("loading_indicator")
        renpy.invoke_in_thread(make_key_request)

    def make_key_request():
        global key_response
        try:
            key = quote((persistent.entered_key or "").strip(), safe="")
            # Ask for expires_at so we can show a countdown to the actual expiry date
            url = _build_request_url(key, extra_query="fields=valid,message,expires_at")
            data = _call_backend(url)

            key_response["ok"] = bool(data.get("ok"))
            key_response["valid"] = bool(data.get("valid"))
            key_response["message"] = data.get("message", "") or ""
            key_response["expires_at"] = data.get("expires_at")

            # Fallback: if expires_at missing, try full response
            if key_response["expires_at"] is None and key_response["ok"] and key_response["valid"]:
                try:
                    url2 = _build_request_url(key, extra_query=None)
                    data2 = _call_backend(url2)
                    key_response["expires_at"] = data2.get("expires_at", None)
                except Exception:
                    pass

        except HTTPError as e:
            if e.code == 410:
                key_response = {"ok": False, "valid": False, "message": "Key expired. Request a new one.", "expires_at": None}
            elif e.code == 400:
                key_response = {"ok": False, "valid": False, "message": "Invalid or unknown key.", "expires_at": None}
            elif e.code == 404:
                key_response = {"ok": False, "valid": False, "message": "Key not found.", "expires_at": None}
            else:
                key_response = {"ok": False, "valid": False, "message": "HTTP {}".format(e.code), "expires_at": None}
        except URLError:
            key_response = {"ok": False, "valid": False, "message": "No internet connection.", "expires_at": None}
        except Exception as e:
            key_response = {"ok": False, "valid": False, "message": "Key check error: {}".format(e), "expires_at": None}

        renpy.invoke_in_main_thread(handle_key_response)

    def handle_key_response():
        renpy.hide_screen("loading_indicator")
        if key_response.get("ok") and key_response.get("valid"):
            # Persist “subscriber” state
            persistent.current_activation = "YouTubeSubscriber"

            # Save server expiry if provided
            exp = key_response.get("expires_at")
            if exp is not None:
                try:
                    persistent.expires_at_timestamp = float(exp)
                except Exception:
                    persistent.expires_at_timestamp = None

            inject_cheats_overlay()

            # Show success with remaining time (days:hours:mins:secs)
            remaining = membership_remaining_seconds()
            days = remaining // 86400
            hours = (remaining % 86400) // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60

            # If expiry is missing, show generic success
            if persistent.expires_at_timestamp is None:
                renpy.show_screen(
                    "subscription_confirmation_screen",
                    message=f"✅ Key accepted. Cheats unlocked!"
                )
            else:
                renpy.show_screen(
                    "subscription_confirmation_screen",
                    message=f"✅ Key accepted. Cheats unlocked for {days}d {hours:02d}:{minutes:02d}:{seconds:02d}!"
                )
        else:
            msg = key_response.get("message") or "❌ Invalid or expired key."
            renpy.show_screen("subscription_confirmation_screen", message=msg)
            # Also reflect state
            persistent.current_activation = "Free"
            persistent.expires_at_timestamp = None
            inject_cheats_overlay()

# ────────────────────────────────────────────
# Screens
# ────────────────────────────────────────────

transform loading_bounce:
    yoffset 0
    ease 0.8 yoffset -10
    ease 0.8 yoffset 0
    repeat

screen loading_indicator():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        vbox:
            spacing 10
            text "Checking key status…" style "gui_text" xalign 0.5
            text "Please wait…" style "gui_text" xalign 0.5 at loading_bounce
            textbutton "Cancel" action Hide("loading_indicator") xalign 0.5

screen subscription_confirmation_screen(message=""):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        vbox:
            spacing 20
            text "[message]" style "gui_text" xalign 0.5
            textbutton "OK" action Hide("subscription_confirmation_screen") xalign 0.5

# ────────────────────────────────────────────
# Prompt
# ────────────────────────────────────────────

label ask_generated_key:
    $ entered_key = renpy.input(
        "Paste your generated key:",
        default=(persistent.entered_key or ""),
        length=120
    )
    $ entered_key = (entered_key or "").strip()
    if entered_key:
        $ persistent.entered_key = entered_key
        $ check_generated_key()
    return

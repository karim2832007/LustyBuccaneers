# Version event: 3
# Version game: 0.26

default clock_rain = False

init -999 python:
    class gameClock(objectRevertable):

        MORNING = "Morning"
        AFTERNOON = "Afternoon"
        EVENING = "Evening"
        NIGHT = "Night"
        
        MONDAY = "Monday"
        TUESDAY = "Tuesday"
        WEDNESDAY = "Wednesday"
        THURSDAY = "Thursday"
        FRIDAY = "Friday"
        SATURDAY = "Saturday"
        SUNDAY = "Sunday"

        MONDAY_SHOT = "Mon"
        TUESDAY_SHOT = "Tue"
        WEDNESDAY_SHOT = "Wed"
        THURSDAY_SHOT = "Thu"
        FRIDAY_SHOT = "Fri"
        SATURDAY_SHOT = "Sat"
        SUNDAY_SHOT = "Sun"

        def __init__(self):
            super().__init__()
            self.day = 1
            self.WEEK_DAYS = (self.MONDAY, self.TUESDAY, self.WEDNESDAY, self.THURSDAY, self.FRIDAY, self.SATURDAY, self.SUNDAY)
            self.TIME_MOMENTS = (self.MORNING, self.AFTERNOON, self.EVENING, self.NIGHT)
            self.time_day = list(self.TIME_MOMENTS)
            self.locked = False


        def next(self, increment=1, force=False):
            if self.locked and not force:
                return
            
            # va recortando la lista lo cual permite que siempre el momento actual sea el 0
            self.time_day = self.time_day[min(increment, len(self.time_day) - 1):]

        def sleep(self, force=False):
            if self.locked and not force:
                return
            
            # dormir vuelve toda la 
            self.time_day = list(self.TIME_MOMENTS)
            self.day += 1
        
        def lock(self):
            self.locked = True

        def unlock(self):
            self.locked = False

        @property
        def getWeekDay(self):
            return self.WEEK_DAYS[(self.day-1)%7]
    
        @property
        def getTime(self):
            return self.time_day[0]

        @property
        def getDay(self):
            return self.day

        @property
        def morning(self):
            return self.getTime == self.MORNING
        @property
        def afternoon(self):
            return self.getTime == self.AFTERNOON
        @property
        def evening(self):
            return self.getTime == self.EVENING
        @property
        def night(self):
            return self.getTime == self.NIGHT


        @property
        def monday(self):
            return self.getWeekDay == self.MONDAY
        @property
        def tuesday(self):
            return self.getWeekDay == self.TUESDAY
        @property
        def wednesday(self):
            return self.getWeekDay == self.WEDNESDAY
        @property
        def thursday(self):
            return self.getWeekDay == self.THURSDAY
        @property
        def friday(self):
            return self.getWeekDay == self.FRIDAY
        @property
        def saturday(self):
            return self.getWeekDay == self.SATURDAY
        @property
        def sunday(self):
            return self.getWeekDay == self.SUNDAY


        def nDay(self, nday=0 ):
            return self.day == nday
        def nActiveDay(self, nday=0):
            return self.day >= nday


image a_rain:
    Animation(
        "FX rain 1", 0.08,
        "FX rain 2", 0.08,
        "FX rain 3", 0.08,
        repeat=True
    )

screen s_rain():
    zorder -20
    add "black_30"
    add "a_rain"

init python:
    def show_rain():
        global clock_rain
        clock_rain = True
        renpy.show_screen("s_rain")
        renpy.with_statement(Dissolve(0.8))
        renpy.music.stop("ambient", 2.0)
        renpy.music.play("rain", "ambient", True, fadein=1.0, relative_volume=1.0)

    def hide_rain():
        global clock_rain
        clock_rain = False
        renpy.hide_screen("s_rain")
        renpy.with_statement(Dissolve(0.8))
        renpy.music.stop("ambient", 2.0)

    def get_day():
        time_value = game.clock.getTime
        # Asegurarse de comparar con las versiones inglesas, ya que son los "identificadores"
        if time_value == "Morning":
            return _("Morning")
        elif time_value == "Afternoon":
            return _("Afternoon")
        elif time_value == "Evening":
            return _("Evening")
        elif time_value == "Night":
            return _("Night")
        else:
            return time_value  # fallback por si acaso

        
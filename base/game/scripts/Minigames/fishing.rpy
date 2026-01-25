# Version event: 4
# Version game: 0.20

#Tabla de peses con su mapa y dificultad y sale random

screen s_miniGameFishing(gameFishing = _miniGameFishing):
    add gameFishing

init python:
    class MinigameFishingBar(renpy.Displayable):
        def __init__(self, xpos, ypos, **kwargs):
            super(MinigameFishingBar, self).__init__(**kwargs)
            self.img = renpy.displayable("minigames fishing score_fishing")
            self.imgYellow = renpy.displayable("minigames fishing score_fishing_yellow")
            self.imgRed = renpy.displayable("minigames fishing score_fishing_red")

            self.x = xpos 
            self.y = ypos

            self.progress = 0

        def render(self, width, height, st, at):
            render = renpy.Render(50, 768)

            nCrop = int(((100 - self.progress) * 768) / 100)

            if self.progress >= 70:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.img)
            elif self.progress >= 30:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.imgYellow)
            else:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.imgRed)
    
            render.place(imgCrop, x=self.x, y=self.y + nCrop)

            renpy.redraw(self, .0)
            return render

        def visit(self):
            return [ self.img ]


    class MinigameFishingRect(renpy.Displayable):
        def __init__(self, img, xpos, ymax, type, xsize, ysize, **kwargs):
            super(MinigameFishingRect, self).__init__(**kwargs)
            self.img = renpy.displayable(img)
            self.xsize = xsize 
            self.ysize = ysize
            self.type = type

            self.ymax = ymax
            self.ymin = ymax + 768 - ysize

            self.x = xpos + 64
            self.y = self.ymin

            self.rect = pygame.Rect((self.x, self.y), (self.xsize, self.ysize))

            if self.type == 'fish':
                self.yspeed = 180
            else:
                self.yspeed = 0

            self.force = 0
            #self.update = True
            self.delta_time = 0

        #def set_update(self, update):
        #    self.update = update

        def set_delta(self, delta_time):
            self.delta_time = delta_time

        def render(self, width, height, st, at):
            render = renpy.Render(self.xsize, self.ysize)

            #if not self.update:
            #    render.place(self.img, x=self.x, y=self.y)
            #    renpy.redraw(self, .0)
            #    return render

            if self.type == 'grab':
                if self.force > 0:
                    self.force -= 60 * self.delta_time
                    self.y -= 420 * self.delta_time

                    if self.y < self.ymax: 
                        self.y = self.ymax

                elif self.rect.y < self.ymin: 
                        self.y += 420 * self.delta_time
                
                        if self.y > self.ymin:
                            self.y = self.ymin
            else:
                # FISH MOVEMENT (CHEAT: FREEZE FISH)
                if cheat_mg_fishing_freeze_fish:
                    pass
                else:
                    self.y -= self.yspeed * self.delta_time

                if self.y >= self.ymin: 
                    self.yspeed *= -1
                elif self.y <= self.ymax: 
                    self.yspeed *= -1


            self.rect.y = self.y

            render.place(self.img, x=self.x, y=self.y)
            renpy.redraw(self, .0)
            return render

    class MinigameFishing(renpy.Displayable):
        def __init__(self, **kwargs):
            super(renpy.Displayable, self).__init__(**kwargs)
            #self.rectBack = renpy.displayable(Solid((0,0,0,0)))

            self.xpos = 350
            self.ypos = 156
            self.game = renpy.displayable("minigames fishing bar_fishing")
            self.fish = MinigameFishingRect("minigames fishing fish", xpos=self.xpos, ymax=self.ypos, type='fish', xsize=128, ysize=128)
            self.grab = MinigameFishingRect("minigames fishing grab", xpos=self.xpos, ymax=self.ypos, type='grab', xsize=128, ysize=200)

            self.barFish = MinigameFishingBar(xpos=self.xpos + 206, ypos=self.ypos)

            self.barFish.progress = 30

            #Timer
            #self.update = True
            self.last_time = time.time()
            self.delta_time = 0

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            current_time = time.time()
            self.delta_time = current_time - self.last_time
            self.last_time = current_time

            #if time.time() < self.update_time:
            #    update = False
            #else:
            #    update = True
            #    self.update_time = time.time() + 0.01
            
            # Update
            #self.grab.set_update(update)
            #self.fish.set_update(update)
            self.grab.set_delta(self.delta_time)
            self.fish.set_delta(self.delta_time)
            
            # Render
            render.place(self.game, x=self.xpos, y=self.ypos)

            render.place(self.grab)
            render.place(self.fish)

            render.place(self.barFish)
            
            #if config.developer:
            #    intersection = rectangle_intersect(self.grab, self.fish)
            #    self.overlap = Text("{size=+30}{color=#000}Percentage: %s"%intersection,outlines=[(2, "#fff", 0, 0)]) 
            #    render.place(self.overlap, x=1000, y=200)
            #
            #    self.progressFish_text = Text("{size=+30}{color=#000}ProgressFish: %s"% int(self.barFish.progress),outlines=[(2, "#fff", 0, 0)]) 
            #    render.place(self.progressFish_text, x=1000, y=300)

            #self.run()
            #if update:
            self.run()

            renpy.redraw(self, .0)
            return render

        def run(self):

            # AUTO-WIN CHEAT
            if cheat_mg_fishing_autowin:
                self.barFish.progress = 100
                self.win()
                return

            intersection = rectangle_intersect(self.grab, self.fish)
            
            if intersection > 60:

                # SUPER PROGRESS GAIN CHEAT
                gain = 16
                if cheat_mg_fishing_super_gain:
                    gain *= 5

                self.barFish.progress += gain * self.delta_time

                if self.barFish.progress > 70:
                    if renpy.sound.get_playing(channel="sound") != "fishing_reel_1":
                        renpy.music.stop("sound", 0.0)
                        renpy.sound.play("fishing_reel_1", "sound", True, fadein=0.0, relative_volume=2.0)
                else:
                    if renpy.sound.get_playing(channel="sound") != "fishing_reel_0":
                        renpy.sound.play("fishing_reel_0", "sound", True, fadein=0.0, relative_volume=2.0)

            elif  self.barFish.progress > 0:

                # NO PROGRESS LOSS CHEAT
                if not cheat_mg_fishing_no_loss:
                    self.barFish.progress -= 8 * self.delta_time

                if intersection < 40:
                    renpy.music.stop("sound", 0.0)

            if self.barFish.progress > 100:
                self.barFish.progress = 100
                renpy.music.stop("sound", 0.5)
                self.win()

            elif self.barFish.progress < 0:
                self.barFish.progress = 0
                self.gameOver()

        def gameOver(self):
            renpy.jump(game.location + "_gameover")

        def win(self): 
            renpy.jump(game.location + "_win")

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.grab.force += 10
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.win = pg.display.get_surface()



        self.direction = pg.math.Vector2()
        self.speed = 500

        self.right = True

        self.player_r = [
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f0.png"),
                (64, 64)),
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f1.png"),
                (64, 64)),
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f2.png"),
                (64, 64)),
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f3.png"),
                (64, 64)),
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f4.png"),
                (64, 64)),
            pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f5.png"),
                (64, 64))]

        self.player_run_r = [pg.transform.scale(
            pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f0.png"),
            (64, 64)),
                             pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f1.png"),
                                                (64, 64)),
                             pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f2.png"),
                                                (64, 64)),
                             pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f3.png"),
                                                (64, 64)),
                             pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f4.png"),
                                                (64, 64)),
                             pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f5.png"),
                                                (64, 64)), ]

        self.player_l = [
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f0.png"),
                (64, 64)), True, False),
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f1.png"),
                (64, 64)), True, False),
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f2.png"),
                (64, 64)), True, False),
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f3.png"),
                (64, 64)), True, False),
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f4.png"),
                (64, 64)), True, False),
            pg.transform.flip(pg.transform.scale(
                pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/idle/knight_idle_anim_f5.png"),
                (64, 64)), True, False)]

        self.player_run_l = [pg.transform.flip(pg.transform.scale(
            pg.image.load("res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f0.png"),
            (64, 64)), True, False),
                             pg.transform.flip(pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f1.png"),
                                                                  (64, 64)), True, False),
                             pg.transform.flip(pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f2.png"),
                                                                  (64, 64)), True, False),
                             pg.transform.flip(pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f3.png"),
                                                                  (64, 64)), True, False),
                             pg.transform.flip(pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f4.png"),
                                                                  (64, 64)), True, False),
                             pg.transform.flip(pg.transform.scale(pg.image.load(
                                 "res/v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/run/knight_run_anim_f5.png"),
                                                                  (64, 64)), True, False)]
        self.player_index = 0
        self.anim_speed = 7
        self.image = self.player_r[0]
        self.rect = self.image.get_rect(center=pos)


    def animate(self, dt):
        self.player_index += self.anim_speed * dt

        if self.player_index >= len(self.player_r):
            self.player_index = 0

        if self.right:
            self.image = self.player_r[int(self.player_index)]
        else:
            self.image = self.player_l[int(self.player_index)]

    def update(self, dt):
        self.animate(dt)
        self.input()
        self.move(dt)

    def input(self):
        key = pg.key.get_pressed()


        if key[pg.K_w]:
            self.direction.y = -1
        elif key[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pg.K_a]:
            self.direction.x = -1
            self.right = False
        elif key[pg.K_d]:
            self.direction.x = 1
            self.right = True
        else:
            self.direction.x = 0

    def move(self,dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

        print(self.rect)


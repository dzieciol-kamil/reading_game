from random import randrange

import pygame as pg


class GamePresentation:
    error = ""
    points = "0"
    time = "0.000"
    exit = False
    last_question_ok = True

    def __init__(self):
        pg.init()
        info = pg.display.Info()
        self.screen = pg.display.set_mode((1920, 1024))
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.Font(None, 300)
        self.clock = pg.time.Clock()

    def print_question(self, text):
        print("question={}".format(text))
        self.screen.fill((30, 30, 30))
        self.present_question(text)
        self.present_points()
        self.present_error()
        self.present_time()
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                raise KeyboardInterrupt

    def present_question(self, text):
        color = (randrange(256), randrange(256), randrange(256))
        self.font = pg.font.Font(None, 300)
        txt = self.font.render(text, True, color)
        self.screen.blit(txt, txt.get_rect(center=self.screen_rect.center))

    def present_points(self):
        color = (0, 255, 0) if self.last_question_ok else (255, 0, 0)
        self.font = pg.font.Font(None, 100)
        txt = self.font.render(str(self.points), True, color)
        self.screen.blit(txt, txt.get_rect(topleft=self.screen_rect.topleft))

    def present_error(self):
        color = (255, 0, 0)
        self.font = pg.font.Font(None, 50)
        txt = self.font.render(self.error, True, color)
        self.screen.blit(txt, txt.get_rect(bottom=self.screen_rect.bottom))

    def present_time(self):
        color = (255, 255, 255)
        self.font = pg.font.Font(None, 50)
        txt = self.font.render("średni czas odpowiedzi = " + self.time, True, color)
        self.screen.blit(txt, txt.get_rect(topright=self.screen_rect.topright))

    def shutdown(self):
        pg.quit()

    def print_error(self, error):
        self.error = error

    def update_points(self, points, is_ok):
        self.points = points
        self.last_question_ok = is_ok

    def update_time(self, time):
        self.time = time

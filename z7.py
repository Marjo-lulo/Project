import pygame
import random
import math
import time
pygame.init()

wi, he = 800, 600

win = pygame.display.set_mode((wi, he))
pygame.display.set_caption("Aim Trainer")

ta_i = 400
ta_e = pygame.USEREVENT

ta_p = 30
lives = 3

label_font = pygame.font.SysFont("comicsans", 24)

class target:
    max_t = 30
    gr_r = 0.2
    color = (255, 0, 0)
    color2 = (255, 255, 255)

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.gr = True

    def update(self):
        if self.max_t <= self.size + self.gr_r:
            self.gr = False
        if self.gr:
            self.size += self.gr_r
        else:
            self.size -= self.gr_r

    def draw(self,win):
        pygame.draw.circle(win, self.color,(self.x,self.y), int(self.size))
        pygame.draw.circle(win, self.color2,(self.x,self.y), int(self.size * 0.8))
        pygame.draw.circle(win, self.color,(self.x,self.y), int(self.size * 0.6))
        pygame.draw.circle(win, self.color2,(self.x,self.y), int(self.size * 0.4))

    def collide(self,x,y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size

def draw(win, tar):
    win.fill((0,25,40))

    for ta in tar:
        ta.draw(win)

def format(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top(win, elapsed_time, tar_pres, misses):
    pygame.draw.rect(win, (255,50,25),(0,0,wi,50))
    time_la = label_font.render(f"Time: {format(elapsed_time)}", 1, "black")

    speed = round(tar_pres / elapsed_time, 1)
    speed_la = label_font.render(f"Speed: {speed} t/s", 1, "black")

    hits_la = label_font.render(f"Hits: {tar_pres} ", 1, "black")

    lives_la = label_font.render(f"Lives: {lives - misses} ", 1, "black")

    win.blit(time_la, (5, 5))
    win.blit(speed_la, (230, 5))
    win.blit(hits_la, (450, 5))
    win.blit(lives_la, (650, 5))

def end_screen(win, elapsed_time, tar_pres, click_pr):
    win.fill((0,25,40))
    time_la = label_font.render(f"Time: {format(elapsed_time)}", 1, "white")

    speed = round(tar_pres / elapsed_time, 1)
    speed_la = label_font.render(f"Speed: {speed} t/s", 1, "white")

    hits_la = label_font.render(f"Hits: {tar_pres} ", 1, "white")

    acc = round(tar_pres / click_pr * 100, 1)
    acc_la = label_font.render(f"Accuracy: {acc}%", 1, "white")

    win.blit(time_la, (get_middle(time_la), 200))
    win.blit(speed_la, (get_middle(speed_la), 250))
    win.blit(hits_la, (get_middle(hits_la), 300))
    win.blit(acc_la, (get_middle(acc_la), 350))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                run = False
                break

def get_middle(surface):
    return wi / 2 - surface.get_width() / 2

def main():
    run = True
    tar = []
    clock = pygame.time.Clock()

    tar_pres = 0
    click_pr = 0
    start_time = time.time()
    misses = 0

    pygame.time.set_timer(ta_e, ta_i)

    while run:
        clock.tick(60)
        click = False
        mouse = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == ta_e:
                x = random.randint(ta_p, wi - ta_p)
                y = random.randint(ta_p + 50, he - ta_p)
                targ = target(x,y)
                tar.append(targ)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                click_pr += 1

        for ta in tar:
            ta.update()

            if ta.size <= 0:
                tar.remove(ta)
                misses += 1

            if click and ta.collide(*mouse):
                tar.remove(ta)
                tar_pres += 1

        if misses >= lives:
           end_screen(win, elapsed_time, tar_pres, click_pr)

        draw(win, tar)
        draw_top(win, elapsed_time, click_pr, misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
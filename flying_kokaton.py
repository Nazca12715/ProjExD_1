import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img, True, False)
    koukaton = pg.image.load("fig/3.png")
    koukaton_flip = pg.transform.flip(koukaton, True, False)
    kk_rct = koukaton_flip.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr
        key_lst = pg.key.get_pressed()
        dx, dy = 0, 0
        if key_lst[pg.K_UP]:
            dy -= 1
        if key_lst[pg.K_DOWN]:
            dy += 1
        if key_lst[pg.K_LEFT]:
            dx -= 1
        if key_lst[pg.K_RIGHT]:
            dx += 2
        kk_rct.move_ip(dx, dy)

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img_flip, [-tmr+1600, 0])
        screen.blit(bg_img2, [-tmr+3200, 0])
        screen.blit(koukaton_flip, kk_rct)
        pg.display.update()

        if key_lst[pg.K_RIGHT]:
            tmr -= 1
        else:
            tmr += 1        


        clock.tick(200)

        if tmr > 3199:
            tmr = 0
        if tmr < 0:
            tmr = 3199
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
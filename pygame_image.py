import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_imgs = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    img3 = pg.image.load("ex01-20230926/fig/3.png")
    img3 = pg.transform.flip(img3, True, False)
    img3s = pg.transform.rotozoom(img3, 10, 1.0)
    img3_3s = [img3, img3s]
    bg_img = pg.transform.flip(bg_img, True, False)
    bg_imgs = pg.transform.flip(bg_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        num = 0
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_imgs, [1600-x, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(img3_3s[num], [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
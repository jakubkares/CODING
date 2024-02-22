import pygame,sys

def main():
    pygame.init
    win = pygame.display.set_mode((900,500))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    win.fill(0,255,255)
    pygame.display.flip
    pygame.quit()

if __name__ == '__main__':
    main()            




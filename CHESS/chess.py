import pygame,sys
pygame.init
#screen = pygame.display.set_mode((800,600))
def main():
    pygame.init
    win = pygame.display.set_mode((900,500))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    win.fill(0,0,255)
    pygame.display.flip
    pygame.quit()

if __name__ == '__main__':
    main()        




import pygame
from pygame.time import Clock

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('New game')
    size = width, height = 600, 1000
    screen = pygame.display.set_mode(size)

    fps = 60

    all_sprites = pygame.sprite.Group()

    clock = Clock()
    running = True

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.draw(screen)
        all_sprites.update()

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()

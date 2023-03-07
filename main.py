# Potrzebne importy
import pygame

from pygame.constants import *
from pygame.locals import *

class Planet:

    AU = 149.6e9
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24


    def __init__(self, x , y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self. color = color
        self.mass = mass

        self.isSum = False

    def draw(self):
        x = self.x * Planet.SCALE + SCREEN_WIDTH/2
        y = self.y * Planet.SCALE + SCREEN_HEIGHT/2

        pygame.draw.circle(screen, self.color, (x, y), self.radius)





# Odpalenie modułów pygame
pygame.init()

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 720

# Parametry Screena
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, (255, 255, 0), 1.989e30)

    mercury = Planet(Planet.AU * 0.47, 0, 8, (254, 127, 0), 3.285e23)

    venus = Planet(Planet.AU * 0.723, 0, 10, (128, 128, 128), 4.867e24)

    earth = Planet(Planet.AU, 0, 15, (0, 0, 255), 5.98e24)

    mars = Planet(Planet.AU * 1.524, 0, 12, (255, 0, 0), 6.4171e23)

    jupiter = Planet(Planet.AU * 5.2, 0, 18, (150, 75, 0), 1.898E27)


    # Pętla gry
    running = True
    while running:
        # LOGIKA GRY (w przyszłości):


        # RYSOWANIE GRAFIKI:

        # Wypełnienie okienka kolorem
        screen.fill((0, 0, 0))

        # Rysowanie kształtów w PyGame
        sun.draw()
        mercury.draw()
        venus.draw()
        earth.draw()
        mars.draw()
        jupiter.draw()


        # Czekanie na kolejną klatkę
        clock.tick(60)

        #Aktualizacja gry
        pygame.display.flip()

        # Te cztery linijki pozwalają nam normalnie zamknąć program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

main()
# Potrzebne importy
import math

import pygame

from pygame.constants import *
from pygame.locals import *

class Planet:


    counter = 0
    listOfPlanets = []

    AU = 149.6e9
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24 / 100000

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.isSun = False

        self.velX = self.velY = 0

        if len(Planet.listOfPlanets) > 0:
            sunMass = Planet.listOfPlanets[0].mass
            self.velY = (Planet.G * sunMass / self.x) ** 0.5

        Planet.counter += 1
        Planet.listOfPlanets.append(self)

    def count_gravity_force(self):

        sumForceX = sumForceY = 0

        for planet in Planet.listOfPlanets:
            if planet == self:
                continue

            distance = ((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2) ** 0.5

            force = Planet.G * self.mass * planet.mass / (distance ** 2)

            angle = math.atan2(planet.y - self.y, planet.x - self.x)

            forceX = force * math.cos(angle)
            forceY = force * math.sin(angle)

            sumForceX += forceX * Planet.TIMESTEP
            sumForceY += forceY * Planet.TIMESTEP

        return sumForceX, sumForceY

    def apply_forces(self):
        forceX, forceY = self.count_gravity_force()

        self.velX += forceX / self.mass
        self.velY += forceY / self.mass

        self.x += self.velX * Planet.TIMESTEP
        self.y += self.velY * Planet.TIMESTEP

    def draw(self):
        x = (self.x - offsetX) * Planet.SCALE + SCREEN_WIDTH / 2
        y = (self.y - offsetY) * Planet.SCALE + SCREEN_HEIGHT / 2

        scaledRadius = self.radius * Planet.SCALE

        pygame.draw.rect(screen ,self.color, Rect(x, y - 10, 1, 10))
        pygame.draw.circle(screen, self.color, (x, y), scaledRadius)




    @staticmethod
    def draw_all_planets():
        for planet in Planet.listOfPlanets:
            planet.draw()

    @staticmethod
    def update_all_planets():
        for planet in Planet.listOfPlanets:
            planet.apply_forces()


def lerp(start, stop, interpolation):
    return start + (stop - start) * interpolation


# Odpalenie modułów pygame
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Parametry Screena
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

offsetX = offsetY = 0


def main():
    global offsetY
    global offsetX

    targetScale = 250 / Planet.AU
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 696340, (239, 255, 4), 1.989e30)

    mercury = Planet(0.42 * Planet.AU, 0, 2439.7, (140, 141, 136), 0.330e24)
    venus = Planet(0.72 * Planet.AU, 0, 6051, (255, 128, 0), 4.87e24)
    earth = Planet(1 * Planet.AU, 0, 6371, (0, 0, 255), 5.97e24)
    mars = Planet(1.63 * Planet.AU, 0, 3389, (255, 0, 0), 0.642e24)
    jupiter = Planet(5.2 * Planet.AU, 0, 69911, (255, 255, 255), 1.9e27)
    saturn = Planet(9.5 * Planet.AU, 0, 58232, (216, 132, 48), 5.683E26)
    uranus = Planet(19.2 * Planet.AU, 0, 25362, (51, 204, 255), 8.681E25)
    neptune = Planet(30 * Planet.AU, 0, 24622, (0, 118, 161), 1.024E26)

    # Pętla gry
    running = True
    while running:

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            offsetY -= 10/Planet.SCALE
        if keys[K_s]:
            offsetY += 10/Planet.SCALE
        if keys[K_a]:
            offsetX -= 10/Planet.SCALE
        if keys[K_d]:
            offsetX += 10/Planet.SCALE

        # LOGIKA GRY (w przyszłości):
        Planet.SCALE = lerp(Planet.SCALE, targetScale, 0.01)
        Planet.update_all_planets()


        # RYSOWANIE GRAFIKI:
        # Wypełnienie okienka kolorem
        screen.fill((0, 0, 0))

        # Rysowanie kształtów w PyGame
        Planet.draw_all_planets()


        # Czekanie na kolejną klatkę


        #Aktualizacja gry
        pygame.display.flip()
        clock.tick(60)

        left, middle, right = pygame.mouse.get_pressed()

        moveMouse = pygame.mouse.get_rel()
        if left:
            offsetX = offsetX - moveMouse[0] / Planet.SCALE
            offsetY = offsetY - moveMouse[1] / Planet.SCALE
        if middle:
            offsetX = 0
            offsetY = 0

        # Te cztery linijki pozwalają nam normalnie zamknąć program
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                targetScale *= 1.4 ** event.y
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

main()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import asteroid
import asteroidfield
import sys


from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
        			return
		screen.fill((0, 0, 0))
		updatable.update(dt)
		if keys[pygame.K_SPACE]:
			Player# the open-source pygame library
# throughout this file
import pygame
import asteroid
import asteroidfield
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        asteroid_field = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        running = True
        while running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                screen.fill((0, 0, 0))
                updatable.update(dt)
                if keys[pygame.K_SPACE]:
                        self.shoot()
                for collidable_object in asteroids:
                        if player.collision(collidable_object):
                                print("Game over!")
                                sys.exit()
                for drawable_item in drawable:
                        drawable_item.draw(screen)
                pygame.display.flip()
                dt = clock.tick(60) /1000
if __name__ == "__main__":
        main()


.shoot()
		for collidable_object in asteroids:
			if player.collision(collidable_object):
				print("Game over!")
				sys.exit()
		for drawable_item in drawable:
			drawable_item.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) /1000
if __name__ == "__main__":
	main()


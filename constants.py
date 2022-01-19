# This file is responible for all the constants in the game
import pygame
import os
pygame.init()

# Screen size
WIN_WIDTH = 500
WIN_HEIGHT = 800

# Images
BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
RETURN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "return.png")),(45,45))
PLAY_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "play.png")), (50, 47))
LOGO_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "logo.png")), (350, 150))
# Font
STAT_FONT = pygame.font.SysFont("comicsans", 50)
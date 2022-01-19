import pygame
import os
pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800




BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
RETURN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "return_white.png")),(45,45))
# RETURN_IMG = pygame.transform.threshold(RETURN_IMG, RETURN_IMG,(0,0,0),(255,255,255))
STAT_FONT = pygame.font.SysFont("comicsans", 50)
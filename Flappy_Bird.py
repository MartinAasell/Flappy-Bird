# MAIN file, where all the game logic is
import pygame
from pipe import Pipe
from bird import Bird
from base import Base
from constants import *
pygame.init()

# Start menu
def start_menu(win, bird, base):
    win.blit(BG_IMG, (0,0))
    base.draw(win)
    bird.draw(win)
    win.blit(LOGO_IMG, ((WIN_WIDTH-LOGO_IMG.get_width())//2, 100))
    current_hs = STAT_FONT.render("Current Highscore: " + str(update_score(0)), 1, (255, 255, 255))
    start_text = STAT_FONT.render("Press Space To Play! ", 1, (255, 255, 255))
    win.blit(current_hs, ((WIN_WIDTH-current_hs.get_width())//2, 560))
    win.blit(start_text, ((WIN_WIDTH-start_text.get_width())//2,460))
    # win.blit(PLAY_IMG, ((WIN_WIDTH-PLAY_IMG.get_width())//2, 470))
    pygame.display.update()

def start_game():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    bird = Bird(230,350)
    base = Base(730)
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_game()
        start_menu(win, bird, base)
        base.move()

# Drawing the gamewindow
def draw_win(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, ((WIN_WIDTH-text.get_width())//2, 100))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()

# If player loses
def end_screen(win, bird, pipes, base, score, lose):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game()
        if bird.y + bird.img.get_height() < 730:
            bird.move()
        redraw_win(win, bird, pipes, base, score)
        pygame.display.update()

# Draw window when losing
def redraw_win(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    draw_losing_msg(win)
    draw_scores(win, score)
    pygame.display.update()

# Text when losing
def draw_losing_msg(win):
    lose_text = STAT_FONT.render("GAME OVER!", 1, (255, 255, 255))
    win.blit(lose_text, ((WIN_WIDTH-lose_text.get_width())//2, WIN_HEIGHT//4))
    press = STAT_FONT.render("Press Space To Play Again!", 1, (255,255,255))
    win.blit(press, (((WIN_WIDTH-press.get_width())//2, WIN_HEIGHT//4+press.get_height()*5)))

# Updates the score
def update_score(score):
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])
    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()
        return score
    return last

# Displaying the score
def draw_scores(win, score):
    current_score = STAT_FONT.render("Your Score: " + str(score), 1, (255, 255, 255))
    best_score = STAT_FONT.render("Best Score: " + str(update_score(score)), 1, (255, 255, 255))
    win.blit(current_score,((WIN_WIDTH-current_score.get_width())//2, WIN_HEIGHT//4+current_score.get_height()*2))
    win.blit(best_score, ((WIN_WIDTH-best_score.get_width())//2, WIN_HEIGHT//4+best_score.get_height()*3))


# Game loop
def main_game():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird(230,350)
    base = Base(730)
    pipes = [Pipe(700)]
    score = 0
    lose = False
    run = True
    while run:
        clock.tick(30)
        if lose:
            end_screen(win, bird, pipes, base, score, lose)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not lose:
                        bird.jump()
        if not lose:
            bird.move()
            base.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird): 
                lose = True
            if pipe.x + pipe.pipe_top.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True 
            if not lose: 
                pipe.move()
        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
        for r in rem:
            pipes.remove(r)
        draw_win(win, bird, pipes, base, score)   
        if bird.y + bird.img.get_height() >= 730:
            lose = True
        if bird.y + bird.img.get_height()//2 < 0:
            lose = True

    pygame.quit()
    quit()

# # Replayabilty
# def replay(win):
#     start_game()


def main():
    start_game()

if __name__=="__main__":
    main()
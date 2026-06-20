import pygame
import sys
from color_file import Colors
from game_file import Game

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

game_update_event = pygame.USEREVENT
pygame.time.set_timer(game_update_event, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset_game()
            elif event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()
            elif event.key == pygame.K_DOWN:
                game.move_down()
                game.update_score(0, 1)
            elif event.key == pygame.K_UP:
                game.rotate()
        if event.type == game_update_event and not game.game_over:
            game.move_down()

    screen.fill(Colors.dark_blue)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (375, 180))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw_game(screen)

    pygame.display.update()
    clock.tick(60)





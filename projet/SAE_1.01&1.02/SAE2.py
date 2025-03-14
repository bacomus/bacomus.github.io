import pygame
from SAE1 import *
def bouton():
    pygame.init()

    window_size = (400, 400)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('MasterMind Menu')

    font = pygame.font.Font(None, 24)

    button_surface_Play = pygame.Surface((150, 50))
    button_surface_dificulter = pygame.Surface((150, 50))
    button_surface_Quit = pygame.Surface((150, 50))

    text_play = font.render("Play", True, (0, 0, 0))
    text_dificulter = font.render("Difficulté", True, (0, 0, 0))
    text_quit = font.render("Quitter", True, (0, 0, 0))
    
    text_rect_play = text_play.get_rect(center=(button_surface_Play.get_width()/2, button_surface_Play.get_height()/2))
    text_rect_dificulter = text_dificulter.get_rect(center=(button_surface_dificulter.get_width()/2, button_surface_dificulter.get_height()/2))
    text_rect_quit = text_quit.get_rect(center=(button_surface_Quit.get_width()/2, button_surface_Quit.get_height()/2))

    button_rect_play = pygame.Rect(125, 100, 150, 50)  
    button_rect_dificulter = pygame.Rect(125, 175, 150, 50)
    button_rect_quit = pygame.Rect(125, 250, 150, 50) 
    
    while True:
    
        screen.fill((255, 255, 155))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if button_rect_play.collidepoint(event.pos):
                    print("Play button clicked!")
                    prog()

                if button_rect_dificulter.collidepoint(event.pos):
                    print("Test reussi")
                    difficulte()

                if button_rect_quit.collidepoint(event.pos):
                    print("Quitter button clicked!")
                    pygame.quit()
                    return

        if button_rect_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_Play, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_Play, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_Play, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_Play, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_Play, (0, 100, 0), (1, 48, 148, 10), 2)

        if button_rect_dificulter.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_dificulter, (169, 169, 169), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_dificulter, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_dificulter, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_dificulter, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_dificulter, (100, 0, 0), (1, 48, 148, 10), 2)

        if button_rect_quit.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_Quit, (255, 100, 100), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_Quit, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_Quit, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_Quit, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_Quit, (100, 0, 0), (1, 48, 148, 10), 2)

        button_surface_Play.blit(text_play, text_rect_play)
        button_surface_dificulter.blit(text_dificulter, text_rect_dificulter)
        button_surface_Quit.blit(text_quit, text_rect_quit)

        screen.blit(button_surface_Play, (button_rect_play.x, button_rect_play.y))
        screen.blit(button_surface_dificulter,(button_rect_dificulter.x, button_rect_dificulter.y))
        screen.blit(button_surface_Quit, (button_rect_quit.x, button_rect_quit.y))

        pygame.display.update()

def difficulte():
    pygame.init()
    fen = pygame.display.set_mode((400,400))
    pygame.display.set_caption('dificulter')
    continuer = True
    color = 156, 185, 244
    fen.fill((color))

    font = pygame.font.Font(None, 24)

    button_surface_simple = pygame.Surface((150, 50))
    button_surface_moyen = pygame.Surface((150, 50))
    button_surface_hard = pygame.Surface((150, 50))

    text_simple = font.render("simple", True, (0, 0, 0))
    text_moyen = font.render("moyen", True, (0, 0, 0))
    text_hard = font.render("Hardcore", True, (0, 0, 0))

    text_rect_simple = text_simple.get_rect(center=(button_surface_simple.get_width()/2, button_surface_simple.get_height()/2))
    text_rect_moyen = text_moyen.get_rect(center=(button_surface_moyen.get_width()/2, button_surface_moyen.get_height()/2))
    text_rect_hard = text_hard.get_rect(center=(button_surface_hard.get_width()/2, button_surface_hard.get_height()/2))

    button_rect_simple = pygame.Rect(125, 100, 150, 50)  
    button_rect_moyen = pygame.Rect(125, 175, 150, 50)
    button_rect_hard = pygame.Rect(125, 250, 150, 50) 

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if button_rect_simple.collidepoint(event.pos):
                    print("Dificulté simple")

                if button_rect_moyen.collidepoint(event.pos):
                    print("Dificulté moyenne")

                if button_rect_hard.collidepoint(event.pos):
                    print("Dificulté hard")


        if button_rect_simple.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_simple, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_simple, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_simple, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_simple, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_simple, (0, 100, 0), (1, 48, 148, 10), 2)

        if button_rect_moyen.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_moyen, (255, 170, 0 ), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_moyen, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_moyen, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_moyen, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_moyen, (100, 0, 0), (1, 48, 148, 10), 2)

        if button_rect_hard.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_hard, (255, 100, 100), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_hard, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_hard, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_hard, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_hard, (100, 0, 0), (1, 48, 148, 10), 2)

        button_surface_simple.blit(text_simple, text_rect_simple)
        button_surface_moyen.blit(text_moyen, text_rect_moyen)
        button_surface_hard.blit(text_hard, text_rect_hard)

        fen.blit(button_surface_simple, (button_rect_simple.x, button_rect_simple.y))
        fen.blit(button_surface_moyen,(button_rect_moyen.x, button_rect_moyen.y))
        fen.blit(button_surface_hard, (button_rect_hard.x, button_rect_hard.y))

        pygame.display.update()


                
    pygame.quit()

if(__name__ == '__main__'):
    bouton()
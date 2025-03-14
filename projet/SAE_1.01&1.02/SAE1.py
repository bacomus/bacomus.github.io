from sae import *
import pygame as py
import math
import random

def secret()-> list:
    """
    Fonction qui permet de créer une liste d element selectionner aleatoirement dans la liste
    TabCouleur du fichier sae python. Cette liste constitura notre code secret pour le MasterMind
    :return:list, Code secret du MasterMind
    """
    #initialisation des variables
    
    secret_code : list = []
    
    # boucle permettant d ajouter les differents elements dans notre liste
    # secret_code de maniere aleatoire a partir de la liste TabCouleur du fichier sae
    
    while len(secret_code)<5:
        color : list = TabCouleur[random.randint(0,5)]
        if color not in secret_code:
            print(color)
            secret_code.append(color)
    return secret_code

def verification(prop : list ,secret : list)-> list:
    """
    Pour le jeu du MasterMind, Fonction qui permet de determiner le nombre le oculeur bien positionnee et de couleur mal positionne.
    :param prop:list, liste contenant les couleurs qui constitues notre proposition
    :param secret:list, liste contenant les couleurs du code secret du jeu
    :return: list, count[0] sera le nombre de couleur bien placee et count[1] sera le nombre de couleur mal placee 
    """
    
    # Initialisation des variables
    
    color_verif : list = []
    count : list = [0,0]
    
    # Boucle permettant d incremente count en fonction de si la couleur est la meme que dans dans la proposition et
    # le code secret, si ils ont le même indice ou pas et si la couleur a deja ete teste
    
    for i in range(5):
        if prop[i] not in color_verif:
            color_verif.append(prop[i])
            if prop[i] in secret and prop[i] != secret[i]:
                count[1]+=1
            elif prop[i] == secret[i]:
                count[0]+=1
    return count

def win():
    """
    Fonction qui permet de creer une fenetre pygame
    :return:bool,Boolean permettant de fermer la fenetre parent
    """
    
    # Initialisation des variables
    
    ecran : pygame.Surface = pygame.display.set_mode((534, 360))
    image : pygame.Surface = pygame.image.load("gg.jpg").convert_alpha()
    power : bool = True
    
    # Boucle permettant de faire tourner la fenetre tant qu une certaine action de l utilisateur la ferme
    
    while power :
        ecran.blit(image, (0, 50))
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                power : bool = False
        pygame.display.flip()
    return False
    
def loose():
    """
    Fonction qui permet de creer une fenetre pygame
    :return:bool,Boolean permettant de fermer la fenetre parent
    """
    
    # Initialisation des variables
    
    ecran : pygame.surface = pygame.display.set_mode((1300, 1238))
    image : pygame.surface = pygame.image.load("loose.jpg").convert_alpha()
    power : bool = True
    
    # Boucle permettant de faire tourner la fenetre tant qu une certaine action de l utilisateur la ferme
    
    while power :
        ecran.blit(image, (0, 50))
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                power = False
        pygame.display.flip()
    return False

def prog():
    """
    Fonction qui permet d initialiser les variables necessaire et de lancer successivement les fonctions pour pouvoir jouer au jeu MasterMind
    :return: None
    """
    
    # Initialisation des variables
    
    nb_cout : int = 0
    f : pygame.surface = py.display.set_mode((1920,1080))
    secret_code : list = secret()
    power : bool = True
    turn : int = 1
    
    # parametre de la fenetre et initialisation de pygame
    
    f.fill((255,255,255))
    py.init()

    # Fonction secondaire permettant de jouer au MasterMind
    
    afficherPlateau(f)
    afficherChoixCouleur(f)
    afficherSecret(f,secret_code)
    
    # Boucle permettant de faire tourner le jeu tant que l utilisateur na pas perdu gagne ou qu une action est etait fait pour ferme le jeu
    while power :
        turn +=1
        if turn == 17:
            power=loose()
        my_prop : list = construireProposition(f,turn)
        if verification(my_prop,secret_code)[0]==5:
            afficherSecret(f,secret_code)
            print(turn-1)
            power : bool = win()
            print("FELICITATION")
        else:
            afficherResultat(f,verification(my_prop,secret_code),turn)

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                power = False

    py.quit()
    
if __name__ == "__main__":
    prog()
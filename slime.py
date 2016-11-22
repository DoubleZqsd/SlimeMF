import pygame


H = 0
V = 1

BLANC  = ( 255, 255, 255)
NOIR   = (0, 0, 0)
COUL = ( 255 , 0 , 0 )

FENETRE_LARGEUR = 1280
FENETRE_HAUTEUR = 720

CUL_JOUEUR_H = 10
CUL_JOUEUR_L = 110

BALLE_RAYON = 30
joueur_rayon = 60

pygame.init()

fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)
fenetre = pygame.display.set_mode(fenetre_taille)

fenetre.fill(BLANC)

balle_position = [30, 30]
balle_vitesse  = [5, 5]

sol_position = [0, FENETRE_HAUTEUR - 50]
sol2_position = [0, FENETRE_HAUTEUR - 53]



joueur1_position = [ 150 , FENETRE_HAUTEUR - 53]
joueur2_position = [ FENETRE_LARGEUR - 150 , FENETRE_HAUTEUR - 53]

cul_position = [ joueur1_position[0]-joueur_rayon+5 , sol2_position[1]-10 ]

fini = False
temps = pygame.time.Clock()

#--- Boucle principale
while not fini:
    #--- Traiter entrées joueur
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True

    #--- Logique du jeu
    #balle_position[H] = balle_position[H] + balle_vitesse[H]
    balle_position[V] = balle_position[V] + balle_vitesse[V]

    if balle_position[H] + BALLE_RAYON >= FENETRE_LARGEUR:
        balle_position[H] = FENETRE_LARGEUR - BALLE_RAYON
        balle_vitesse[H] = -balle_vitesse[H]
    else:
        if balle_position[H] < BALLE_RAYON:
            balle_position[H] = BALLE_RAYON
            balle_vitesse[H] = -balle_vitesse[H]

    if balle_position[V] + BALLE_RAYON >= sol2_position[1]:
        balle_position[V] = sol2_position[1] - BALLE_RAYON
        balle_vitesse[V] = -balle_vitesse[V]
    else:
        if balle_position[V] < BALLE_RAYON:
            balle_position[V] = BALLE_RAYON
            balle_vitesse[V] = -balle_vitesse[V]

    #--- Dessiner l'écran
    fenetre.fill(BLANC)
    #--- Dessin joueurs
    pygame.draw.circle(fenetre, NOIR, joueur1_position, joueur_rayon)
    pygame.draw.circle(fenetre, BLANC, joueur1_position, joueur_rayon-10)
    pygame.draw.rect(fenetre, NOIR , (cul_position, (CUL_JOUEUR_L , CUL_JOUEUR_H)))
    
    pygame.draw.circle(fenetre, NOIR, joueur2_position, joueur_rayon)
    
    pygame.draw.circle(fenetre, NOIR, balle_position, BALLE_RAYON)
    pygame.draw.circle(fenetre, BLANC, balle_position, BALLE_RAYON-5)
    #--- Dessin sol
    pygame.draw.rect(fenetre, BLANC, (sol2_position, (1500, 200)))
    pygame.draw.rect(fenetre, NOIR, (sol_position, (1500, 200)))


    #--- Afficher (rafraîchir) l'écran
    pygame.display.flip()

    #--- 50 images par seconde
    temps.tick(100)

pygame.display.quit()
pygame.quit()

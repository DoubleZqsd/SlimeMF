import pygame


H = 0
V = 1

blanc  = ( 255, 255, 255)
noir   = (0, 0, 0)
COUL = ( 255 , 0 , 0 )

fenetre_l = 1280
fenetre_h = 720

cul_joueur_h = 10
cul_joueur_l = 110

balle_rayon = 30
joueur_rayon = 60

pygame.init()

fenetre_taille = (fenetre_l, fenetre_h)
fenetre = pygame.display.set_mode(fenetre_taille)

fenetre.fill(blanc)

balle_position = [640.0, 50.0]
balle_vitesse  = [0.0, 0.0]

sol_position = [0, fenetre_h - 50]
sol2_position = [0, fenetre_h - 53]



joueur1_position = [ 150 , fenetre_h - 53]
joueur2_position = [ fenetre_l - 150 , fenetre_h - 53]

cul_position = [ joueur1_position[0]-joueur_rayon+5 , sol2_position[1]-10 ]

fini = False
temps = pygame.time.Clock()

   
#--- Boucle principale
while not fini:
    #--- Traiter entrees joueur
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True

    #--- Logique du jeu
    #balle_position[H] = balle_position[H] + balle_vitesse[H]
    #balle_position[V] += balle_vitesse[V]
    balle_position[V] += (balle_vitesse[V]*(1/60) + ((9.81 * (1/60*1/60))/2))*100 #*100 car 100px = 1m
    balle_vitesse[V] += 9.81 * (1/60)

    if balle_position[H] + balle_rayon >= fenetre_l:
        balle_position[H] = fenetre_l - balle_rayon
        balle_vitesse[H] = -balle_vitesse[H]
    else:
        if balle_position[H] < balle_rayon:
            balle_position[H] = balle_rayon
            balle_vitesse[H] = -balle_vitesse[H]

    if balle_position[V] + balle_rayon >= sol2_position[1]:
        balle_position[V] = sol2_position[1] - balle_rayon
        balle_vitesse[V] = -balle_vitesse[V]
    else:
        if balle_position[V] < balle_rayon:
            balle_position[V] = balle_rayon
            balle_vitesse[V] = -balle_vitesse[V]
            
    

    #--- Dessiner l ecran
    fenetre.fill(blanc)
    #--- Dessin joueurs
    pygame.draw.circle(fenetre, noir, joueur1_position, joueur_rayon)
    pygame.draw.circle(fenetre, blanc, joueur1_position, joueur_rayon-10)
    pygame.draw.rect(fenetre, noir , (cul_position, (cul_joueur_l , cul_joueur_h)))
    
    pygame.draw.circle(fenetre, noir, joueur2_position, joueur_rayon)
    
    pygame.draw.circle(fenetre, noir, (int(balle_position[H]), int(balle_position[V])), balle_rayon)
    pygame.draw.circle(fenetre, blanc, (int(balle_position[H]), int(balle_position[V])), balle_rayon-5)
    #--- Dessin sol
    pygame.draw.rect(fenetre, blanc, (sol2_position, (1500, 200)))
    pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))


    #--- Afficher (rafraichir) l ecran
    pygame.display.flip()

    #--- 60 images par seconde
    temps.tick(60)

pygame.display.quit()
pygame.quit()

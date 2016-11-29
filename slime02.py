import pygame , math


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

ballepos = [640.0, 50.0]
balle_vitesse  = [1.0, 1.0]

sol_position = [0, fenetre_h - 50]
sol2_position = [0, fenetre_h - 53]

reduc_vitesse=0.8

joueur1pos = [ 150 , fenetre_h - 53]
joueur2pos = [ fenetre_l - 620 , fenetre_h - 53]



cul_position = [ joueur1pos[0]-joueur_rayon+5 , sol2_position[1]-10 ]

fini = False
temps = pygame.time.Clock()

   
#--- Boucle principale
while not fini:
    #--- Traiter entrees joueur
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True

    #--- Logique du jeu
    #ballepos[H] = ballepos[H] + balle_vitesse[H]
    #ballepos[V] += balle_vitesse[V]
    ballepos[V] += (balle_vitesse[V]*(1.0/60.0) + ((9.81 * (1.0/60.0*1.0/60.0))/2.0))*100.0 #*100 car 100px = 1m
    balle_vitesse[V] += 9.81 * (1.0/60.0)
    
    #--- Calculons Pythagore
    #Variables pyt
    x1 = joueur1pos[H]-ballepos[H]
    y1 = joueur1pos[V]-ballepos[V]

    x2 = joueur2pos[H]-ballepos[H]
    y2 = joueur2pos[V]-ballepos[V]
   
    pyt1 = math.sqrt( (x1*x1) + (y1*y1) )
    pyt2 = math.sqrt( (x2*x2) + (y2*y2) )
    
    if pyt1 <= 90.0:
       #get the fuck out
       balle_vitesse[V]=0.0
      
    if pyt2 <= 90.0:
       #get the fuck out
       balle_vitesse[V]= -balle_vitesse[V]*reduc_vitesse
       balle_vitesse[H]= -balle_vitesse[H]*reduc_vitesse
    
    
    
    if ballepos[H] + balle_rayon >= fenetre_l:
        ballepos[H] = fenetre_l - balle_rayon
        balle_vitesse[H] = -balle_vitesse[H]
    else:
        if ballepos[H] < balle_rayon:
            ballepos[H] = balle_rayon
            balle_vitesse[H] = -balle_vitesse[H]

    if ballepos[V] + balle_rayon >= sol2_position[1]:
        ballepos[V] = sol2_position[1] - balle_rayon
        balle_vitesse[V] = -balle_vitesse[V]*reduc_vitesse
        reduc_vitesse-=0.1 
    else:
        if ballepos[V] < balle_rayon:
            ballepos[V] = balle_rayon
            balle_vitesse[V] = -balle_vitesse[V]
    

    #--- Dessiner l ecran
    fenetre.fill(blanc)
    #--- Dessin joueurs
    pygame.draw.circle(fenetre, noir, joueur1pos, joueur_rayon)
    pygame.draw.circle(fenetre, blanc, joueur1pos, joueur_rayon-10)
    pygame.draw.rect(fenetre, noir , (cul_position, (cul_joueur_l , cul_joueur_h)))
    
    pygame.draw.circle(fenetre, noir, joueur2pos, joueur_rayon)
    
    pygame.draw.circle(fenetre, noir, (int(ballepos[H]), int(ballepos[V])), balle_rayon)
    pygame.draw.circle(fenetre, blanc, (int(ballepos[H]), int(ballepos[V])), balle_rayon-5)
    #--- Dessin sol
    
    
    
    
    pygame.draw.rect(fenetre, blanc, (sol2_position, (1500, 200)))
    pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))


    #--- Afficher (rafraichir) l ecran
    pygame.display.flip()

    #--- 60 images par seconde
    temps.tick(60)

pygame.display.quit()
pygame.quit()

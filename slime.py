import pygame , math

#---Horizontal Vertical
H = 0
V = 1

#---Touches du clavier
right2 = pygame.K_d
left2 = pygame.K_q

right = pygame.K_RIGHT
left = pygame.K_LEFT

#---Vitesse du joueur a chaque fois qu'une touche est lue au clavier 
joueur_deplacement = 10 

#---Variables qui serviront a determiner le sens dans laquelle le joueur se deplace.
DROITE = 1
GAUCHE = -1

#---Couleurs
blanc  = ( 255, 255, 255)
noir   = (0, 0, 0)
red = ( 255 , 0 , 0 )

#---Taille fenetre
fenetre_l = 1280
fenetre_h = 720

#---Taille elements
balle_rayon = 30
joueur_rayon = 60
cul_joueur_h = 10
cul_joueur_l = 110

#---Position elements
ballepos = [640.0, 50.0]
balle_vitesse  = [1.0, 1.0]
sol_position = [0, fenetre_h - 50]
sol2_position = [0, fenetre_h - 53]
joueur1pos = [ 150 , fenetre_h - 53]
joueur2pos = [ fenetre_l - 150 , fenetre_h - 53]
cul_position = [ joueur1pos[0]-joueur_rayon+5 , sol2_position[1]-10 ]

#---Variables
reduc_vitesse=8
fini = False

#Quelques definitions rapides qui peuvent etre raccourcies une fois que les deplacements verticaux des joueurs seront pris en compte

def deplace_joueur2(sens):
    joueur2_position[H] += joueur_deplacement * sens

def deplace_joueur1(sens):
    joueur1_position[H] += joueur_deplacement * sens
    cul_position[H] = joueur1_position[0]-joueur_rayon+5

#----------PYGAME INIT--------------
pygame.init()
##############
fenetre_taille = (fenetre_l, fenetre_h)
fenetre = pygame.display.set_mode(fenetre_taille)
fenetre.fill(blanc)
temps = pygame.time.Clock()
pygame.key.set_repeat(200, 25)
##############

#--- Boucle principale
while not fini:
    #--- Traitement entrees joueur
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == right:
                deplace_joueur1(DROITE)
            elif evenement.key == left:
                deplace_joueur1(GAUCHE)
            if evenement.key == right2:
                deplace_joueur2(DROITE)
            elif evenement.key == left2:
                deplace_joueur2(GAUCHE)

    #--- Logique du jeu
    ballepos[V] += (balle_vitesse[V]*(1.0/60.0) + ((9.81 * (1.0/60.0*1.0/60.0))/2.0))*100.0 #*100 car 100px = 1m
    balle_vitesse[V] += 9.81 * (1.0/60.0)

    #---Calculons Pythagore
    #---Variables pyt
    x1 = joueur1pos[H]-ballepos[H]
    y1 = joueur1pos[V]-ballepos[V]

    x2 = joueur2pos[H]-ballepos[H]
    y2 = joueur2pos[V]-ballepos[V]
    
    #---Distance entre balle et joueur1
    pyt1 = math.sqrt( (x1*x1) + (y1*y1) )
    #---Distance entre balle et joueur2
    pyt2 = math.sqrt( (x2*x2) + (y2*y2) )
    #---Collision balle - joueur1    
    if pyt1 <= 90.0:
       #get the fuck out
       balle_vitesse[V]=0.0
    #---Collision balle - joueur2
    if pyt2 <= 90.0:
       #get the fuck out
       balle_vitesse[V]= -balle_vitesse[V]*reduc_vitesse/10
       balle_vitesse[H]= -balle_vitesse[H]*reduc_vitesse/10
    
    
    #---Collision balle - fenetre DROIT
    if ballepos[H] + balle_rayon >= fenetre_l:
        ballepos[H] = fenetre_l - balle_rayon
        balle_vitesse[H] = -balle_vitesse[H]
    #---Collision balle - fenetre GAUCHE
    else:
        if ballepos[H] < balle_rayon:
            ballepos[H] = balle_rayon
            balle_vitesse[H] = -balle_vitesse[H]
    #---Collision balle - fenetre BAS
    if ballepos[V] + balle_rayon >= sol2_position[1]:
        ballepos[V] = sol2_position[1] - balle_rayon
        balle_vitesse[V] = -balle_vitesse[V]*reduc_vitesse/10
        reduc_vitesse-=1
        if reduc_vitesse == -1:
           reduc_vitesse = 0
           
    #---Collision balle - fenetre HAUT
    else:
        if ballepos[V] < balle_rayon:
            ballepos[V] = balle_rayon
            balle_vitesse[V] = -balle_vitesse[V]

    
    #---Dessin a chaque tour (60/sec)
    #---Dessin l ecran
    fenetre.fill(blanc)
    #---Dessin joueur1
    pygame.draw.circle(fenetre, noir, joueur1pos, joueur_rayon)
    pygame.draw.circle(fenetre, blanc, joueur1pos, joueur_rayon-10)
    pygame.draw.rect(fenetre, noir , (cul_position, (cul_joueur_l , cul_joueur_h)))
    #---Dessin joueur2
    pygame.draw.circle(fenetre, noir, joueur2pos, joueur_rayon)
    #---Dessin balle
    pygame.draw.circle(fenetre, noir, (int(ballepos[H]), int(ballepos[V])), balle_rayon)
    pygame.draw.circle(fenetre, blanc, (int(ballepos[H]), int(ballepos[V])), balle_rayon-5)
    #--- Dessin sol    
    pygame.draw.rect(fenetre, blanc, (sol2_position, (1500, 200)))
    pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))

    #--- Afficher (rafraichir) l ecran
    pygame.display.flip()
    
    print reduc_vitesse
    
    #--- 60 images par seconde
    temps.tick(60)

pygame.display.quit()
pygame.quit()

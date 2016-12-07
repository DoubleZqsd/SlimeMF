import pygame , math

#---Horizontal Vertical
H = 0
V = 1

#---Vitesse du joueur a chaque fois qu'une touche est lue au clavier 
joueur_deplacement = 10 


#définition d'un nouvel évènement pour représenter une touche qui reste enfoncée
pygame.KEYPRESSED = pygame.USEREVENT

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
joueur_rayon = 60.0

#---Position elements
ballepos = [640.0, 50.0]
balle_vitesse  = [2.0, 4.0]
sol_position = [0, fenetre_h - 50]
sol2_position = [0, fenetre_h - 53]
joueur1pos = [ 150 , fenetre_h - 53]
joueur2pos = [ fenetre_l - 150 , fenetre_h - 53]
joueur1_vitesse = [5.0 , 0.0]
joueur2_vitesse = [5.0 , 0.0]

#---Variables
reduc_vitesse=8
fini = False
air1 = False
air2 = False
lastballpos = [0.0 , 0.0] 

#Quelques definitions rapides qui peuvent etre raccourcies une fois que les deplacements verticaux des joueurs seront pris en compte

def deplace_h_joueur2(sens):
       joueur2pos[H] += joueur2_vitesse[H]* sens
       if joueur2pos[H] >= fenetre_l - joueur_rayon*2 :
          joueur2pos[H] = fenetre_l - joueur_rayon*2
       elif joueur2pos[H] <= 0:
            joueur2pos[H] = 0 
def deplace_h_joueur1(sens):
       joueur1pos[H] += joueur1_vitesse[H] * sens
       if joueur1pos[H] >= fenetre_l - joueur_rayon*2 :
          joueur1pos[H] = fenetre_l - joueur_rayon*2
       elif joueur1pos[H] <= 0:
            joueur1pos[H] = 0
       
def deplace_v_joueur2(sens):       
               global air2
               if not air2 :
                  joueur2_vitesse[V] -= 10.0 
                  air2 = True
      
def deplace_v_joueur1(sens):       
               global air1
               if not air1 :
                  joueur1_vitesse[V] -= 10.0 
                  air1 = True

#---Touches Clavier

def _nouveauEtatTouche():
    return {
        'actif': False,
        'delai': 0,
        'periode': 0,
        'suivant': 0
    }

def nouvelleGestionClavier():
    return {}

# gc: gestionnaire de clavier (créé par nouvelleGestion Clavier())
# touche: numéro de la touche (ex: pygame.K_e)
# delai: attente (en ms) avant la première répétition
# periode: temps (en ms) entre deux répétitions

def repeteTouche(gc, touche, delai, periode):
    pygame.key.set_repeat()
    
    if touche in gc:
        entree = gc[touche]
    else:
        entree = _nouveauEtatTouche()

    entree['delai'] = delai
    entree['periode'] = periode
    gc[touche] = entree


def scan(gc):
    maintenant = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    for touche in gc:
        if keys[touche] == 1:
            if gc[touche]['actif']:
                if maintenant >= gc[touche]['suivant']:
                    gc[touche]['suivant'] = gc[touche]['periode'] + maintenant
                    pygame.event.post(pygame.event.Event(pygame.KEYPRESSED, {'key':touche}))
            else:
                gc[touche]['actif'] = True
                gc[touche]['suivant'] = gc[touche]['delai'] + maintenant
        else:
            gc[touche]['actif'] = False
            gc[touche]['suivant'] = 0

                  
#----------PYGAME INIT--------------
pygame.init()
##############
fenetre_taille = (fenetre_l, fenetre_h)
fenetre = pygame.display.set_mode(fenetre_taille)
fenetre.fill(blanc)
temps = pygame.time.Clock()
joueur1 = pygame.image.load('joueur1.png').convert_alpha(fenetre)
joueur1 = pygame.transform.scale(joueur1,(120,60))
joueur2 = pygame.image.load('joueur2.png').convert_alpha(fenetre)
joueur2 = pygame.transform.scale(joueur2,(120,60))
##############

gc = nouvelleGestionClavier()
repeteTouche(gc, pygame.K_q, 25, 5)
repeteTouche(gc, pygame.K_z, 25, 5)
repeteTouche(gc, pygame.K_d, 25, 5)
repeteTouche(gc, pygame.K_LEFT, 25, 5)
repeteTouche(gc, pygame.K_RIGHT, 25, 25)
repeteTouche(gc, pygame.K_UP, 25, 25)


#--- Boucle principale
while not fini:
    now = pygame.time.get_ticks()
    #--- Traitement entrees joueur
    scan(gc)
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True
        if evenement.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
               deplace_h_joueur2(DROITE)
            if key[pygame.K_LEFT]:
               deplace_h_joueur2(GAUCHE)
            if key[pygame.K_d]:
               deplace_h_joueur1(DROITE)             
            if key[pygame.K_q] :
               deplace_h_joueur1(GAUCHE)                
            if key[pygame.K_UP]:
               deplace_v_joueur2(DROITE)
            if key[pygame.K_z]:
               deplace_v_joueur1(DROITE)
        if evenement.type == pygame.KEYPRESSED:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
               deplace_h_joueur2(DROITE)
            if key[pygame.K_LEFT]:
               deplace_h_joueur2(GAUCHE)
            if key[pygame.K_d]:
               deplace_h_joueur1(DROITE)             
            if key[pygame.K_q] :
               deplace_h_joueur1(GAUCHE)                
            if key[pygame.K_UP]:
               deplace_v_joueur2(DROITE)
            if key[pygame.K_z]:
               deplace_v_joueur1(DROITE)
    #--- Gravity
    #---Derniere position balle
    lastballpos[H] = ballepos [H]
    lastballpos[V] = ballepos [V]
    #---Ball gravity
    ballepos[V] += (balle_vitesse[V]*(1.0/60.0) + ((9.81 * (1.0/60.0*1.0/60.0))/2.0))*100.0 #*100 car 100px = 1m
    balle_vitesse[V] += 9.81 * (1.0/60.0)
    ballepos[H] += balle_vitesse[H] * reduc_vitesse
    
    joueur2pos[V] += (joueur2_vitesse[V]*(1.0/60.0) + ((15.0 * (1.0/60.0*1.0/60.0))/2.0))*100.0
    joueur2_vitesse[V] += 15.00* (1.0/60.0)
    
    joueur1pos[V] += (joueur1_vitesse[V]*(1.0/60.0) + ((15.0 * (1.0/60.0*1.0/60.0))/2.0))*100.0
    joueur1_vitesse[V] += 15.00* (1.0/60.0)
    
    
    #-------
    

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
        #reposition de la balle au point de collision


        if x1 > 0: #collision a gauche
            balle_vitesse[H] = -abs(balle_vitesse[H]) * abs(x1)/60 * reduc_vitesse/10 # +joueur1vitesse[H]
            balle_vitesse[V] = -abs(balle_vitesse[V]) * abs(y1)/60 * reduc_vitesse/10 # +joueur1vitesse[V]
        else:
            if x1 < 0: #collision a droite
                balle_vitesse[H] = abs(balle_vitesse[H]) * abs(x1)/60 * reduc_vitesse/10 # +joueur1vitesse[H]
                balle_vitesse[V] = -abs(balle_vitesse[V]) * abs(y1)/60 * reduc_vitesse/10 # +joueur1vitesse[V]

        #get the fuck out

        
    #---Collision balle - joueur2
    if pyt2 <= 90.0:
        #reposition de la balle au point de collision 

        
        if x2 > 0: #collision a gauche
            balle_vitesse[H] = -abs(balle_vitesse[H]) * (abs(x2)/60) * reduc_vitesse/10 # +joueur2vitesse[H]
            balle_vitesse[V] = -abs(balle_vitesse[V]) * (abs(y2)/60) * reduc_vitesse/10 # +joueur2vitesse[V]
        else:
            if x2 < 0: #collision a droite
                balle_vitesse[H] = abs(balle_vitesse[H]) * (abs(x2)/60) * reduc_vitesse/10 # +joueur2vitesse[H]
                balle_vitesse[V] = -abs(balle_vitesse[V]) * (abs(y2)/60) * reduc_vitesse/10 # +joueur2vitesse[V]


        #get the fuck out

        
    
    
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
          
    if joueur2pos[V] >= sol2_position[1]-joueur_rayon:
        joueur2pos[V] = sol2_position[1]-joueur_rayon
        air2 = False
    if joueur1pos[V] >= sol2_position[1]-joueur_rayon:
        joueur1pos[V] = sol2_position[1]-joueur_rayon
        air1 = False       
    #---Collision balle - fenetre HAUT
    else:
        if ballepos[V] < balle_rayon:
            ballepos[V] = balle_rayon
            balle_vitesse[V] = -balle_vitesse[V]

    
    #---Dessin a chaque tour (60/sec)
    #---Dessin l ecran
    fenetre.fill(blanc)
    #---Dessin joueur1
    fenetre.blit(joueur1, joueur1pos)
    fenetre.blit(joueur2, joueur2pos)
    #---Dessin balle
    pygame.draw.circle(fenetre, noir, (int(ballepos[H]), int(ballepos[V])), balle_rayon)
    pygame.draw.circle(fenetre, blanc, (int(ballepos[H]), int(ballepos[V])), balle_rayon-5)
    #--- Dessin sol    
    pygame.draw.rect(fenetre, blanc, (sol2_position, (1500, 200)))
    pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))

    #--- Afficher (rafraichir) l cran
    pygame.display.flip()
    
    #print reduc_vitesse
    
    #--- 60 images par seconde
    temps.tick(60)

pygame.display.quit()
pygame.quit()

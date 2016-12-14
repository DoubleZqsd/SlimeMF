import pygame , math , time

#---Horizontal Vertical
H = 0
V = 1

#définition d'un nouvel évènement pour représenter une touche qui reste enfoncée
pygame.KEYPRESSED = pygame.USEREVENT

#---Variables qui serviront a determiner le sens dans laquelle le joueur se deplace.
DROITE = 1
GAUCHE = -1
BOUTON_SOURIS_GAUCHE = 1

#---Couleurs
blanc  = ( 255, 255, 255)
noir   = (0, 0, 0)
red = ( 255 , 0 , 0 )
bleu =  (  0,   0, 255)
#---Taille fenetre
fenetre_l = 1280
fenetre_h = 720

#---Taille elements
balle_rayon = 30
joueur_rayon = 60.0
score1 =0
score2 =0 
#---Position elements
ballepos = [640.0, 360.0]
sol_position = [0, fenetre_h - 50]
sol2_position = [0, fenetre_h - 53]
joueur1pos = [ 180 , fenetre_h - 113]
joueur2pos = [ fenetre_l - 300 , fenetre_h - 113]
joueur1_vitesse = [10.0 , 0.0]
joueur2_vitesse = [10.0 , 0.0]
balle_vitesse  = [0.0, 4.0]
lastballpos = [0.0 , 0.0] 
j1pos = [0.0 , 0.0]
j2pos = [0.0 , 0.0]
jou1vit = [ 0.0 , 0.0]
jou2vit = [ 0.0 , 0.0]
#---Variables
reduc_vitesse=8
fini = False
air1 = False
air2 = False
pause = False
menu = True
j1col = False
j2col = False
son = True


#DEFINITIONS


def menu_intro():
    global menu 
    if son :
       pygame.mixer.music.play(-1)
    while menu :
          fenetre.fill(blanc)
          m = pygame.mouse.get_pos()
          if 580>= m[0]>=550 and 390 >= m[1] >= 350 or 610 >= m[0] >= 580 and 405 >= m[1]>315 or 670 >= m[0] >= 610 and 420 >= m[1] >=300 or 700 >= m[0] >= 670 and 400 >= m[1] >= 315  :
                   fenetre.blit(joueur1, (joueur1pos[H] ,joueur1pos[V]))
                   fenetre.blit(joueur2, (joueur2pos[H] , joueur2pos[V]))
                   fenetre.blit(goal1 , (0,sol2_position[V]-220))
                   fenetre.blit(goal2 , (fenetre_l-160,sol2_position[V]-220))
                   pygame.draw.circle(fenetre, noir, (640,360), 30)
          else :
                   fenetre.blit(logo,(580,300))
          for evenement in pygame.event.get():
              if evenement.type == pygame.QUIT:
                 pygame.quit()
              if evenement.type == pygame.MOUSEBUTTONDOWN:
                 m = evenement.pos   
                 if 580>= m[0]>=550 and 390 >= m[1] >= 350 or 610 >= m[0] >= 580 and 405 >= m[1]>315 or 670 >= m[0] >= 610 and 420 >= m[1] >=300 or 700 >= m[0] >= 670 and 400 >= m[1] >= 315  :
                    if evenement.button == BOUTON_SOURIS_GAUCHE : 
                       menu = False
                    
          

          
          titrejeu = pygame.image.load('titre.png').convert_alpha(fenetre)
          titrejeu = pygame.transform.scale(titrejeu,(500,230))
          fenetre.blit(titrejeu,(390,50))
          pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))
          pygame.display.flip()
          
def menu_pause() : 
    global pause , menu , fini , joueur1pos , joueur2pos , ballepos , joueur1_vitesse , joueur2_vitesse , balle_vitesse , score1 , score2 , son
    fenetre.fill(blanc)
    if son :
       pygame.mixer.music.play(-1)
    while pause :
          pause = time.time()
          mouse = pygame.mouse.get_pos()
          if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 250 and mouse[1]<= 300 :
             fenetre.blit(reprendre2,(435,250))
          else :
             fenetre.blit(reprendre,(435,250))
          if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 325 and mouse[1]<= 375 :
             fenetre.blit(recommencer2,(435,325))
          else :
             fenetre.blit(recommencer,(435,325))
          if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 400 and mouse[1]<= 450 or son :
             fenetre.blit(son2,(435,400))
          elif mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 400 and mouse[1]<= 450 or not son :
             fenetre.blit(son3,(435,400))
          if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 475 and mouse[1]<= 525 :
             fenetre.blit(quitter2,(435,475))
          else :
             fenetre.blit(quitter,(435,475))
          for evenement in pygame.event.get():
              if evenement.type == pygame.QUIT:
                 pygame.quit()
              if evenement.type == pygame.MOUSEBUTTONDOWN:
                 mouse = evenement.pos   
                 if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 250 and mouse[1]<= 300 :
                    if evenement.button == BOUTON_SOURIS_GAUCHE :
                       pause = False

                 if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 325 and mouse[1]<= 375 :
                    if evenement.button == BOUTON_SOURIS_GAUCHE :
                       joueur1pos = [ 180 , fenetre_h - 113]
                       joueur2pos = [ fenetre_l - 300 , fenetre_h - 113]
                       ballepos = [640.0, 360.0]
                       joueur1_vitesse = [10.0 , 0.0]
                       joueur2_vitesse = [10.0 , 0.0]
                       balle_vitesse  = [0.0, 0.0]
                       score1 = 0
                       score2 = 0
                       menu = True
                       pause = False
                 if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 475 and mouse[1]<= 525 :
                    if evenement.button == BOUTON_SOURIS_GAUCHE:
                       fini = True
                       pause = False
                 if mouse[0] >= 435 and mouse[0]<=835 and mouse[1] >= 400 and mouse[1]<= 450 :
                    if evenement.button == BOUTON_SOURIS_GAUCHE:
                       son = not son
                       if not son :
                          pygame.mixer.music.pause()
                       if son :
                          pygame.mixer.music.play(-1)
                          pygame.mixer.music.unpause()
          logo2 = pygame.transform.scale(logo ,(150,150))
          fenetre.blit(logo2,(565,50))
          pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))

          pygame.display.flip()  
    
          
          
          
          
          
          
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
                  joueur2_vitesse[V] -= 6.0
                  air2 = True
def deplace_v_joueur1(sens):       
               global air1
               if not air1 :
                  joueur1_vitesse[V] -= 6.0 
                  air1 = True
                  
#---Fonction collision joueurs
def collisionJoueur(x1pos , y1pos, numjoueur):
   global H
   global V
   global balle_vitesse
   global reduc_vitesse
   global lastballpos
   canDo = False
   
   
   #---Calcul Alpha (vecteur arrivee balle - sol)
   if numjoueur == 1:
      ax = ballepos[H] - lastballpos[H] - jou1vit[H] #--Composante X vecteur arrivee balle
      ay = ballepos[V] - lastballpos[V] - joueur1_vitesse[V]#--Composante Y vecteur arrivee balle
      air = air1
   elif numjoueur == 2:
      ax = ballepos[H] - lastballpos[H] - jou2vit[H]
      ay = ballepos[V] - lastballpos[V] - joueur2_vitesse[V]
      air = air2

   if ay < 0 and air == False:
      #rebond sur plat dessous joueur
      if numjoueur == 1:
         balle_vitesse[V] = -balle_vitesse[V] + 2* joueur1_vitesse[V]
      elif numjoueur == 2:
         balle_vitesse[V] = -balle_vitesse[V] + 2* joueur2_vitesse[V]
          
   else:
      #if abs(x1pos) < 1e-4 :
       #  #collision sur plat dessus joueur
        # balle_vitesse[V] = -balle_vitesse[V] * 0.8
             
      
         #collision sur le cote 
         #---Calcul Theta (droite centre joueur et balle - sol)
         theta = math.atan2(y1pos,-x1pos)


         alpha = math.atan2( ay,-ax )

         #---Calcul gamma (angle arrivee balle - perpendiculaire tangente point de collision)
         gamma = alpha - theta

         #---Calcul beta (angle rebond balle - sol)
         beta = alpha - 2 * gamma

         #---Calcul vecteur arrivee balle
         va = math.sqrt( (ax*ax) + (ay*ay)) * 0.8
         print('va: ' + str(va))
         if va < 0.15:
            va = 25.0
         #---Decomposition X Y du vecteur rebond balle
         rx = math.cos(beta) * va

         ry = -math.sin(beta) * va

         #---Application du vecteur rebond a la balle
         if numjoueur == 1:         
            balle_vitesse[V] = (ry + joueur1_vitesse[V] - 0.13333) * 0.8
            balle_vitesse[H] = rx + jou1vit[H]
            print('rebond joueur1')
            print('vitesse H: ' + str(jou1vit[H]) + ' et V: ' + str(joueur1_vitesse[V]))

         elif numjoueur == 2:
            balle_vitesse[V] = (ry + joueur2_vitesse[V] - 0.13333) * 0.8
            balle_vitesse[H] = rx + jou2vit[H]
            print('rebond joueur2')
            print('vitesse H: ' + str(jou2vit[H]) + ' et V: ' + str(joueur2_vitesse[V]))
         
                   
         #---Regain energie balle
         reduc_vitesse = 8

def score():
   global score1 , score2 , ballepos , balle_vitesse , joueur1pos , joueur2pos , joueur1_vitesse , joueur2_vitesse 
   pygame.draw.rect(fenetre, noir, ((500,60),(275,115)))
   pygame.draw.rect(fenetre, blanc, ((515,75),(245,85)))
   police = pygame.font.SysFont('Arial', 60, True)
   scores = police.render(str(score1) + "   -   " + str(score2) , True, noir )
   fenetre.blit(scores,(542,85))
   pygame.display.flip()
   

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

def entrees():
      global fini
      global now
      global pause
      now = pygame.time.get_ticks()
      scan(gc)
      for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RIGHT :
               deplace_h_joueur2(DROITE)
               jou2vit[H] = 10.0
            if evenement.key ==pygame.K_LEFT:
               deplace_h_joueur2(GAUCHE)
               jou2vit[H] = -10.0
            if evenement.key ==pygame.K_d:
               deplace_h_joueur1(DROITE)
               jou1vit[H] = 10.0             
            if evenement.key ==pygame.K_q:
               deplace_h_joueur1(GAUCHE)
               jou1vit[H] = -10.0                        
            if evenement.key ==pygame.K_UP :
               deplace_v_joueur2(DROITE)
            if evenement.key ==pygame.K_z :
               deplace_v_joueur1(DROITE)
            if evenement.key ==pygame.K_TAB :
               pause = not pause
        if evenement.type == pygame.KEYPRESSED:
            if evenement.key == pygame.K_RIGHT :
               deplace_h_joueur2(DROITE)
            if evenement.key ==pygame.K_LEFT:
               deplace_h_joueur2(GAUCHE)
            if evenement.key ==pygame.K_d:
               deplace_h_joueur1(DROITE)             
            if evenement.key==pygame.K_q:
               deplace_h_joueur1(GAUCHE)                
            if evenement.key ==pygame.K_UP :
               deplace_v_joueur2(DROITE)
            if evenement.key ==pygame.K_z :
               deplace_v_joueur1(DROITE)
        if evenement.type == pygame.KEYUP:
            if evenement.key == pygame.K_RIGHT:
               jou2vit[H] = 0
            if evenement.key == pygame.K_LEFT:
               jou2vit[H] = 0
            if evenement.key == pygame.K_d:
               jou1vit[H] = 0
            if evenement.key == pygame.K_q:
               jou1vit[H] = 0
             
             
             

#----------PYGAME INIT--------------
pygame.init()
##############
fenetre_taille = (fenetre_l, fenetre_h)
fenetre = pygame.display.set_mode(fenetre_taille)
fenetre.fill(blanc)
temps = pygame.time.Clock()
paused =time.time()
joueur1 = pygame.image.load('joueur1.png').convert_alpha(fenetre)
joueur1 = pygame.transform.scale(joueur1,(120,60))
joueur2 = pygame.image.load('joueur2.png').convert_alpha(fenetre)
joueur2 = pygame.transform.scale(joueur2,(120,60))

goal1 = pygame.image.load('goal1.png').convert_alpha(fenetre)
goal1 = pygame.transform.scale(goal1,(160,220))
goal2 = pygame.image.load('goal2.png').convert_alpha(fenetre)
goal2 = pygame.transform.scale(goal2,(160,220))

logo = pygame.image.load('logo.png').convert_alpha(fenetre)
logo = pygame.transform.scale(logo,(120,120))

reprendre = pygame.image.load('reprendre.png').convert_alpha(fenetre)
reprendre = pygame.transform.scale(reprendre,(400,50))
reprendre2 = pygame.image.load('reprendre2.png').convert_alpha(fenetre)
reprendre2 = pygame.transform.scale(reprendre2,(400,50))

recommencer = pygame.image.load('Recommencer.png').convert_alpha(fenetre)
recommencer = pygame.transform.scale(recommencer,(400,50))
recommencer2 = pygame.image.load('Recommencer2.png').convert_alpha(fenetre)
recommencer2 = pygame.transform.scale(recommencer2,(400,50))

quitter = pygame.image.load('Quitter.png').convert_alpha(fenetre)
quitter = pygame.transform.scale(quitter,(400,50))
quitter2 = pygame.image.load('Quitter2.png').convert_alpha(fenetre)
quitter2 = pygame.transform.scale(quitter2,(400,50))

son3 = pygame.image.load('Son.png').convert_alpha(fenetre)
son3 = pygame.transform.scale(son3,(400,50))
son2 = pygame.image.load('Son2.png').convert_alpha(fenetre)
son2 = pygame.transform.scale(son2,(400,50))

message = pygame.image.load('message.png').convert_alpha(fenetre)
message = pygame.transform.scale(message,(300,130))

mur = pygame.mixer.Sound("mur.wav")
balj = pygame.mixer.Sound("joueur.wav")
man = pygame.mixer.Sound("goal.wav")
musique = pygame.mixer.music.load("musique.wav")

##############

gc = nouvelleGestionClavier()
repeteTouche(gc, pygame.K_q, 25, 0)
repeteTouche(gc, pygame.K_z, 0, 0)
repeteTouche(gc, pygame.K_d, 25, 0)
repeteTouche(gc, pygame.K_LEFT, 25, 0)
repeteTouche(gc, pygame.K_RIGHT, 25, 0)
repeteTouche(gc, pygame.K_UP, 0, 0)


#--- Boucle principale
while not fini:
    
    menu_pause()
    menu_intro()

    if not pause and not menu:
       entrees()
       pygame.mixer.music.stop()
         #--- Gravity
        #---Derniere position balle
       lastballpos[H] = ballepos [H]
       lastballpos[V] = ballepos [V]
       #print('lastballpos=' + str(lastballpos))
       #---Ball gravity
       ballepos[V] += (balle_vitesse[V]*(1.0/60.0) + ((9.81 * (1.0/60.0*1.0/60.0))/2.0))*100.0 #*100 car 100px = 1m
       balle_vitesse[V] += 9.81 * (1.0/60.0)
       ballepos[H] += balle_vitesse[H] * reduc_vitesse/10
    
       joueur2pos[V] += (joueur2_vitesse[V]*(1.0/60.0) + ((8.0 * (1.0/60.0*1.0/60.0))/2.0))*100.0
       joueur2_vitesse[V] += 8.00* (1.0/60.0)
    
       joueur1pos[V] += (joueur1_vitesse[V]*(1.0/60.0) + ((8.0 * (1.0/60.0*1.0/60.0))/2.0))*100.0
       joueur1_vitesse[V] += 8.00* (1.0/60.0)
    
   
       #---Def pos joueurs au centre du cercle
       j1pos[H] = joueur1pos[H]+60
       j1pos[V] = joueur1pos[V]+60
       
       j2pos[H] = joueur2pos[H]+60
       j2pos[V] = joueur2pos[V]+60
        #---Calculons Pythagore
       
       #---Variables pyt
       x1pos = j1pos[H]-ballepos[H]
       y1pos = j1pos[V]-ballepos[V]

       x2pos = j2pos[H]-ballepos[H]
       y2pos = j2pos[V]-ballepos[V]
    
       #---Distance entre balle et joueur1
       pyt1 = math.sqrt( (x1pos*x1pos) + (y1pos*y1pos) )
       #---Distance entre balle et joueur2
       pyt2 = math.sqrt( (x2pos*x2pos) + (y2pos*y2pos) )
       
       #---Collision balle - joueur1    
       if pyt1 <= 90.0 and j1col == False:
          j1col = True
          if son :
             pygame.mixer.Sound.play(balj)
          #appel fonction collisionJoueur pour le joueur 1
          collisionJoueur(x1pos, y1pos, 1)                       
       elif pyt1 > 90.0:
          j1col = False
          
       #---Collision balle - joueur 2   
       if pyt2 <= 90.0 and j2col == False:
          j2col = True
          if son :
             pygame.mixer.Sound.play(balj)
          #appel fonction collisionJoueur pour le joueur 2
          collisionJoueur(x2pos, y2pos, 2)                 
       elif pyt2>90.0:
          j2col = False
          
          
       
    
    
    #---Collision balle - fenetre DROIT
       if ballepos[H] + balle_rayon >= fenetre_l:
          ballepos[H] = fenetre_l - balle_rayon
          balle_vitesse[H] = -balle_vitesse[H] * 0.8
          if son :
             pygame.mixer.Sound.play(mur)
    #---Collision balle - fenetre GAUCHE
       else:
          if ballepos[H] < balle_rayon:
             ballepos[H] = balle_rayon
             balle_vitesse[H] = -balle_vitesse[H] * 0.8
             if son :
                pygame.mixer.Sound.play(mur)
    #---Collision balle - fenetre BAS
          if ballepos[V] + balle_rayon >= sol2_position[1]:
             ballepos[V] = sol2_position[1] - balle_rayon
             balle_vitesse[V] = -balle_vitesse[V]*reduc_vitesse/10
             reduc_vitesse-=1
             if reduc_vitesse < 0:
                reduc_vitesse = 0
          
       if joueur2pos[V] >= sol2_position[1]-joueur_rayon:
          joueur2pos[V] = sol2_position[1]-joueur_rayon
          joueur2_vitesse[V] = 0.0
          air2 = False
    
       if joueur1pos[V] >= sol2_position[1]-joueur_rayon:
          joueur1pos[V] = sol2_position[1]-joueur_rayon
          joueur1_vitesse[V] = 0.0
          air1 = False
        
    #---Collision balle - fenetre HAUT
       
       if ballepos[V] < balle_rayon:
          ballepos[V] = balle_rayon
          balle_vitesse[V] = -balle_vitesse[V] * 0.8
          if son :
             pygame.mixer.Sound.play(mur)   
    
    #---Balle dans le goal 2
       if ballepos[V] >= 470 and ballepos[H] >= fenetre_l - 85:
          score1 += 1
          ballepos=[640.0, 50.0]
          balle_vitesse=[0.0 , 0.0]
          joueur1pos = [ 180 , fenetre_h - 113]
          joueur2pos = [ fenetre_l - 300 , fenetre_h - 113]
          joueur1_vitesse = [10.0 , 0.0]
          joueur2_vitesse = [10.0 , 0.0]
          fenetre.blit(message,(535,310))
          if son : 
             pygame.mixer.Sound(man)
          time.sleep(1)
    #---Balle dans le Goal 1
       if ballepos[V] >= 470 and ballepos[H] <= 85:
          score2 += 1
          ballepos=[640.0, 50.0]
          balle_vitesse=[0.0 , 0.0]
          joueur1pos = [ 180 , fenetre_h - 113]
          joueur2pos = [ fenetre_l - 300 , fenetre_h - 113]
          joueur1_vitesse = [10.0 , 0.0]
          joueur2_vitesse = [10.0 , 0.0]
          
          fenetre.blit(message,(535,310))
          if son : 
             pygame.mixer.Sound(man)
          time.sleep(1)


    #---Collision dessus goal 1
       if ballepos[V] > 440 and ballepos[V] < 480 and ballepos[H] < 140:
          ballepos[V] = 452
          balle_vitesse[V] = -balle_vitesse[V] * reduc_vitesse/10
          reduc_vitesse -= 1
          if reduc_vitesse < 0:
             reduc_vitesse = 0


    #---Collision dessus goal 2
       if ballepos[V] > 440 and ballepos[V] < 480 and ballepos[H] > fenetre_l - 140 :
          ballepos[V] = 452
          balle_vitesse[V] = -balle_vitesse[V] * reduc_vitesse/10
          reduc_vitesse -= 1
          if reduc_vitesse < 0:
             reduc_vitesse = 0
          
    
    
    #---Dessin a chaque tour (60/sec)
    #---Dessin l ecran
       fenetre.fill(blanc)
    #---Dessin balle
       pygame.draw.circle(fenetre, noir, (int(ballepos[H]), int(ballepos[V])), balle_rayon)
       pygame.draw.circle(fenetre, blanc, (int(ballepos[H]), int(ballepos[V])), balle_rayon-5)
    #---Dessin joueurs + goal
       fenetre.blit(joueur1, joueur1pos)
       fenetre.blit(joueur2, joueur2pos)
       fenetre.blit(goal1 , (-30.0,sol2_position[V]-215.0))
       fenetre.blit(goal2 , (fenetre_l-130.0,sol2_position[V]-215.0))
    
    #--- Dessin sol    
       pygame.draw.rect(fenetre, blanc, (sol2_position, (1500, 200)))
       pygame.draw.rect(fenetre, noir, (sol_position, (1500, 200)))
       score()

    #--- Afficher (rafraichir) l écran
    pygame.display.flip()
    
    
    #--- 60 images par seconde
    temps.tick(60)

pygame.display.quit()
pygame.quit()

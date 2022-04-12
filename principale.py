# %%
import math 
from random import randint
import pygame

liste = []
class t_vaisseau:
    def __init__(self, mon_ecran):
        self.image_model = pygame.image.load('vaisseau.jpg') 
        self.image = self.image_model
        self.mon_y = 310
        self.mon_x = 540
        self.angle = 0
        self.nv_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (self.mon_x,self.mon_y)
        mon_ecran.blit(self.nv_image, self.rect)
        self.Vx = 0
        self.Vy = 0
        self.Ax = 0
        self.Ay = 0
        self.VA = 0
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))

    
    def tourner(self):
        self.nv_image = self.image
        self.angle += self.VA * mon_delai
        self.nv_image = pygame.transform.rotate(self.nv_image, self.angle)
        self.rect = self.nv_image.get_rect()
        self.rect.center = (self.mon_x, self.mon_y)
        mon_ecran.blit(self.nv_image, self.rect)

    def avancer(self):
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.Vx = self.Ax * mon_delai
        self.Vy = self.Ay * mon_delai
        self.mon_x += self.cosinus * self.Vx
        self.mon_y -= self.sinus * self.Vy
        self.nv_image = self.image
        self.nv_image = pygame.transform.rotate(self.nv_image, self.angle)
        self.rect = self.nv_image.get_rect()
        self.rect.center = (self.mon_x, self.mon_y)
        #régler pb de display Surface Error
        mon_ecran.blit(self.nv_image, self.rect)


class t_missile:
    def __init__(self, vaisseau1 : t_vaisseau):
        self.img_missile_model = pygame.image.load('missile.png')
        self.img_missile = self.img_missile_model
        self.le_x = vaisseau1.mon_x
        self.le_y = vaisseau1.mon_y
        self.l_angle = vaisseau1.angle
        self.Vx = 0
        self.Vy = 0
        self.rect_missile = self.img_missile.get_rect()
        self.son_cosinus = math.cos(math.radians(self.l_angle + 90))
        self.son_sinus = math.sin(math.radians(self.l_angle + 90))
    
    def est_dans_la_fen(self):
        return 0 <= self.le_x <= x_fen and 0 <= self.le_y <= y_fen

    def tir_de_missile(self, vaisseau1 : t_vaisseau):
        self.le_x += self.son_cosinus * mon_delai * 100
        self.le_y -= self.son_sinus * mon_delai * 100
        self.nv_image_missile = self.img_missile
        self.nv_image_missile = pygame.transform.rotate(self.img_missile, self.l_angle)
        self.rect_missile = self.img_missile.get_rect()
        self.rect_missile.center = (self.le_x, self.le_y)
        mon_ecran.blit(self.img_missile, self.rect_missile)
        
liste_asteroid = []
class t_asteroid:
    def __init__(self):
        self.img_grand = pygame.image.load('asteroid_grand.png')
        self.img_moyen = pygame.image.load('asteroid_moyenne.png')
        self.img_petit = pygame.image.load('asteroid_petit.png')
        nb_alea = randint(1, 3)
        if nb_alea == 1:
            self.le_x = 0
            self.le_y = randint(1, 621)
        else:
            self.le_x = randint(1, 1080)
            self.le_y = 0
        self.l_angle = randint(1, 180)
        nb = randint(1, 4)
        if nb == 1:
            self.img = self.img_petit
        elif nb==2:
            self.img = self.img_moyen
        else:
            self.img = self.img_grand
        self.img2 = self.img
        self.rect_asteroid = self.img.get_rect()
        self.son_cosinus = math.cos(math.radians(self.l_angle + 90))
        self.son_sinus = math.sin(math.radians(self.l_angle + 90))
        
    def deplacement(self):
        self.cosinus = math.cos(math.radians(self.l_angle + 90))
        self.sinus = math.sin(math.radians(self.l_angle + 90))
        self.Vx = 50 * mon_delai
        self.Vy = 50 * mon_delai
        self.le_x += self.cosinus * self.Vx
        self.le_y -= self.sinus * self.Vy
        self.img2 = self.img
        self.img2 = pygame.transform.rotate(self.img2, self.l_angle)
        self.rect_asteroid = self.img2.get_rect()
        self.rect_asteroid.center = (self.le_x, self.le_y)
        mon_ecran.blit(self.img2, self.rect_asteroid)
    

class t_gestion_tirs:
    def __init__(self):
        pass

pygame.init()
#variable de la fenetre
x_fen = 1080
y_fen = 620
#inititialiser l'écran avec les dimensions suivantes
mon_ecran = pygame.display.set_mode((x_fen, y_fen))
#fond de l'écran en noir
black = (0, 0, 0) 
#écran de fond en noir
mon_ecran.fill(black)
#nom de la fenetre pygame qui va se lancer
pygame.display.set_caption('Project Asteroid') 

#horloge
mon_horloge = pygame.time.Clock()

#jeu en cours ou arrêté
game = True

#création d'un t_vaisseau
vaisseau1 = t_vaisseau(mon_ecran)

mon_delai = mon_horloge.tick(60) /1000

#création d'un asteroid
def ajt_asteroid():
    liste_asteroid.append(t_asteroid())
    liste_asteroid[-1].deplacement()

#création accumulateur
accumulateur = 0

ajt_asteroid()
while game :
    #physique
    mon_delai = mon_horloge.tick(60) / 1000
    liste_bis_asteroid = []
    if accumulateur < 3.5:
        accumulateur+= mon_delai
    else:
        ajt_asteroid()
        accumulateur = 0

    #dessin
    mon_ecran.fill(black)
    mon_ecran.blit(vaisseau1.nv_image, vaisseau1.rect)
    for elem in liste:
        mon_ecran.blit(elem.img_missile, elem.rect_missile)

    for asteroid in liste_asteroid:
        for missile in liste:
            if (vaisseau1.mon_x == (asteroid.le_x -5 <= asteroid.le_x <= asteroid.le_x + 5)) and (vaisseau1.mon_y == (asteroid.le_y -5 <= asteroid.le_y <= asteroid.le_y + 5)):
                game = False
                pygame.quit()

            if (missile.le_x == (asteroid.le_x -5 <= asteroid.le_x <= asteroid.le_x + 5)) and (missile.le_y == (asteroid.le_y -5 <= asteroid.le_y <= asteroid.le_y + 5)):
                pass
            else:
                if asteroid not in liste_bis_asteroid:
                    liste_bis_asteroid.append(asteroid)
    liste_asteroid = liste_bis_asteroid
    liste_bis_asteroid = []
    for asteroid in liste_asteroid:
        asteroid.deplacement()
    
    pygame.display.update()
    #missile pour boucle missile
    missile_on = False

    #gestion des evt
    for event in pygame.event.get() :

        #j'ai choisi une vitesse angulaire de 65 sinon le jeu n'est pas assez fluide
        #ainsi qu'une accélération de 50 pour que ce soit rapide
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                vaisseau1.VA -= 65
            if event.key == pygame.K_q:
                vaisseau1.VA += 65
            if event.key == pygame.K_z:
                vaisseau1.Ax += 50
                vaisseau1.Ay += 50
            if event.key == pygame.K_e:
                liste.append(t_missile(vaisseau1))
                missile_on = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                vaisseau1.VA += 65
            elif event.key == pygame.K_q:
                vaisseau1.VA -= 65
            elif event.key == pygame.K_z:
                vaisseau1.Ax = 0
                vaisseau1.Ay = 0
            elif event.key == pygame.K_e:
                missile_on = False
            
        if event.type == pygame.QUIT:
            pygame.quit()           
            quit()

        
    #gestion des missiles
    for elem in liste:
        if elem.est_dans_la_fen():
            elem.tir_de_missile(vaisseau1)

    #ici lorsque l'on avance en tournant nous n'avons pas de boost (+ d'accélération)
    #mais en ligne droite [voilà le pourquoi du deuxième elif], la vitesse accélère progressivement
    #et si on vient à tourner, il y a une déscélération porgressive [premier et deuxième if/elif]

    if vaisseau1.VA != 0 and vaisseau1.Ax > 50 and vaisseau1.Ay > 50:
        vaisseau1.Ax -= 10
        vaisseau1.Ay -= 10
        vaisseau1.tourner()
        vaisseau1.avancer()

    elif vaisseau1.Ax != 0 and vaisseau1.Ay !=0:
        vaisseau1.Ax += 10
        vaisseau1.Ay += 10
        vaisseau1.avancer()

    elif vaisseau1.VA > 0:
        vaisseau1.tourner()

    elif vaisseau1.VA < 0:
        vaisseau1.tourner()


    #POUR NE PAS SORTIR DE LA FENETRE (VAISSEAU)
    #ici changer les valeurs de mon_x et mon_y est judicieux car 
    #changer la valeur du centre du rectangle va nous bloquer le missile
    if vaisseau1.mon_x > x_fen and vaisseau1.mon_y > y_fen:
        vaisseau1.mon_x = 1
        vaisseau1.mon_y = 1
    elif vaisseau1.mon_x > x_fen and vaisseau1.mon_y < 0:
        vaisseau1.mon_x = 1
        vaisseau1.mon_y = y_fen
    elif vaisseau1.mon_x < 0 and vaisseau1.mon_y > y_fen:
        vaisseau1.mon_x = x_fen
        vaisseau1.mon_y = 1
    elif vaisseau1.mon_x < 0 and vaisseau1.mon_y < 0:
        vaisseau1.mon_x = x_fen
        vaisseau1.mon_y = y_fen
    elif vaisseau1.mon_x > x_fen:
        vaisseau1.mon_x = 1
        vaisseau1.mon_y = vaisseau1.mon_y
    elif vaisseau1.mon_y > y_fen:
        vaisseau1.mon_x = vaisseau1.mon_x
        vaisseau1.mon_y = 1
    elif vaisseau1.mon_x < 0:
        vaisseau1.mon_x = x_fen
        vaisseau1.mon_y = vaisseau1.mon_y
    elif vaisseau1.mon_y < 0:
        vaisseau1.mon_x = vaisseau1.mon_x
        vaisseau1.mon_y = y_fen

    #gestion des missiles
    liste_bis = []
    for elem in liste:
        if 5 < elem.le_x < x_fen -5 and 5 < elem.le_y < y_fen - 5:
            liste_bis.append(elem)
    liste = liste_bis

    #gestion des asteroid
    for elem in liste_asteroid:
        if elem.le_x > x_fen and elem.le_y > y_fen:
            elem.le_x = 1
            elem.le_y = 1
        elif elem.le_x > x_fen and elem.le_y < 0:
            elem.le_x = 1
            elem.le_y = y_fen
        elif elem.le_x < 0 and elem.le_y > y_fen:
            elem.le_x = x_fen
            elem.le_y = 1
        elif elem.le_x < 0 and elem.le_y < 0:
            elem.le_x = x_fen
            elem.le_y = y_fen
        elif elem.le_x > x_fen:
            elem.le_x = 1
            elem.le_y = elem.le_y
        elif elem.le_y > y_fen:
            elem.le_x = elem.le_x
            elem.le_y = 1
        elif elem.le_x < 0:
            elem.le_x = x_fen
            elem.le_y = elem.le_y
        elif elem.le_y < 0:
            elem.le_x = elem.le_x
            elem.le_y = y_fen

    

    
# %%

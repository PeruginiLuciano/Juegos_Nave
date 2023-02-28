import pygame
import sys
import random
from pygame.locals import *
from sys import exit
pygame.init()
file = 'Musica/musicaespacio.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
#Constantes
ANCHO=1280
ALTO= 780
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)
color_blanco=(255,255,255)
score = int (0)
score2 = int(0)
fondo = int(0)
velocidad=int(30)
#jugador
jugadot_size = 30
jugador_pos = [ANCHO/2 ,ALTO-jugadot_size *2]
final_pantalla=ANCHO-jugadot_size
principio_pantalla = 0
final_pantallay=ALTO-jugadot_size

#Enemigos
velocidad_enemigo= 10
enemigo_size= 50
enemigo_pos = [random.randint(0,ANCHO),0]
#Fondo


#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))

background=pygame.image.load("Imagenes/fondo_pygame-bspline.jpg")
player = pygame.image.load("Imagenes/nave_jugad.png").convert()
player.set_colorkey([0,0,0])
game_over = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
def detectar_colision(jugador_pos,enemigo_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	ex = enemigo_pos[0]
	ey = enemigo_pos[1]
	if (ex>= jx and ex<(jx + jugadot_size)) or (jx >= ex and jx < (ex + enemigo_size)):
		if (ey>= jy and ey<(jy + jugadot_size)) or (jy >= ey and jy < (ey + enemigo_size)):
			return True
	return False
while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x= jugador_pos[0]
			y= jugador_pos[1]
			if event.key == pygame.K_LEFT:
				if x > principio_pantalla:

					x-= jugadot_size
				

			if event.key == pygame.K_RIGHT:
				if x < final_pantalla:
					x += jugadot_size

			if event.key == pygame.K_UP:
				if y > principio_pantalla:
					y-= jugadot_size		
			if event.key == pygame.K_DOWN:
				if y < final_pantallay:
					y+= jugadot_size	
			jugador_pos[0] = x
			jugador_pos[1] = y

	if enemigo_pos[1] >= 0 and enemigo_pos[1]< ALTO:
		enemigo_pos[1]+= velocidad_enemigo
	else:
		enemigo_pos[0] = random.randint(0, ANCHO - enemigo_size)
		enemigo_pos[1] = 0
		score += 1
		score2+=1
		print(score)
		
		if score2 == 5:
			score2 = 0
			fondo +=1
			color_azul=(random.randint(50,200),random.randint(50,200),random.randint(50,200))
			velocidad_enemigo += 10
	#Fondo
	for i in range(60):
		xc = random.randint(0,800)
		yc = random.randint(0,600)
		pygame.draw.circle(ventana, color_blanco,(xc,yc),2)		
	#Colisiones
	if detectar_colision(jugador_pos,enemigo_pos):
		game_over = True
	ventana.blit(background,[0,0-score*2])	
	ventana.blit(player,[jugador_pos[0],jugador_pos[1]])	
	#Dibujar enemigo	
	pygame.draw.rect(ventana,color_azul,(enemigo_pos[0],enemigo_pos[1],enemigo_size,enemigo_size))
	#dibujar jugador
	#pygame.draw.rect(ventana,color_rojo,(jugador_pos[0],jugador_pos[1],enemigo_size,enemigo_size))
	#movimiento con mouse
	#mouse_pos = pygame.mouse.get_pos()
	#x1= mouse_pos[0]
	#y1= mouse_pos[1]
	#jugador_pos[0] = x1

	clock.tick(30)
	pygame.display.update()
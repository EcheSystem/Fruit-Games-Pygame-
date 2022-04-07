#impotamos sys y pygame
import sys, pygame

#inicializo
pygame.init()

#Pantalla 
size= 800,600
screen=pygame.display.set_mode(size)

#Nombre de la ventana
pygame.display.set_caption("Frutas, No Preguntes")



width,height=800,600

#posicion
speed=[1,1]
#color
white=255,255,255
black=0,0,0
#Manzana
sierra=pygame.image.load("img/manz.png")
sierrarect=sierra.get_rect()
#Manzana
frutas=pygame.image.load("img/frutas.png")
frutasrect=sierra.get_rect()
#Tranpolin
sier=pygame.image.load("img/piedra.png")
sierRect=sier.get_rect()
sierRect.move_ip(400, 550)
#fondo
fondo=pygame.image.load("img/selva.png")
#FUENTE
fuente =pygame.font.SysFont("arial black", 32)
puntos=0
texto=fuente.render("Score: "+ str(puntos),True,black)
texto2=fuente.render("",True,black)


#condicional
run=True
#bucle del juego
while run:
    #Velocidad
    pygame.time.delay(1)
    for event in pygame.event.get():

        if event.type == pygame.QUIT: run=False

    keys=pygame.key.get_pressed()

    # if keys[pygame.K_UP]:

    #     sierRect=sierRect.move(0,-1)

    # if keys[pygame.K_DOWN]:

    #     sierRect=sierRect.move(0,1)

    if keys[pygame.K_RIGHT]:

        sierRect=sierRect.move(1,0)

    if keys[pygame.K_LEFT]:

        sierRect=sierRect.move(-1,0)

    
    if sierRect.colliderect(sierrarect):
        speed[1]=-speed[1]
        #bucle de puntos
        puntos=puntos+1
        texto=fuente.render("Score: "+ str(puntos),True,black)

    #manzana
    sierrarect=sierrarect.move(speed)
    if sierrarect.left < 0 or sierrarect.right >width:
        speed[0]= -speed[0]
    if sierrarect.top < 0 or sierrarect.bottom >height:
        speed[1]= -speed[1]
        if sierrarect.bottom >height: 
            puntos=puntos-5
            texto=fuente.render("Score: "+ str(puntos),True,black)

    if 100>puntos == 100 :
        texto2=fuente.render("Felicidades Llegaste a 100 ptos: "+ str(puntos),True,black)
        pygame.time.delay(3)
        sierrarect.kill()

    
    
    
    screen.fill(white)
    screen.blit(fondo,(0,0))
    screen.blit(texto,(0,0))
    screen.blit(texto2,(0,0))
    screen.blit(sier,sierRect)
    screen.blit(sierra,sierrarect)
    screen.blit(sierra,sierrarect)
    
    
    pygame.display.flip()

pygame.quit()
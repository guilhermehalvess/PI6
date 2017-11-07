#!/usr/bin/env python
# encoding: utf-8
import sys, pygame
from random import randint
from pygame.locals import *
pygame.init()

#fonte
pygame.font.init()
fonte = pygame.font.get_default_font()
fonte_vento = pygame.font.SysFont(fonte,36)
fonte_barra = pygame.font.SysFont(fonte,24)
fonte_erro = pygame.font.SysFont(fonte,36)


#controle de problema
problema = 0

#Textos
#texto, visivel, cor
texto_vento = fonte_vento.render("Sentido do Vento",1, (0,0,0,0))
texto_decolagem = fonte_barra.render("Ponto de Decolagem",1, (0,0,0,0))
texto_velocidade = fonte_barra.render("280 km/h",1, (0,0,0,0))
texto_problema1 = fonte_erro.render("Problema com vento, abortado!", 1, (0,0,0,0))
texto_problema2 = fonte_erro.render("Problema com chuva, abortado!", 1, (0,0,0,0))
texto_problema3 = fonte_erro.render("Problema com o peso, abortado!", 1, (0,0,0,0))
texto_problema_x_y = [310,20]
#titulo
pygame.display.set_caption('PI 6 - Simulacao de avião')

#tela
size = width, height = 840, 450
screen = pygame.display.set_mode(size)

#limpa tela com preto
limpa_fundo = 0, 0, 0

#peso
peso = randint(0,100)
if peso == 100:
    problema = 3


#vento: variaveis
vento_esquerda = False
vento_direita = False

#vento: seta
seta_direita = pygame.image.load("seta_direita.png")
seta_esquerda = pygame.image.load("seta_esquerda.png")
seta_x_y = [100,40]

#vento: aleatorio
vento = randint(0,10)
if vento <= 9:
    #Avião
    aviao = pygame.image.load("aviao1_direito.png")
    aviao_x = 0
    aviao_y = 320
    aviao_tamanho = 303
    vento_direita = True
    #parametros de decolagem
    ponto_decolagem = 150
    ponto_subida = ponto_decolagem+100
    barra_x_y = [ponto_decolagem+aviao_tamanho, 150]
    velocidade_x_y = [ponto_decolagem+aviao_tamanho-10,100]
    texto_decolagem_x_y = [ponto_decolagem+aviao_tamanho-60, 120]

else:
    #Avião
    print "Vento"
    aviao = pygame.image.load("aviao1_direito.png")
    aviao_x = 0
    aviao_y = 320
    aviao_tamanho = 303
    vento_direita = False
    #parametros de decolagem
    ponto_decolagem = 150
    ponto_subida = ponto_decolagem+100
    barra_x_y = [ponto_decolagem+aviao_tamanho, 150]
    texto_decolagem_x_y = [ponto_decolagem+aviao_tamanho-60, 120]
    problema = 1 #vento


chuva = randint(0,10)
if chuva > 9:
    problema = 2 #chuva
    print "chuva"
    #fundo
    background = pygame.image.load("background_chuva.jpg")
    backgroundrect = background.get_rect()
    #chama imagem backgroud chuva
else:
    #fundo
    background = pygame.image.load("background_sol.jpg")
    backgroundrect = background.get_rect()

#imagem do ponto de decolagem
barra = pygame.image.load("barra.png")

#musica
if problema == 0:
    pygame.mixer.music.load("decolando.wav")
    pygame.mixer.music.play()
elif problema == 1:
    pygame.mixer.music.load("vento2.mp3")
    pygame.mixer.music.play()
elif problema == 2:
    pygame.mixer.music.load("chuva.mp3")
    pygame.mixer.music.play()
elif problema == 3:
    pygame.mixer.music.load("vento2.mp3")
    pygame.mixer.music.play()

#Auxiliar voo
aux_voo = 0
#quantidade que sobe
sustentacao = 1
#contador de subida, passando de 3 para de subir
cont_subida = 0
#ativa exibir velocidade
velocidade_exibir = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #controle da variavel aux_voo
    if aux_voo == 21:
        aux_voo = 0

    #Aviao eixo x
    if aviao_x > (width):
        aviao_x = aviao_x
    elif aviao_x <= (width):
        if (aux_voo == 20) and problema == 0:
            cont_subida = cont_subida + 1
            sustentacao = sustentacao + 1
            if cont_subida == 3:
                aux_voo = 22
                velocidade_exibir = 1
        aviao_x = aviao_x + sustentacao
        aux_voo = aux_voo + 1

    #Aviao eixo y
    if aviao_y > height+100:
        aviao_y = aviao_y
    elif (aviao_y < height and aviao_x > ponto_decolagem and problema == 0):
        aviao_y = aviao_y - 1
    elif (aviao_y < height and aviao_x > ponto_subida and problema == 0):
        aviao_y = aviao_y - 3


    #Limpando fundo
    screen.fill(limpa_fundo)

    #desenha fundo
    screen.blit(background, backgroundrect)

    #desenha indicação de vento
    if vento_direita == True:
        screen.blit(seta_esquerda, seta_x_y)

    else:
        screen.blit(seta_direita, seta_x_y)

    #desenha avião
    screen.blit(aviao, (aviao_x,aviao_y))

    #desenha texto vento
    screen.blit(texto_vento,(10,15))

    #desenha barra de decolagem
    screen.blit(barra,barra_x_y)

    #desenha texto de ponto de decolagem
    screen.blit(texto_decolagem,texto_decolagem_x_y)

    #problemas
    if problema == 1:
        screen.blit(texto_problema1, texto_problema_x_y)
    elif problema == 2:
        screen.blit(texto_problema2, texto_problema_x_y)
    elif problema == 3:
        screen.blit(texto_problema3, texto_problema_x_y)

    if velocidade_exibir == 1:
        screen.blit(texto_velocidade, velocidade_x_y)

    #atualiza tela
    pygame.display.flip()

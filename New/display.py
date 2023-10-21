import pygame
from InputListener import InputListener

pygame.init()
largura, altura = 280, 480

tela = pygame.display.set_mode((largura, altura))

cor_fundo = (255, 255, 255)

pygame.font.init()
fonte = pygame.font.Font("component library/Font.ttc", 36)


texto = ""
cor_texto = (0, 0, 0)
renderizado = fonte.render(texto, True, cor_texto)

posicao_texto = renderizado.get_rect()
posicao_texto.center = (largura // 2, altura // 2)


input_listener = InputListener()
text = input_listener.input_handler.file
executando = True
while executando:
    
    texto = text
    renderizado = fonte.render(texto, True, cor_texto)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    tela.fill(cor_fundo)
    tela.blit(renderizado, posicao_texto)

    pygame.display.flip()

pygame.quit()
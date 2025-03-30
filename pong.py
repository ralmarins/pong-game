import pygame
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo a tela do jogo
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Definindo as variáveis do jogo
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10

# Posições iniciais dos paddles
paddle1_y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)
paddle2_y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)

# Posição inicial da bola
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_velocity_x = 3 * random.choice((1, -1))  # Bola começa em direção aleatória
ball_velocity_y = 3 * random.choice((1, -1))  # Bola começa em direção aleatória

# Função para desenhar o jogo
def draw_game():
    screen.fill(BLACK)
    
    # Desenhando os paddles
    pygame.draw.rect(screen, WHITE, (10, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 10 - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Desenhando a bola
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE // 2)
    
    # Desenhando as bordas da tela
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
    
    pygame.display.update()

# Função principal do jogo
def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_velocity_x, ball_velocity_y
    
    # Controlando o relógio do jogo
    clock = pygame.time.Clock()
    
    # Loop principal do jogo
    running = True
    while running:
        # Atraso de frames (60 frames por segundo)
        clock.tick(60)
        
        # Processando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Movimentação do paddle 1 (controle do jogador)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle1_y > 0:
            paddle1_y -= 5
        if keys[pygame.K_DOWN] and paddle1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle1_y += 5
        
        # Movimentação do paddle 2 (IA ou controle futuro)
        if paddle2_y + PADDLE_HEIGHT // 2 < ball_y:
            paddle2_y += 3
        elif paddle2_y + PADDLE_HEIGHT // 2 > ball_y:
            paddle2_y -= 3

        # Movimentação da bola
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y
        
        # Colisão da bola com o topo e fundo
        if ball_y <= 0 or ball_y >= SCREEN_HEIGHT:
            ball_velocity_y *= -1
        
        # Colisão da bola com os paddles
        if (ball_x <= 10 + PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT) or \
           (ball_x >= SCREEN_WIDTH - 10 - PADDLE_WIDTH and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT):
            ball_velocity_x *= -1
        
        # Se a bola sair da tela
        if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_velocity_x *= random.choice((1, -1))
            ball_velocity_y *= random.choice((1, -1))
        
        # Atualizar a tela
        draw_game()

    pygame.quit()

# Iniciar o jogo
game_loop()

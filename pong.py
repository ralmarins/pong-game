import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamanho da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Configurando a tela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Definindo as dimensões das raquetes
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# Velocidade das raquetes
PADDLE_SPEED = 10

# Definindo o tamanho da bola
BALL_SIZE = 15

# Posições iniciais da raquete e da bola
paddle1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle1_x = 10
paddle2_x = SCREEN_WIDTH - 10 - PADDLE_WIDTH

# Posições iniciais da bola
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

# Velocidade inicial da bola
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))

# Definindo o relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Função para desenhar a raquete
def draw_paddle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Função para desenhar a bola
def draw_ball(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), BALL_SIZE // 2)

# Função para desenhar o placar
def draw_score(player1_score, player2_score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

# Função principal do jogo
def game():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_speed_x, ball_speed_y

    # Placar
    player1_score = 0
    player2_score = 0

    # Controle de movimento das raquetes
    paddle1_speed = 0
    paddle2_speed = 0

    # Definindo a dificuldade da IA (quanto maior a velocidade, mais difícil)
    difficulty = 2

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_speed = -PADDLE_SPEED
                elif event.key == pygame.K_s:
                    paddle1_speed = PADDLE_SPEED
                if event.key == pygame.K_UP:
                    paddle2_speed = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    paddle2_speed = PADDLE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s]:
                    paddle1_speed = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    paddle2_speed = 0

        # Movimentação das raquetes
        paddle1_y += paddle1_speed
        paddle2_y += paddle2_speed

        # Impedir as raquetes de saírem da tela
        if paddle1_y < 0:
            paddle1_y = 0
        elif paddle1_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle1_y = SCREEN_HEIGHT - PADDLE_HEIGHT

        if paddle2_y < 0:
            paddle2_y = 0
        elif paddle2_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle2_y = SCREEN_HEIGHT - PADDLE_HEIGHT

        # Movimentação da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisão da bola com o topo e o fundo
        if ball_y - BALL_SIZE // 2 <= 0 or ball_y + BALL_SIZE // 2 >= SCREEN_HEIGHT:
            ball_speed_y *= -1

        # Colisão da bola com as raquetes
        if ball_x - BALL_SIZE // 2 <= paddle1_x + PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
            ball_speed_x *= -1
        if ball_x + BALL_SIZE // 2 >= paddle2_x and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
            ball_speed_x *= -1

        # IA para controlar a raquete 2
        if ball_y < paddle2_y + PADDLE_HEIGHT // 2:
            paddle2_speed = -difficulty
        elif ball_y > paddle2_y + PADDLE_HEIGHT // 2:
            paddle2_speed = difficulty
        else:
            paddle2_speed = 0

        # Pontuação
        if ball_x - BALL_SIZE // 2 <= 0:
            player2_score += 1
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))
        elif ball_x + BALL_SIZE // 2 >= SCREEN_WIDTH:
            player1_score += 1
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))

        # Preenchendo a tela com fundo preto
        screen.fill(BLACK)

        # Desenhando as raquetes e a bola
        draw_paddle(paddle1_x, paddle1_y)
        draw_paddle(paddle2_x, paddle2_y)
        draw_ball(ball_x, ball_y)

        # Desenhando o placar
        draw_score(player1_score, player2_score)

        # Atualizando a tela
        pygame.display.flip()

        # Controlando os quadros por segundo (FPS)
        clock.tick(60)

# Iniciando o jogo
game()

# Finalizando o Pygame
pygame.quit()
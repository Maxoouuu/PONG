
import pygame

# Initialiser Pygame
pygame.init()

# Créer la fenêtre de jeu
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))

# Titer la fenêtre de jeu
pygame.display.set_caption("Pong")

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définir les dimensions de la balle et de la raquette
ball_radius = 10
paddle_width = 20
paddle_height = 100

# Définir les positions initiales de la balle et des raquettes
ball_x = (window_width - ball_radius) // 2
ball_y = (window_height - ball_radius) // 2
paddle1_x = 10
paddle1_y = (window_height - paddle_height) // 2
paddle2_x = window_width - paddle_width - 10
paddle2_y = (window_height - paddle_height) // 2

# Définir la vitesse de déplacement de la balle et des raquettes
ball_speed_x = 3
ball_speed_y = 3
paddle_speed = 5

# Définir les scores des joueurs
score1 = 0
score2 = 0

# Boucle principale du jeu
running = True
while running:
    # Obtenir les événements de la file d'attente d'événements
    events = pygame.event.get()

    # Parcourir les événements et réagir en conséquence
    for event in events:
        # Si l'utilisateur clique sur le bouton de fermeture de la fenêtre, arrêter le jeu
        if event.type == pygame.QUIT:
            running = False
            
    # Empêcher les raquettes de sortir de l'écran
    if paddle1_y < 0:
        paddle1_y = 0
    if paddle1_y > window_height - paddle_height:
        paddle1_y = window_height - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > window_height - paddle_height:
        paddle2_y = window_height - paddle_height

    # Mettre à jour la position de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Gérer la collision de la balle avec les raquettes
    if ball_y < 0 or ball_y > window_height - ball_radius:
        ball_speed_y *= -1
    if ball_x < 0 or ball_x > window_width - ball_radius:
        ball_speed_x *= -1

    # Gérer les mouvements de la raquette 1 avec les touches Z et S
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_z]:
        paddle1_y -= paddle_speed
    if keys_pressed[pygame.K_s]:
        paddle1_y += paddle_speed

    # Gérer les mouvements de la raquette 2 avec les touches fléchées haut et bas
    if keys_pressed[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys_pressed[pygame.K_DOWN]:
        paddle2_y += paddle_speed

    # Gérer la collision de la balle avec les raquettes
    if ball_x < paddle1_x + paddle_width and ball_y > paddle1_y and ball_y < paddle1_y + paddle_height:
        ball_speed_x *= -1
    if ball_x > paddle2_x - paddle_width and ball_y > paddle2_y and ball_y < paddle2_y + paddle_height:
        ball_speed_x *= -1


    # Remplir l'écran de jeu avec la couleur noire
    game_window.fill(BLACK)

    # Dessiner la balle
    pygame.draw.circle(game_window, WHITE, (ball_x, ball_y), ball_radius)

    # Dessiner les raquettes
    pygame.draw.rect(game_window, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(game_window, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Mettre à jour l'écran de jeu
    pygame.display.flip()

    # Définir le nombre d'images par seconde
    pygame.time.Clock().tick(60)

    # Si un des joueurs a atteint 10 points, arrêter le jeu
    if score1 == 10 or score2 == 10:
        running = False    

    # Accélérer la balle à chaque touché de raquette gauche ou droite
    if ball_x < paddle1_x + paddle_width and ball_y > paddle1_y and ball_y < paddle1_y + paddle_height:
        ball_speed_x += 2
    if ball_x > paddle2_x - paddle_width and ball_y > paddle2_y and ball_y > paddle2_y + paddle_height:
        ball_speed_x += 2

    # Ball speed limit
    if ball_speed_x > 10:
        ball_speed_x = 10
    if ball_speed_y > 10:
        ball_speed_y = 10
        
    
    
    # Gérer les scores des joueurs
    if ball_x < 0:
        score2 += 1
    if ball_x > window_width - ball_radius:
        score1 += 1

    # Afficher les scores des joueurs à chaque fois que la balle touche le bord gauche ou droit de l'écran
    if ball_x < 0 or ball_x > window_width - ball_radius:
        print(score1, " - ", score2)


# Quitter Pygame
pygame.quit()

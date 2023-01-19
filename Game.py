import pygame

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Breaking Game")

# Load assets
ball_image = pygame.image.load("ball.png")
paddle_image = pygame.image.load("paddle.png")
brick_image = pygame.image.load("brick.png")

# Create ball, paddle, and bricks
ball = pygame.Rect(400, 500, 20, 20)
paddle = pygame.Rect(350, 550, 100, 20)
bricks = [pygame.Rect(i*70, 50, 60, 20) for i in range(10)]

# Initialize ball movement variables
ball_speed_x = 5
ball_speed_y = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle with the mouse
    paddle.x = pygame.mouse.get_pos()[0]

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for ball collision with walls
    if ball.left < 0 or ball.right > 800:
        ball_speed_x = -ball_speed_x
    if ball.top < 0:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # Check for ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw assets
    screen.blit(ball_image, ball)
    screen.blit(paddle_image, paddle)
    for brick in bricks:
        screen.blit(brick_image, brick)

    # Update display
    pygame.display.update()

# Clean up
pygame.quit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

class pawn:
    size = (SQUARE_SIZE, SQUARE_SIZE)  # Square size for chessboard
    image = pygame.image.load('pawn.png')
    image = pygame.transform.scale(image, size)
    pawn_x = 0
    pawn_y = 0
    moveStraight = 1
    moveSide = 0
    moveTilt = 0
    moveWeird = 0
# Load chess piece images (you can replace these with your own)
p1 = pawn()
p2 = pawn()
p3 = pawn()
p4 = pawn()
p5 = pawn()
p6 = pawn()
p7 = pawn()
p8 = pawn()
pawns = [p1, p2, p3, p4, p5, p6, p7, p8]


rook_image = pygame.image.load('rook.png')
# Load other piece images...

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get current mouse position and state of mouse buttons
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    # Function for Drawing the chessboard
    def chessBoard(start):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = WHITE if (row + col) % 2 == 0 else GRAY
                field[row][col] = pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if row == 1:
                    if start == 1:
                        pawns[col].pawn_x = row
                        pawns[col].pawn_y = col
                    screen.blit(pawns[pawns[col].pawn_x].image, (col * SQUARE_SIZE, row * SQUARE_SIZE))  # Place pawns on the second row

    chessBoard(1)

    if mouse_pressed[0]:
        pawns[0].pawn_x = mouse_x - SQUARE_SIZE // 2
        pawns[0].pawn_y = mouse_y - SQUARE_SIZE // 2
        print("x = ", pawns[0].pawn_x)
        print("y = ", pawns[0].pawn_y)
        screen.blit(pawns[0].image, (pawns[0].pawn_x * SQUARE_SIZE, pawns[0].pawn_y * SQUARE_SIZE))  # Place newpawn

    
    # Draw the chess pieces
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

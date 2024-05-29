from ssl import Options
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
OPTIONBLUE = (22, 170, 219)

# Load images
pawn_image = pygame.image.load('pawn.png')  # Pfad zu deinem Bauernbild
pawn_image = pygame.transform.scale(pawn_image, (SQUARE_SIZE, SQUARE_SIZE))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

# Initialize the Board
board = []

def initialize_board():
    for row in range(BOARD_SIZE):
        board_row = []
        for col in range(BOARD_SIZE): 
            square = {
                'color': WHITE if (row + col) % 2 == 0 else GRAY,
                'piece': None, # Save the Chesspiece here
                'position': (col,row) 
            }
            board_row.append(square)
        board.append(board_row)


# Function for Drawing the chessboard
def drawBoard():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            square = board[row][col]
            color = square['color']
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if square['pieces'] == 1:
                screen.blit(pawn_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            



# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get current mouse position and state of mouse buttons
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    if mouse_pressed[0]:
        pass

    # Draw the chess pieces
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

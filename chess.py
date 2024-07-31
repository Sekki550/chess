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
# !!!   todo auf chess.com gehen und pieces klauen  !!!
pawn_image = pygame.image.load('pawn.png')  # Pfad zu deinem Bauernbild
pawn_image = pygame.transform.scale(pawn_image, (SQUARE_SIZE, SQUARE_SIZE))

rook_image = pygame.image.load('rook.png')  # Pfad zu deinem Turmbild
rook_image = pygame.transform.scale(rook_image, (SQUARE_SIZE, SQUARE_SIZE))

knight_image = pygame.image.load('knight.png')  # Pfad zu deinem Turmbild
knight_image = pygame.transform.scale(knight_image, (SQUARE_SIZE, SQUARE_SIZE))

bishop_image = pygame.image.load('bishop.png')  # Pfad zu deinem Turmbild
bishop_image = pygame.transform.scale(bishop_image, (SQUARE_SIZE, SQUARE_SIZE))

queen_image = pygame.image.load('queen.png')  # Pfad zu deinem Turmbild
queen_image = pygame.transform.scale(queen_image, (SQUARE_SIZE, SQUARE_SIZE))

king_image = pygame.image.load('king.png')  # Pfad zu deinem Turmbild
king_image = pygame.transform.scale(king_image, (SQUARE_SIZE, SQUARE_SIZE))


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')


# Initialize the Board
board = []

def initialize_board():
    for row in range(BOARD_SIZE):
        board_row = []
        for col in range(BOARD_SIZE): 
            piece = None
            if row == 1:
                piece = 1
            elif col == 0 and row == 0 or col == 7 and row == 0:
                piece = 2
            elif col == 1 and row == 0 or col == 6 and row == 0:
                piece = 3
            elif col == 2 and row == 0 or col == 5 and row == 0:
                piece = 4
            elif col == 3 and row == 0 :
                piece = 5
            elif col == 4 and row == 0 :
                piece = 6

            square = {
                'color': WHITE if (row + col) % 2 == 0 else GRAY,
                'position': (col,row), 
                'piece':  piece 
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
            if square['piece'] == 1:
                screen.blit(pawn_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif square['piece'] == 2:
                screen.blit(rook_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif square['piece'] == 3:
                screen.blit(knight_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif square['piece'] == 4:
                screen.blit(bishop_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif square['piece'] == 5:
                screen.blit(queen_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif square['piece'] == 6:
                screen.blit(king_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))


initialize_board()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    drawBoard()
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

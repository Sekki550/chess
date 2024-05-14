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

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

class pawn:
    size = (SQUARE_SIZE, SQUARE_SIZE)  # Square size for chessboard
    image = pygame.image.load('pawn.png')
    image = pygame.transform.scale(image, size)
    x = 0
    y = 0
    moveStraight = 1
    moveSide = 0
    moveTilt = 0
    moveWeird = 0

    def showMoveOption(self):
        option_x = self.x
        option_y = self.y + 1
        pygame.draw.rect(screen, OPTIONBLUE, (option_x * SQUARE_SIZE, option_y * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
        options = {option_x, option_y}
        return options 

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

# Function for Drawing the chessboard
def chessBoard(start):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if row == 1:
                if start == 1:
                    pawns[col].x = col
                    pawns[col].y = row
                screen.blit(pawns[pawns[col].x].image, (col * SQUARE_SIZE, row * SQUARE_SIZE))  # Place pawns on the second row
                print("Pawn" + str(col) + " x: " + str(pawns[col].x))
                print("Pawn" + str(col) + " y: " + str(pawns[col].y))
            
chessBoard(1)

# Function for checking if there is a chesspeace on given location
def checkPeace(x,y):
    chessBoard(0)
    for i in range(len(pawns)):
        if pawns[i].x == x and pawns[i].y == y:
           options = pawns[i].showMoveOption()
        return options



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
        options = checkPeace(mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE)
        if (mouse_x // SQUARE_SIZE) == options[0] and (mouse_y // SQUARE_SIZE) == options[1]:
            print ("asd")
        #pawns[0].x = mouse_x // SQUARE_SIZE 
        #pawns[0].y = mouse_y // SQUARE_SIZE  
        #print("---------------------------")
        #print("x = ", pawns[0].x)
        #print("y = ", pawns[0].y)
        #print("---------------------------")
        #screen.blit(pawns[0].image, (pawns[0].x * SQUARE_SIZE, pawns[0].y * SQUARE_SIZE))  # Place newpawn


    
    # Draw the chess pieces
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

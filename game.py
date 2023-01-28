import pygame
import os
import time
import chess

pygame.init()
clock = pygame.time.Clock()

width = 750
height = 750
color = "w"
turn = "w"
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
board_img = pygame.transform.scale(pygame.image.load(os.path.join("chessPieces", "board.png")), (750, 750))
chessbg = pygame.image.load(os.path.join("chessPieces", "bg.png"))

rect = (16, 16, 555, 555)

b = chess.Board(8, 8)

def click(pos):
    x=pos[0]
    y=pos[1]
    if (rect[0]<x<height):
        if rect[1]<y<width:
            div_x=x-rect[0]/2
            div_y=y-rect[1]/2
            i=int(div_y/(rect[2]/6))
            j=int(div_x/(rect[3]/6))
            return i, j
    return -1, -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            '''
            1. Get the formulae to convert the board coordinates into pixel coordinates ✅
            2. Print the circles for the valid moves for the piece that you click on ✅
            3. Make sure that "moves" isn't NoneType so we can iterate it ✅
            4. Some of the positions are "0" instead of the actual piece types ✅
            5. Prevent the program from crashing when you click on a "0" ✅
            6. Change the move method
            7. Work on valid_moves overload
            8. Making use of the selected boolean (make the circle disappear when you click on 
            another piece)
            9. Import the AI

            Order: 3, 1, 2
            '''
            i, j=click(pygame.mouse.get_pos())
            print(b.board[i][j])  #Testing if the position is filled with an actual piece
            if b.board[i][j] != 0:
                p = b.board[i][j]
                moves = p.valid_moves(b.board)
                print((moves))
                if moves != None:
                    x_offset=45
                    y_offset=140
                    for z in moves: #For loop for the formulae and to print the pixel coordinates
                        x=(rect[2]/6)*j + 8 + x_offset #(4-z[0])+round(113+(z[0]*525/6))-42
                        y=(rect[2]/6)*i + 8 + y_offset#3+round(113+(z[1]*525/6))-138
                        print("pixel coordinates: (%d, %d)" %(x, y))
                        pygame.draw.circle(board_img, "#eb344c", (x, y), 28)
                    i , j = click(pygame.mouse.get_pos())
                    if (i, j) in moves:
                        b.move((p.row, p.column), (i, j), "w", win)
                
        
    win.blit(board_img, (0, 0))
    b.draw(win, color)
    pygame.display.update()
    clock.tick(30)
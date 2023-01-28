import time
import pygame
from pieces import Pawn
from pieces import Queen
from pieces import Rook
from pieces import King
from pieces import Knight
from pieces import Bishop

class Board:
    board_co=(113, 113, 525, 525)
    startx=board_co[0]
    starty=board_co[1]
    def __init__(self, row, col):
        self.last=None
        self.copy=True
        self.row=row
        self.col=col
        self.ready=False
        self.board=[[0 for x in range(8)]for y in range(row)]
        #white
        self.board[0][0]=Rook(0, 0, "w")
        self.board[0][1]=Knight(0, 1, "w")
        self.board[0][2]=Bishop(0, 2, "w")
        self.board[0][3]=King(0, 3, "w")
        self.board[0][4]=Queen(0, 4, "w")
        self.board[0][5]=Bishop(0, 5, "w")
        self.board[0][6]=Knight(0, 6, "w")
        self.board[0][7]=Rook(0, 7, "w")

        self.board[1][0]=Pawn(1, 0, "w")
        self.board[1][1]=Pawn(1, 1, "w")
        self.board[1][2]=Pawn(1, 2, "w")
        self.board[1][3]=Pawn(1, 3, "w")
        self.board[1][4]=Pawn(1, 4, "w")
        self.board[1][5]=Pawn(1, 5, "w")
        self.board[1][6]=Pawn(1, 6, "w")
        self.board[1][7]=Pawn(1, 7, "w")

        #black
        self.board[7][0]=Rook(7, 0, "b")
        self.board[7][1]=Knight(7, 1, "b")
        self.board[7][2]=Bishop(7, 2, "b")
        self.board[7][3]=King(7, 3, "b")
        self.board[7][4]=Queen(7, 4, "b")
        self.board[7][5]=Bishop(7, 5, "b")
        self.board[7][6]=Knight(7, 6, "b")
        self.board[7][7]=Rook(7, 7, "b")
        
        self.board[6][0]=Pawn(6, 0, "b")
        self.board[6][1]=Pawn(6, 1, "b")
        self.board[6][2]=Pawn(6, 2, "b")
        self.board[6][3]=Pawn(6, 3, "b")
        self.board[6][4]=Pawn(6, 4, "b")
        self.board[6][5]=Pawn(6, 5, "b")
        self.board[6][6]=Pawn(6, 6, "b")
        self.board[6][7]=Pawn(6, 7, "b")

        self.turn="w"
    def update_move(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)
    
    def move(self, start, end, color, win):
        
            self.update_move()
    
    def draw(self, win, color):
        if self.last and color==self.turn:
            y, x=self.last[0]
            y1, x1=self.last[1]

            xx=0
            yy=0
            pygame.draw.circle(win, (0, 0, 255), (xx, yy), 34, 4)
            xx=0
            yy=0
            pygame.draw.circle(win, (0, 0, 255), (xx, yy), 34, 4)
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j]!=0:
                    self.board[i][j].draw(win, color)
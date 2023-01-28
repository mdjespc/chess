import pygame
import os
path=os.path.join("chessPieces", "whitePieces")
wpawn=pygame.image.load(os.path.join(path, "pawn.png"))
wbishop=pygame.image.load(os.path.join(path, "bishop.png"))
wqueen=pygame.image.load(os.path.join(path, "queen.png"))
wking=pygame.image.load(os.path.join(path, "king.png"))
wrook=pygame.image.load(os.path.join(path, "rook.png"))
wknight=pygame.image.load(os.path.join(path, "knight.png"))

path=os.path.join("chessPieces", "blackPieces")
bpawn=pygame.image.load(os.path.join(path, "pawn1.png"))
bbishop=pygame.image.load(os.path.join(path, "bishop1.png"))
bqueen=pygame.image.load(os.path.join(path, "queen1.png"))
bking=pygame.image.load(os.path.join(path, "king1.png"))
brook=pygame.image.load(os.path.join(path, "rook1.png"))
bknight=pygame.image.load(os.path.join(path, "knight1.png"))

b=[bpawn, bbishop, bqueen, bking, brook, bknight]
B=[]
w=[wpawn, wbishop, wqueen, wking, wrook, wknight]
W=[]

for image in b:
    B.append(pygame.transform.scale(image, (70, 70)))
for image in w:
    W.append(pygame.transform.scale(image, (70, 70)))
class Piece:
    img=-1
    board_co=(16, 16, 555, 555)
    startx=board_co[0]
    starty=board_co[1]
    def __init__(self, row, column, color):
        self.row=row
        self.column=column
        self.color=color
        self.selected=False #USE it to know whether a piece is eligible to move
        self.move_list=[]
        self.king=False
        self.pawn=False
    def draw(self, win, color):
        if self.color=="w":
            draw_this=W[self.img]
        else:
            draw_this=B[self.img]
        #(4-column)+(113+(column*525/6))
        x=(4-self.column)+round(self.startx+(self.column*self.board_co[2]/6))
        y=3+round(self.starty+(self.row*self.board_co[3]/6))
        if self.selected and self.color==color:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 62, 62), 4)
        win.blit(draw_this, (x, y))
    def update_valid_moves(self, board):
        self.move_list=self.valid_moves(board)
class Pawn(Piece):
    img=0
    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.first=True
        self.pawn=True
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
        #valid moves for white
        if self.color=="w":
            if i>0:
                p=board[i-1][j]
                if p==0:
                    moves.append((j, i-1))
            if j<7:
                p=board[i-1][j+1]
                if p != 0:
                    if p.color != self.color:
                        moves.append((j+1, i-1))
            if j>0:
                p=board[i-1][j-1]
                if p != 0:
                    if p.color != self.color:
                        moves.append((j-1, i-1))
            if self.first:
                if i<6:
                    p=board[i+2][j]
                    if p==0:
                        if board[i+1][j]==0:
                            moves.append((j, i+2))
                    elif p.color != self.color:
                        moves.append((j, i+2))
        #valid moves for black
        else:
            pass
        return moves
class Bishop(Piece):
    img=1
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
class Queen(Piece):
    img=2
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
class King(Piece):
    img=3
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
class Rook(Piece):
    img=4
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
class Knight(Piece):
    img=5
    def valid_moves(self, board):
        i=self.row
        j=self.column
        moves=[]
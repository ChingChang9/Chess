'''
Name: Ching's Chess Game
Author: Ching Chang
Contact: chingtheprogrammer@icloud.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

#---------------------Imports---------------------#
import pygame, sys
from pygame.locals import *

#---------------------License Notice---------------------#
print("Ching's Chess Game, Copyright (C), 2018, Ching Chang")
print("This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.")
print("This is free software, and you are welcome to redistribute it under certain")
print("conditions; type `show c' for details. To show both, type 'show b'.")

while True:
    user = input("Type 'show w', 'show c' or 'show b' for more detals, otherwise pleae click return.")
    if user == "show w":
        with open("License Notice.md") as f:
            print("\n", f.read())
    elif user == "show c":
        with open("License.md") as f:
            print("\n", f.read())
    elif user == "show b":
        with open("License Notice.md") as f1:
            with open("License.md") as f2:
                print("\n", f1.read(), "\n", f2.read())
    else:
        break

#---------------------Initialize---------------------#
pygame.init()

display_width = 700
display_height = 750
width_ratio = display_width * (10/display_width)
height_ratio = display_height * (10/display_height)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ching's Chess Game")
clock = pygame.time.Clock()
fps = 30
thinking_time = 90
timer_active = "On"
music_active = True

#---------------------Colours---------------------#
white = (255, 255, 255)
yellow = (255, 255, 0)
grey = (160, 160, 160)
bright_yellow = (160, 160, 0)
magenta = (255, 0, 255)
red = (255, 0, 0)
bright_red = (160, 0, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)
bright_green = (0, 160, 0)
blue = (0, 0, 255)
bright_blue = (0, 0, 160)
black = (0, 0, 0)

#---------------------Loading Sounds---------------------#
pygame.mixer.music.load("sounds/kahoot.wav")
boi_sound = pygame.mixer.Sound("sounds/boi.wav")
oof_sound =  pygame.mixer.Sound("sounds/oof.wav")
queen_dead_sound = pygame.mixer.Sound("sounds/queen_dead.wav")
ohh_sound = pygame.mixer.Sound("sounds/ohh.wav")

#---------------------Loading Images---------------------#

#------Board------#
chessBoard = pygame.image.load("images/chessBoard.jpg")
chessBoard = pygame.transform.scale(chessBoard, (display_width, display_width))
boardX = 0
boardY = display_height - display_width
board_width = chessBoard.get_width()
board_height = chessBoard.get_height()

pieceSize = (int(board_width * (6/75)), int(board_height * (1/10)))

#------Black Pieces------#
blackRookImg1 = pygame.image.load("images/blackRook.png")
blackRookImg1 = pygame.transform.scale(blackRookImg1, pieceSize)
blackRookImg2 = pygame.image.load("images/blackRook.png")
blackRookImg2 = pygame.transform.scale(blackRookImg2, pieceSize)

blackKnightImg1 = pygame.image.load("images/blackKnight.png")
blackKnightImg1 = pygame.transform.scale(blackKnightImg1, pieceSize)
blackKnightImg2 = pygame.image.load("images/blackKnight.png")
blackKnightImg2 = pygame.transform.scale(blackKnightImg2, pieceSize)

blackBishopImg1 = pygame.image.load("images/blackBishop.png")
blackBishopImg1 = pygame.transform.scale(blackBishopImg1, pieceSize)
blackBishopImg2 = pygame.image.load("images/blackBishop.png")
blackBishopImg2 = pygame.transform.scale(blackBishopImg2, pieceSize)

blackQueenImg = pygame.image.load("images/blackQueen.png")
blackQueenImg = pygame.transform.scale(blackQueenImg, pieceSize)
blackKingImg = pygame.image.load("images/blackKing.png")
blackKingImg = pygame.transform.scale(blackKingImg, pieceSize)

blackPawnImg1 = pygame.image.load("images/blackPawn.png")
blackPawnImg1 = pygame.transform.scale(blackPawnImg1, pieceSize)
blackPawnImg2 = pygame.image.load("images/blackPawn.png")
blackPawnImg2 = pygame.transform.scale(blackPawnImg2, pieceSize)
blackPawnImg3 = pygame.image.load("images/blackPawn.png")
blackPawnImg3 = pygame.transform.scale(blackPawnImg3, pieceSize)
blackPawnImg4 = pygame.image.load("images/blackPawn.png")
blackPawnImg4 = pygame.transform.scale(blackPawnImg4, pieceSize)
blackPawnImg5 = pygame.image.load("images/blackPawn.png")
blackPawnImg5 = pygame.transform.scale(blackPawnImg5, pieceSize)
blackPawnImg6 = pygame.image.load("images/blackPawn.png")
blackPawnImg6 = pygame.transform.scale(blackPawnImg6, pieceSize)
blackPawnImg7 = pygame.image.load("images/blackPawn.png")
blackPawnImg7 = pygame.transform.scale(blackPawnImg7, pieceSize)
blackPawnImg8 = pygame.image.load("images/blackPawn.png")
blackPawnImg8 = pygame.transform.scale(blackPawnImg8, pieceSize)

#------White Pieces------#
whiteRookImg1 = pygame.image.load("images/whiteRook.png")
whiteRookImg1 = pygame.transform.scale(whiteRookImg1, pieceSize)
whiteRookImg2 = pygame.image.load("images/whiteRook.png")
whiteRookImg2 = pygame.transform.scale(whiteRookImg2, pieceSize)

whiteKnightImg1 = pygame.image.load("images/whiteKnight.png")
whiteKnightImg1 = pygame.transform.scale(whiteKnightImg1, pieceSize)
whiteKnightImg2 = pygame.image.load("images/whiteKnight.png")
whiteKnightImg2 = pygame.transform.scale(whiteKnightImg2, pieceSize)

whiteBishopImg1 = pygame.image.load("images/whiteBishop.png")
whiteBishopImg1 = pygame.transform.scale(whiteBishopImg1, pieceSize)
whiteBishopImg2 = pygame.image.load("images/whiteBishop.png")
whiteBishopImg2 = pygame.transform.scale(whiteBishopImg2, pieceSize)

whiteQueenImg = pygame.image.load("images/whiteQueen.png")
whiteQueenImg = pygame.transform.scale(whiteQueenImg, pieceSize)
whiteKingImg = pygame.image.load("images/whiteKing.png")
whiteKingImg = pygame.transform.scale(whiteKingImg, pieceSize)

whitePawnImg1 = pygame.image.load("images/whitePawn.png")
whitePawnImg1 = pygame.transform.scale(whitePawnImg1, pieceSize)
whitePawnImg2 = pygame.image.load("images/whitePawn.png")
whitePawnImg2 = pygame.transform.scale(whitePawnImg2, pieceSize)
whitePawnImg3 = pygame.image.load("images/whitePawn.png")
whitePawnImg3 = pygame.transform.scale(whitePawnImg3, pieceSize)
whitePawnImg4 = pygame.image.load("images/whitePawn.png")
whitePawnImg4 = pygame.transform.scale(whitePawnImg4, pieceSize)
whitePawnImg5 = pygame.image.load("images/whitePawn.png")
whitePawnImg5 = pygame.transform.scale(whitePawnImg5, pieceSize)
whitePawnImg6 = pygame.image.load("images/whitePawn.png")
whitePawnImg6 = pygame.transform.scale(whitePawnImg6, pieceSize)
whitePawnImg7 = pygame.image.load("images/whitePawn.png")
whitePawnImg7 = pygame.transform.scale(whitePawnImg7, pieceSize)
whitePawnImg8 = pygame.image.load("images/whitePawn.png")
whitePawnImg8 = pygame.transform.scale(whitePawnImg8, pieceSize)

#------Others------#
auraImg = pygame.image.load("images/aura.png")
auraImg = pygame.transform.scale(auraImg, pieceSize)

gameIconImg = pygame.image.load("images/gameIcon.png")
pygame.display.set_icon(gameIconImg)

speaker_on = pygame.image.load("images/speaker_on.png")
speaker_on = pygame.transform.scale(speaker_on, ((display_height - display_width - 10), (display_height - display_width - 10)))
speaker_off = pygame.image.load("images/speaker_off.png")
speaker_off = pygame.transform.scale(speaker_off, ((display_height - display_width - 10), (display_height - display_width - 10)))

#---------------------Position IDs---------------------#
posA = board_width * 3/40 + boardX
posB = posA + (11/100) * board_width * 1
posC = posA + (11/100) * board_width * 2
posD = posA + (11/100) * board_width * 3
posE = posA + (11/100) * board_width * 4
posF = posA + (11/100) * board_width * 5
posG = posA + (11/100) * board_width * 6
posH = posA + (11/100) * board_width * 7

pos8 = board_height * 7/100 + boardY
pos7 = pos8 + (13/119) * board_height * 1
pos6 = pos8 + (13/119) * board_height * 2
pos5 = pos8 + (13/119) * board_height * 3
pos4 = pos8 + (13/119) * board_height * 4
pos3 = pos8 + (13/119) * board_height * 5
pos2 = pos8 + (13/119) * board_height * 6
pos1 = pos8 + (13/119) * board_height * 7

#---------------------Assigning Positions---------------------#
blackRookImg1X = posA
blackRookImg1Y = pos8

blackKnightImg1X = posB
blackKnightImg1Y = pos8

blackBishopImg1X = posC
blackBishopImg1Y = pos8

blackQueenImgX = posD
blackQueenImgY = pos8

blackKingImgX = posE
blackKingImgY = pos8

blackBishopImg2X = posF
blackBishopImg2Y = pos8

blackKnightImg2X = posG
blackKnightImg2Y = pos8

blackRookImg2X = posH
blackRookImg2Y = pos8

blackPawnImg1X = posA
blackPawnImg1Y = pos7

blackPawnImg2X = posB
blackPawnImg2Y = pos7

blackPawnImg3X = posC
blackPawnImg3Y = pos7

blackPawnImg4X = posD
blackPawnImg4Y = pos7

blackPawnImg5X = posE
blackPawnImg5Y = pos7

blackPawnImg6X = posF
blackPawnImg6Y = pos7

blackPawnImg7X = posG
blackPawnImg7Y = pos7

blackPawnImg8X = posH
blackPawnImg8Y = pos7

whiteRookImg1X = posA
whiteRookImg1Y = pos1

whiteKnightImg1X = posB
whiteKnightImg1Y = pos1

whiteBishopImg1X = posC
whiteBishopImg1Y = pos1

whiteQueenImgX = posD
whiteQueenImgY = pos1

whiteKingImgX = posE
whiteKingImgY = pos1

whiteBishopImg2X = posF
whiteBishopImg2Y = pos1

whiteKnightImg2X = posG
whiteKnightImg2Y = pos1

whiteRookImg2X = posH
whiteRookImg2Y = pos1

whitePawnImg1X = posA
whitePawnImg1Y = pos2

whitePawnImg2X = posB
whitePawnImg2Y = pos2

whitePawnImg3X = posC
whitePawnImg3Y = pos2

whitePawnImg4X = posD
whitePawnImg4Y = pos2

whitePawnImg5X = posE
whitePawnImg5Y = pos2

whitePawnImg6X = posF
whitePawnImg6Y = pos2

whitePawnImg7X = posG
whitePawnImg7Y = pos2

whitePawnImg8X = posH
whitePawnImg8Y = pos2

auraImgX = board_width * 2
auraImgY = board_height * 2

#---------------------Reference Lists---------------------#
reference = [
blackRookImg1, blackRookImg1X, blackRookImg1Y,
blackKnightImg1, blackKnightImg1X, blackKnightImg1Y,
blackBishopImg1, blackBishopImg1X, blackBishopImg1Y,
blackQueenImg, blackQueenImgX, blackQueenImgY,
blackKingImg, blackKingImgX, blackKingImgY,
blackBishopImg2, blackBishopImg2X, blackBishopImg2Y,
blackKnightImg2, blackKnightImg2X, blackKnightImg2Y,
blackRookImg2, blackRookImg2X, blackRookImg2Y,
blackPawnImg1, blackPawnImg1X, blackPawnImg1Y,
blackPawnImg2, blackPawnImg2X, blackPawnImg2Y,
blackPawnImg3, blackPawnImg3X, blackPawnImg3Y,
blackPawnImg4, blackPawnImg4X, blackPawnImg4Y,
blackPawnImg5, blackPawnImg5X, blackPawnImg5Y,
blackPawnImg6, blackPawnImg6X, blackPawnImg6Y,
blackPawnImg7, blackPawnImg7X, blackPawnImg7Y,
blackPawnImg8, blackPawnImg8X, blackPawnImg8Y,
whiteRookImg1, whiteRookImg1X, whiteRookImg1Y,
whiteKnightImg1, whiteKnightImg1X, whiteKnightImg1Y,
whiteBishopImg1, whiteBishopImg1X, whiteBishopImg1Y,
whiteQueenImg, whiteQueenImgX, whiteQueenImgY,
whiteKingImg, whiteKingImgX, whiteKingImgY,
whiteBishopImg2, whiteBishopImg2X, whiteBishopImg2Y,
whiteKnightImg2, whiteKnightImg2X, whiteKnightImg2Y,
whiteRookImg2, whiteRookImg2X, whiteRookImg2Y,
whitePawnImg1, whitePawnImg1X, whitePawnImg1Y,
whitePawnImg2, whitePawnImg2X, whitePawnImg2Y,
whitePawnImg3, whitePawnImg3X, whitePawnImg3Y,
whitePawnImg4, whitePawnImg4X, whitePawnImg4Y,
whitePawnImg5, whitePawnImg5X, whitePawnImg5Y,
whitePawnImg6, whitePawnImg6X, whitePawnImg6Y,
whitePawnImg7, whitePawnImg7X, whitePawnImg7Y,
whitePawnImg8, whitePawnImg8X, whitePawnImg8Y,
auraImg, auraImgX, auraImgY
]

game_log = []

#---------------------Functions---------------------#
def assigning_values():
    global gameExit
    global deciding
    global lift
    global turn
    global takeBack
    global press
    global pieceX
    global pieceY
    global illegal_move
    global blackTime
    global whiteTime
    global referencePoints
    global game_log
    global blackCastle_Queen
    global blackCastle_King
    global whiteCastle_Queen
    global whiteCastle_King

    gameExit = False
    deciding = False
    lift = False
    turn = 1
    takeBack = True
    press = True
    pieceX = 0
    pieceY = 0
    illegal_move = True
    blackTime = thinking_time
    whiteTime = thinking_time
    blackCastle_Queen = True
    blackCastle_King = True
    whiteCastle_Queen = True
    whiteCastle_King = True

    reference[1] = blackRookImg1X
    reference[2] = blackRookImg1Y
    reference[4] = blackKnightImg1X
    reference[5] = blackKnightImg1Y
    reference[7] = blackBishopImg1X
    reference[8] = blackBishopImg1Y
    reference[10] = blackQueenImgX
    reference[11] = blackQueenImgY
    reference[13] = blackKingImgX
    reference[14] = blackKingImgY
    reference[16] = blackBishopImg2X
    reference[17] = blackBishopImg2Y
    reference[19] = blackKnightImg2X
    reference[20] = blackKnightImg2Y
    reference[22] = blackRookImg2X
    reference[23] = blackRookImg2Y
    reference[25] = blackPawnImg1X
    reference[26] = blackPawnImg1Y
    reference[28] = blackPawnImg2X
    reference[29] = blackPawnImg2Y
    reference[31] = blackPawnImg3X
    reference[32] = blackPawnImg3Y
    reference[34] = blackPawnImg4X
    reference[35] = blackPawnImg4Y
    reference[37] = blackPawnImg5X
    reference[38] = blackPawnImg5Y
    reference[40] = blackPawnImg6X
    reference[41] = blackPawnImg6Y
    reference[43] = blackPawnImg7X
    reference[44] = blackPawnImg7Y
    reference[46] = blackPawnImg8X
    reference[47] = blackPawnImg8Y
    reference[49] = whiteRookImg1X
    reference[50] = whiteRookImg1Y
    reference[52] = whiteKnightImg1X
    reference[53] = whiteKnightImg1Y
    reference[55] = whiteBishopImg1X
    reference[56] = whiteBishopImg1Y
    reference[58] = whiteQueenImgX
    reference[59] = whiteQueenImgY
    reference[61] = whiteKingImgX
    reference[62] = whiteKingImgY
    reference[64] = whiteBishopImg2X
    reference[65] = whiteBishopImg2Y
    reference[67] = whiteKnightImg2X
    reference[68] = whiteKnightImg2Y
    reference[70] = whiteRookImg2X
    reference[71] = whiteRookImg2Y
    reference[73] = whitePawnImg1X
    reference[74] = whitePawnImg1Y
    reference[76] = whitePawnImg2X
    reference[77] = whitePawnImg2Y
    reference[79] = whitePawnImg3X
    reference[80] = whitePawnImg3Y
    reference[82] = whitePawnImg4X
    reference[83] = whitePawnImg4Y
    reference[85] = whitePawnImg5X
    reference[86] = whitePawnImg5Y
    reference[88] = whitePawnImg6X
    reference[89] = whitePawnImg6Y
    reference[91] = whitePawnImg7X
    reference[92] = whitePawnImg7Y
    reference[94] = whitePawnImg8X
    reference[95] = whitePawnImg8Y
    reference[96] = auraImg
    reference[97] = auraImgX
    reference[98] = auraImgY

    referencePoints = {
        "A1": "white", "A2": "white", "A3": "empty", "A4": "empty", "A5": "empty", "A6": "empty", "A7": "black", "A8": "black",
        "B1": "white", "B2": "white", "B3": "empty", "B4": "empty", "B5": "empty", "B6": "empty", "B7": "black", "B8": "black",
        "C1": "white", "C2": "white", "C3": "empty", "C4": "empty", "C5": "empty", "C6": "empty", "C7": "black", "C8": "black",
        "D1": "white", "D2": "white", "D3": "empty", "D4": "empty", "D5": "empty", "D6": "empty", "D7": "black", "D8": "black",
        "E1": "white", "E2": "white", "E3": "empty", "E4": "empty", "E5": "empty", "E6": "empty", "E7": "black", "E8": "black",
        "F1": "white", "F2": "white", "F3": "empty", "F4": "empty", "F5": "empty", "F6": "empty", "F7": "black", "F8": "black",
        "G1": "white", "G2": "white", "G3": "empty", "G4": "empty", "G5": "empty", "G6": "empty", "G7": "black", "G8": "black",
        "H1": "white", "H2": "white", "H3": "empty", "H4": "empty", "H5": "empty", "H6": "empty", "H7": "black", "H8": "black"
    }

    game_log = []

    print("----------------------------------")

def message_display(text, size, colour, y = "centre", x = "centre"):
    font = pygame.font.SysFont(None, int(size))

    global text_width, text_height
    text_width, text_height = font.size(text)

    if y == "centre":
        y = (display_height/2)-(text_height/2)
    if x == "centre":
        x = (display_width/2)-(text_width/2)
    gameDisplay.blit(font.render(text, True, colour), (x,y))

def button(text, size, text_colour, button_colour, y = "centre", x = "centre"):

    #------Display the Text Before Displaying the Button to Get text_width and text_height------#
    message_display(text, size-(width_ratio*5), text_colour, y, x)

    global text_width, text_height
    if y == "centre":
        y = (display_height/2)-(text_height/2)
    if x == "centre":
        x = (display_width/2)-(text_width/2)

    pygame.draw.rect(gameDisplay, button_colour, [x-(width_ratio*2), y-(height_ratio*2), text_width+(width_ratio*5), text_height+(height_ratio*3)])

    #------Display the Message On Top Of the Button------#
    message_display(text, size-(width_ratio*5), text_colour, y, x)

def timer(player, seconds, x):

    #------Convert Seconds to Minutes and Seconds------#
    minutes = 0
    seconds = int(seconds)

    while seconds >= 60:
        seconds -= 60
        minutes += 1

    if seconds < 10:
        if seconds == 0:
            time = str(minutes) + ":00"
        else:
            time = str(minutes) + ":0" + str(seconds)
    else:
        time = str(minutes) + ":" + str(seconds)

    font = pygame.font.SysFont(None, int(width_ratio * 5))
    text = font.render(player + ": " + time, True, magenta)
    gameDisplay.blit(text, (width_ratio * x, height_ratio * 1.5))

def select_piece(start, end):

    #------Globalize Variables------#
    global mouseX
    global mouseY
    global piece
    global pieceX
    global pieceY
    global deciding
    global lift
    global oldSpot

    for item in range(start, end, 3):
        if reference[item].get_rect(topleft = (reference[item + 1], reference[item + 2])).collidepoint(mouseX, mouseY):
            deciding = True
            lift = True
            piece = item
            pieceX = item + 1
            pieceY = item + 2
            if reference[item + 1] == posA:
                oldSpot = 0
            elif reference[item + 1] == posB:
                oldSpot = 8
            elif reference[item + 1] == posC:
                oldSpot = 16
            elif reference[item + 1] == posD:
                oldSpot = 24
            elif reference[item + 1] == posE:
                oldSpot = 32
            elif reference[item + 1] == posF:
                oldSpot = 40
            elif reference[item + 1] == posG:
                oldSpot = 48
            else:
                oldSpot = 56
            if reference[item + 2] == pos2:
                oldSpot += 1
            elif reference[item + 2] == pos3:
                oldSpot += 2
            elif reference[item + 2] == pos4:
                oldSpot += 3
            elif reference[item + 2] == pos5:
                oldSpot += 4
            elif reference[item + 2] == pos6:
                oldSpot += 5
            elif reference[item + 2] == pos7:
                oldSpot += 6
            elif reference[item + 2] == pos8:
                oldSpot += 7

def rook_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    if "Rook" in pieceType:

        #----Vertical----#
        #--Up--#
        i = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 8:
            if referencePoints[get_column + str(i)] == player:
                break
            elif referencePoints[get_column + str(i)] == opponent:
                legal_moves.append(get_column + str(i))
                break
            else:
                legal_moves.append(get_column + str(i))
                i += 1

        #--Down--#
        i = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 1:
            if referencePoints[get_column + str(i)] == player:
                break
            elif referencePoints[get_column + str(i)] == opponent:
                legal_moves.append(get_column + str(i))
                break
            else:
                legal_moves.append(get_column + str(i))
                i -= 1

        #----Horizontal----#
        #--Right--#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 72:
            if referencePoints[chr(i) + get_row] == player:
                break
            elif referencePoints[chr(i) + get_row] == opponent:
                legal_moves.append(chr(i) + get_row)
                break
            else:
                legal_moves.append(chr(i) + get_row)
                i += 1

        #--Left--#
        i = ord(get_column) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 65:
            if referencePoints[chr(i) + get_row] == player:
                break
            elif referencePoints[chr(i) + get_row] == opponent:
                legal_moves.append(chr(i) + get_row)
                break
            else:
                legal_moves.append(chr(i) + get_row)
                i -= 1

        for moves in legal_moves:
            legal_takes.append(moves)

def bishop_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    if "Bishop" in pieceType:

        #----To Top Right----#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        j = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 72 and j <= 8:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i += 1
                j += 1

        #----To Bottom Right----#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        j = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i <= 72 and j >= 1:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i += 1
                j -= 1

        #----To Top Left----#
        i = ord(get_column) -1 #--Minus One So That It Won't Count the Current Spot--#
        j = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i >= 65 and j <= 8:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i -= 1
                j += 1

        #----To Bottom Left----#
        i = ord(get_column) - 1 #--Minus One So That It Won't Count the Current Spot--#
        j = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 65 and j >= 1:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i -= 1
                j -= 1

        for moves in legal_moves:
            legal_takes.append(moves)

def queen_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    if "Queen" in pieceType:

        #------Rook------#
        #----Vertical----#
        #--Up--#
        i = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 8:
            if referencePoints[get_column + str(i)] == player:
                break
            elif referencePoints[get_column + str(i)] == opponent:
                legal_moves.append(get_column + str(i))
                break
            else:
                legal_moves.append(get_column + str(i))
                i += 1

        #--Down--#
        i = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 1:
            if referencePoints[get_column + str(i)] == player:
                break
            elif referencePoints[get_column + str(i)] == opponent:
                legal_moves.append(get_column + str(i))
                break
            else:
                legal_moves.append(get_column + str(i))
                i -= 1

        #----Horizontal----#
        #--Right--#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 72:
            if referencePoints[chr(i) + get_row] == player:
                break
            elif referencePoints[chr(i) + get_row] == opponent:
                legal_moves.append(chr(i) + get_row)
                break
            else:
                legal_moves.append(chr(i) + get_row)
                i += 1

        #--Left--#
        i = ord(get_column) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 65:
            if referencePoints[chr(i) + get_row] == player:
                break
            elif referencePoints[chr(i) + get_row] == opponent:
                legal_moves.append(chr(i) + get_row)
                break
            else:
                legal_moves.append(chr(i) + get_row)
                i -= 1

        #------Bishop------#
        #----To Top Right----#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        j = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i <= 72 and j <= 8:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i += 1
                j += 1

        #----To Bottom Right----#
        i = ord(get_column) + 1 #--Add One So That It Won't Count the Current Spot--#
        j = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i <= 72 and j >= 1:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i += 1
                j -= 1

        #----To Top Left----#
        i = ord(get_column) -1 #--Minus One So That It Won't Count the Current Spot--#
        j = int(get_row) + 1 #--Add One So That It Won't Count the Current Spot--#
        while i >= 65 and j <= 8:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i -= 1
                j += 1

        #----To Bottom Left----#
        i = ord(get_column) - 1 #--Minus One So That It Won't Count the Current Spot--#
        j = int(get_row) - 1 #--Minus One So That It Won't Count the Current Spot--#
        while i >= 65 and j >= 1:
            if referencePoints[chr(i) + str(j)] == player:
                break
            elif referencePoints[chr(i) + str(j)] == opponent:
                legal_moves.append(chr(i) + str(j))
                break
            else:
                legal_moves.append(chr(i) + str(j))
                i -= 1
                j -= 1

        for moves in legal_moves:
            legal_takes.append(moves)

def knight_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    if "Knight" in pieceType:

        #----Make Sure The Characters are in Range A-H and 1-8----#
        if ord(get_column) + 2 <= 72 and int(get_row) + 1 <= 8:
            legal_moves.append(chr(ord(get_column)+2) + str(int(get_row)+1))
        if ord(get_column) + 2 <= 72 and int(get_row) - 1 >= 1:
            legal_moves.append(chr(ord(get_column)+2) + str(int(get_row)-1))
        if ord(get_column) + 1 <= 72 and int(get_row) + 2 <= 8:
            legal_moves.append(chr(ord(get_column)+1) + str(int(get_row)+2))
        if ord(get_column) + 1 <= 72 and int(get_row) - 2 >= 1:
            legal_moves.append(chr(ord(get_column)+1) + str(int(get_row)-2))
        if ord(get_column) - 1 >= 65 and int(get_row) + 2 <= 8:
            legal_moves.append(chr(ord(get_column)-1) + str(int(get_row)+2))
        if ord(get_column) - 1 >= 65 and int(get_row) - 2 >= 1:
            legal_moves.append(chr(ord(get_column)-1) + str(int(get_row)-2))
        if ord(get_column) - 2 >= 65 and int(get_row) + 1 <= 8:
            legal_moves.append(chr(ord(get_column)-2) + str(int(get_row)+1))
        if ord(get_column) - 2 >= 65 and int(get_row) - 1 >= 1:
            legal_moves.append(chr(ord(get_column)-2) + str(int(get_row)-1))

        for moves in legal_moves:
            legal_takes.append(moves)

def king_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    global blackCastle_Queen
    global blackCastle_King
    global whiteCastle_Queen
    global whiteCastle_King

    #------Regular Moves------#
    if "King" in pieceType:
        for i in range(-1, 2):
            for j in range(-1, 2):

                #----Make Sure The Characters are in Range A-H and 1-8----#
                if ord(get_column) + i >= 65 and ord(get_column) + i <= 72 and \
                   int(get_row) + j >= 1 and int(get_row) + j <= 8:
                    legal_moves.append(chr(ord(get_column)+i) + str(int(get_row)+j))
        for moves in legal_moves:
            legal_takes.append(moves)

    #------Castle------#
    if player == "black":
        if blackCastle_Queen == True:
            if referencePoints.get("B8") == "empty" and referencePoints.get("C8") == "empty" and referencePoints.get("D8") == "empty":
                legal_moves.append("C8")
        if blackCastle_King == True:
            if referencePoints.get("F8") == "empty" and referencePoints.get("G8") == "empty":
                legal_moves.append("G8")
    else:
        if whiteCastle_Queen == True:
            if referencePoints.get("B1") == "empty" and referencePoints.get("C1") == "empty" and referencePoints.get("D1") == "empty":
                legal_moves.append("C1")
        if whiteCastle_King == True:
            if referencePoints.get("F1") == "empty" and referencePoints.get("G1") == "empty":
                legal_moves.append("G1")

def pawn_moves(player, opponent, pieceType):

    global legal_moves
    global legal_takes
    global get_column
    global get_row

    if "Pawn" in pieceType:

        #----Black----#
        if player == "black":

            #--Moving Forward--#
            legal_moves.append(get_column + str(int(get_row)-1))
            if get_row == "7":
                legal_moves.append(get_column + str(int(get_row)-2))

            #--Taking Pieces--#
            if ord(get_column) + 1 <= 72 and int(get_row) -1 >= 1:
                legal_takes.append(chr(ord(get_column)+1) + str(int(get_row)-1))
            if ord(get_column) - 1 >= 65 and int(get_row) -1 >= 1:
                legal_takes.append(chr(ord(get_column)-1) + str(int(get_row)-1))

        #----White----#
        else:

            #--Moving Forward--#
            legal_moves.append(get_column + str(int(get_row)+1))
            if get_row == "2":
                legal_moves.append(get_column + str(int(get_row)+2))

            #--Taking Pieces--#
            if ord(get_column) + 1 <= 72 and int(get_row) -1 >= 1:
                legal_takes.append(chr(ord(get_column)+1) + str(int(get_row)+1))
            if ord(get_column) - 1 >= 65 and int(get_row) -1 >= 1:
                legal_takes.append(chr(ord(get_column)-1) + str(int(get_row)+1))

def start_menu():

    global timer_active
    global music_active

    intro = True
    press = True

    while intro == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                if event.key == pygame.K_t:
                    if timer_active == "On":
                        timer_active = "Off"
                    else:
                        timer_active = "On"
                if event.key == pygame.K_m:
                    if music_active == True:
                        music_active = False
                    else:
                        music_active = True
                if event.key == pygame.K_s:
                    shortcuts_menu()
            if event.type == pygame.MOUSEBUTTONUP:
                press = True

        #------Display------#
        gameDisplay.fill(bright_blue)

        #--message_display(text, size, colour, y = "centre", x = "centre")--#
        message_display("Welcome to Ching's Chess Game", width_ratio * 6, magenta, height_ratio * 20)

        #------Hover------#
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] >= width_ratio * 16 and mouse[0] <= width_ratio * 55 and mouse[1] >= height_ratio * 30 and mouse[1] <= height_ratio * 36.5:
            shortcuts_colour = grey
            if click[0] == 1:
                shortcuts_menu()
        else:
            shortcuts_colour = white

        if mouse[0] >= width_ratio * 13 and mouse[0] <= width_ratio * 31 and mouse[1] >= height_ratio * 43 and mouse[1] <= height_ratio * 51:
            enter_colour = bright_green
            if click[0] == 1:
                intro = False
        else:
            enter_colour = green

        if mouse[0] >= width_ratio * 43 and mouse[0] <= width_ratio * 57.5 and mouse[1] >= height_ratio * 43 and mouse[1] <= height_ratio * 51:
            exit_colour = bright_red
            if click[0] == 1:
                quit_game()
        else:
            exit_colour = red

        if mouse[0] >= width_ratio * 33 and mouse[0] <= width_ratio * 42 and mouse[1] >= height_ratio * 56 and mouse[1] <= height_ratio * 62:
            timer_colour = bright_yellow
            if click[0] == 1 and press == True:
                if timer_active == "On":
                    timer_active = "Off"
                    press = False
                else:
                    timer_active = "On"
                    press = False
        else:
            timer_colour = yellow

        if mouse[0] >= width_ratio * 60 and mouse[0] <= width_ratio * 64 and mouse[1] >= height_ratio * 1 and mouse[1] <= height_ratio * 4.5 and click[0] == 1 and press == True:
            if music_active == True:
                music_active = False
                press = False
            else:
                music_active = True
                press = False

        #--button(text, size, text_colour, button_colour, y = "centre", x = "centre")--#
        button("Keyboard Shortcuts", width_ratio * 10, shortcuts_colour, black, height_ratio * 32)
        button("Enter", width_ratio * 12, black, enter_colour, height_ratio * 45, width_ratio * 15)
        button("Exit", width_ratio * 12, black, exit_colour, height_ratio * 45, width_ratio * 45)

        message_display("Timer:", width_ratio * 4, black, height_ratio * 58, width_ratio * 22)
        button(timer_active, width_ratio * 9, black, timer_colour, height_ratio * 58, width_ratio * 35)

        #------Speaker------#
        if music_active == True:
            gameDisplay.blit(speaker_on, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(speaker_off, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(fps)

def pause_menu():

    global timer_active
    global music_active

    pause = True
    press = True

    #------Pause the Music------#
    music_active = False

    while pause == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.unpause()
                    pause = False
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                if event.key == pygame.K_t:
                    if timer_active == "On":
                        timer_active = "Off"
                    else:
                        timer_active = "On"
                if event.key == pygame.K_r:
                    assigning_values()
                    pause = False
                if event.key == pygame.K_m:
                    if music_active == True:
                        music_active = False
                    else:
                        music_active = True
                if event.key == pygame.K_s:
                    shortcuts_menu()
            if event.type == pygame.MOUSEBUTTONUP:
                press = True

        #------Display------#
        gameDisplay.fill(bright_blue)

        #--message_display(text, size, colour, y = "centre", x = "centre")--#
        message_display("Paused", width_ratio * 20, magenta, height_ratio * 20)

        #------Hover------#
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] >= width_ratio * 16 and mouse[0] <= width_ratio * 55 and mouse[1] >= height_ratio * 40 and mouse[1] <= height_ratio * 46.5:
            shortcuts_colour = grey
            if click[0] == 1:
                shortcuts_menu()
        else:
            shortcuts_colour = white

        if mouse[0] >= width_ratio * 8 and mouse[0] <= width_ratio * 34.5 and mouse[1] >= height_ratio * 53 and mouse[1] <= height_ratio * 61:
            enter_colour = bright_green
            if click[0] == 1:
                pygame.mixer.music.unpause()
                pause = False
        else:
            enter_colour = green

        if mouse[0] >= width_ratio * 48 and mouse[0] <= width_ratio * 62.5 and mouse[1] >= height_ratio * 53 and mouse[1] <= height_ratio * 61:
            exit_colour = bright_red
            if click[0] == 1:
                quit_game()
        else:
            exit_colour = red

        if mouse[0] >= width_ratio * 33 and mouse[0] <= width_ratio * 42 and mouse[1] >= height_ratio * 63 and mouse[1] <= height_ratio * 69:
            timer_colour = bright_yellow
            if click[0] == 1 and press == True:
                if timer_active == "On":
                    timer_active = "Off"
                    press = False
                else:
                    timer_active = "On"
                    press = False
        else:
            timer_colour = yellow

        if mouse[0] >= width_ratio * 24.5 and mouse[0] <= width_ratio * 46.5 and mouse[1] >= height_ratio * 8 and mouse[1] <= height_ratio * 16:
            restart_colour = grey
            if click[0] == 1:
                assigning_values()
                pause = False
        else:
            restart_colour = white

        if mouse[0] >= width_ratio * 60 and mouse[0] <= width_ratio * 64 and mouse[1] >= height_ratio * 1 and mouse[1] <= height_ratio * 4.5 and click[0] == 1 and press == True:
            if music_active == True:
                music_active = False
                press = False
            else:
                music_active = True
                press = False

        #--button(text, size, text_colour, button_colour, y = "centre", x = "centre")--#
        button("Keyboard Shortcuts", width_ratio * 10, shortcuts_colour, black, height_ratio * 42)
        button("Continue", width_ratio * 12, black, enter_colour, height_ratio * 55, width_ratio * 10)
        button("Exit", width_ratio * 12, black, exit_colour, height_ratio * 55, width_ratio * 50)

        message_display("Timer:", width_ratio * 4, black, height_ratio * 65, width_ratio * 22)
        button(timer_active, width_ratio * 9, black, timer_colour, height_ratio * 65, width_ratio * 35)

        button("Restart", width_ratio * 12, black, restart_colour, height_ratio * 10)

        #------Speaker------#
        if music_active == True:
            gameDisplay.blit(speaker_on, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(speaker_off, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(fps)

def shortcuts_menu():

    global timer_active
    global music_active

    shortcuts = True
    press = True

    while shortcuts == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    shortcuts = False
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                if event.key == pygame.K_t:
                    if timer_active == "On":
                        timer_active = "Off"
                    else:
                        timer_active = "On"
                if event.key == pygame.K_m:
                    if music_active == True:
                        music_active = False
                    else:
                        music_active = True

        #------Display------#
        gameDisplay.fill(bright_blue)

        #------Hover------#
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] >= width_ratio * 2 and mouse[0] <= width_ratio * 7.3 and mouse[1] >= height_ratio * 1 and mouse[1] <= height_ratio * 4:
            back_colour = bright_green
            if click[0] == 1:
                shortcuts = False
        else:
            back_colour = green

        if mouse[0] >= width_ratio * 60 and mouse[0] <= width_ratio * 64 and mouse[1] >= height_ratio * 1 and mouse[1] <= height_ratio * 4.5 and click[0] == 1 and press == True:
            if music_active == True:
                music_active = False
                press = False
            else:
                music_active = True
                press = False

        #--message_display(text, size, colour, y = "centre", x = "centre")--#
        message_display("Keyboard Shortcuts", width_ratio * 10, magenta, height_ratio * 5)

        message_display("General", width_ratio * 8, black, height_ratio * 14, width_ratio * 8)
        message_display("Pause:   p", width_ratio * 6, white, height_ratio * 20, width_ratio * 10)
        message_display("Mute:   m", width_ratio * 6, white, height_ratio * 25, width_ratio * 10)
        message_display("Take Back Move:   b", width_ratio * 6, white, height_ratio * 30, width_ratio * 10)
        message_display("Show shortcuts:    s", width_ratio * 6, white, height_ratio * 35, width_ratio * 10)
        message_display("Quit:   esc", width_ratio * 6, white, height_ratio * 40, width_ratio * 10)

        message_display("On Paused Screen", width_ratio * 8, black, height_ratio * 49, width_ratio * 8)
        message_display("Restart:    r", width_ratio * 6, white, height_ratio * 55, width_ratio * 10)
        message_display("Timer:    t", width_ratio * 6, white, height_ratio * 60, width_ratio * 10)
        message_display("Continue:    enter", width_ratio * 6, white, height_ratio * 65, width_ratio * 10)

        #--button(text, size, text_colour, button_colour, y = "centre", x = "centre")--#
        button("", width_ratio * 6, white, back_colour, height_ratio * 3, width_ratio * 4)
        message_display("Back", width_ratio * 3, white, height_ratio * 2, width_ratio * 2.2) #----Because the text is too small, we have to display a bigger text----#

        #------Speaker------#
        if music_active == True:
            gameDisplay.blit(speaker_on, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(speaker_off, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(fps)

def game_loop():

    #------Music------#
    #----The Value Stands For the Number of Times + 1 to Repeat the Music, -1 Means Infinite----#
    pygame.mixer.music.play(-1)

    #---------------------Variables---------------------#
    global gameExit
    global deciding
    global lift
    global turn
    global takeBack
    global press
    global pieceX
    global pieceY
    global illegal_move
    global blackTime
    global whiteTime
    global referencePoints

    global legal_moves
    global legal_takes
    global get_column
    global get_row
    global blackCastle_Queen
    global blackCastle_King
    global whiteCastle_Queen
    global whiteCastle_King

    global piece
    global mouseX
    global mouseY
    global oldSpot

    global winner
    global text_colour

    global music_active

    global game_log

    #---------------------Re-assigning Positions---------------------#
    assigning_values()

    #---------------------Main Loop---------------------#
    while not gameExit:

        #------Player------#
        if turn % 2 == 0:
            player = "black"
            opponent = "white"
        else:
            player = "white"
            opponent = "black"

        for event in pygame.event.get():

            #------Quiting------#
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                if event.key == pygame.K_p:
                    if music_active == True:
                        pause_menu()
                        music_active = True
                    else:
                        pause_menu()
                if event.key == pygame.K_m:
                    if music_active == True:
                        music_active = False
                    else:
                        music_active = True
                if event.key == pygame.K_s:
                    shortcuts_menu()
                if event.key == pygame.K_b:
                    if takeBack == True:

                        #----Make Sure the Previous Move is Finished----#
                        if reference[pieceX] == newXPos and reference[pieceY] == newYPos:

                            #----Undo the Move----#
                            reference[pieceX] -= differenceX
                            reference[pieceY] -= differenceY
                            newXPos -= differenceX
                            newYPos -= differenceY
                            turn -= 1
                            takeBack = False

                            #----Remark the Old Spots----#
                            referencePoints[oldPosID] = opponent

                            #----Unmark the New Spot----#
                            if action == " to ":
                                referencePoints[newPosID] = "empty"
                            elif action == " take ":
                                referencePoints[newPosID] = player

                            #----Remove the Last Move From Game Log----#
                            game_log = game_log[:-1]


            if event.type == pygame.MOUSEBUTTONUP:
                press = True

            #------Interactions------#
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos

                #----Speaker----#
                if mouseX >= width_ratio * 60 and mouseX <= width_ratio * 64 and mouseY >= height_ratio * 1 and mouseY <= height_ratio * 4.5 and press == True:
                    if music_active == True:
                        music_active = False
                        press = False
                    else:
                        music_active = True
                        press = False

                #------Lifting the Piece Up------#
                if deciding == False and lift == False:

                    try:
                        if reference[pieceX] == newXPos and reference[pieceY] == newYPos and illegal_move == False:

                            #------Black's Move------#
                            if player == "black":
                                select_piece(0, 46)

                            #------White's Move------#
                            else:
                                select_piece(48, 94)

                            #----Aura Effect----#
                            if deciding == True and lift == True:
                                reference[97] = reference[pieceX]
                                reference[98] = reference[pieceY]

                            #----Aura Effect----#
                            if deciding == True and lift == True:
                                reference[97] = reference[pieceX]
                                reference[98] = reference[pieceY]

                        elif illegal_move == True:

                            #------Black's Move------#
                            if player == "black":
                                select_piece(0, 46)

                            #------White's Move------#
                            else:
                                select_piece(48, 94)

                            #----Aura Effect----#
                            if deciding == True and lift == True:
                                reference[97] = reference[pieceX]
                                reference[98] = reference[pieceY]

                            #----Aura Effect----#
                            if deciding == True and lift == True:
                                reference[97] = reference[pieceX]
                                reference[98] = reference[pieceY]

                    except NameError:

                        #------Black's Move------#
                        if player == "black":
                            select_piece(0, 46)

                        #------White's Move------#
                        else:
                            select_piece(48, 94)

                        #----Aura Effect----#
                        if deciding == True and lift == True:
                            reference[97] = reference[pieceX]
                            reference[98] = reference[pieceY]

                #------Getting the Mouse Position and Placing the Piece------#
                else:

                    #----X Position----#
                    if mouseX <= posA:
                        deciding = 0
                        lift = False
                    elif mouseX <= posB:
                        newXPos = posA
                        newSpot = 0
                    elif mouseX <= posC:
                        newXPos = posB
                        newSpot = 8
                    elif mouseX <= posD:
                        newXPos = posC
                        newSpot = 16
                    elif mouseX <= posE:
                        newXPos = posD
                        newSpot = 24
                    elif mouseX <= posF:
                        newXPos = posE
                        newSpot = 32
                    elif mouseX <= posG:
                        newXPos = posF
                        newSpot = 40
                    elif mouseX <= posH:
                        newXPos = posG
                        newSpot = 48
                    elif mouseX <= board_width:
                        newXPos = posH
                        newSpot = 56
                    else:
                        deciding = 0
                        lift = False

                    #----Y Position----#
                    if mouseY >= pos1 + (13/119) * board_height:
                        deciding = 0
                        lift = False
                    elif mouseY >= pos1:
                        newYPos = pos1
                    elif mouseY >= pos2:
                        newYPos = pos2
                        newSpot += 1
                    elif mouseY >= pos3:
                        newYPos = pos3
                        newSpot += 2
                    elif mouseY >= pos4:
                        newYPos = pos4
                        newSpot += 3
                    elif mouseY >= pos5:
                        newYPos = pos5
                        newSpot += 4
                    elif mouseY >= pos6:
                        newYPos = pos6
                        newSpot += 5
                    elif mouseY >= pos7:
                        newYPos = pos7
                        newSpot += 6
                    elif mouseY >= pos8:
                        newYPos = pos8
                        newSpot += 7
                    else:
                        deciding = 0
                        lift = False

                    #------Moving the Piece------#
                    if deciding == 1 and lift == True:
                        oldPosID = list(referencePoints.keys())[oldSpot]
                        newPosID = list(referencePoints.keys())[newSpot]

                        #----Determining the Type Of Piece----#
                        if piece == 0 or piece == 21:
                            pieceType = "Black Rook "
                        elif piece == 3 or piece == 18:
                            pieceType = "Black Knight "
                        elif piece == 6 or piece == 15:
                            pieceType = "Black Bishop "
                        elif piece == 9:
                            pieceType = "Black Queen "
                        elif piece == 12:
                            pieceType = "Black King "
                        elif piece == 24 or piece == 27 or piece == 30 or piece == 33 or \
                             piece == 36 or piece == 39 or piece == 42 or piece == 45:
                            pieceType = "Black Pawn "

                        elif piece == 48 or piece == 69:
                            pieceType = "White Rook "
                        elif piece == 51 or piece == 66:
                            pieceType = "White Knight "
                        elif piece == 54 or piece == 63:
                            pieceType = "White Bishop "
                        elif piece == 57:
                            pieceType = "White Queen "
                        elif piece == 60:
                            pieceType = "White King"
                        elif piece == 72 or piece == 75 or piece == 78 or piece == 81 or \
                             piece == 84 or piece == 87 or piece == 90 or piece == 93:
                            pieceType = "White Pawn "

                        #------Get the Column and Row Seperately------#
                        get_column, get_row = tuple(oldPosID)

                        legal_moves = []
                        legal_takes = []

                        #------Set Legal Moves------#
                        #------Note: chr(65 to 72 are A to H)------#
                        #------Note: ord is the opposite of chr------#
                        rook_moves(player, opponent, pieceType)
                        knight_moves(player, opponent, pieceType)
                        bishop_moves(player, opponent, pieceType)
                        queen_moves(player, opponent, pieceType)
                        king_moves(player, opponent, pieceType)
                        pawn_moves(player, opponent, pieceType)

                        #----Moving the Piece----#
                        if referencePoints[newPosID] == "empty":

                            #----Check If It is a Legal Move----#
                            if newPosID in legal_moves:

                                illegal_move = False

                                differenceX = newXPos - reference[pieceX]
                                differenceY = newYPos - reference[pieceY]
                                deciding = 0
                                action = " to "

                                #--En Passant--#
                                if "Pawn" in pieceType and int(abs(differenceY)) == int(pos1 - pos3): #--Checks if Pawn Moves 2 Steps Forward--#
                                    enPassant = True
                                else:
                                    enPassant = False

                                #--Castle--#
                                if "King" in pieceType and oldPosID == "E8" and newPosID == "C8":
                                    reference[1] = posD
                                    referencePoints["A8"] = "empty"
                                    referencePoints["D8"] = player
                                    action = "Black Castle Queen Side"
                                elif "King" in pieceType and oldPosID == "E8" and newPosID == "G8":
                                    reference[22] = posF
                                    referencePoints["H8"] = "empty"
                                    referencePoints["F8"] = player
                                    action = "Black Castle King Side"
                                elif "King" in pieceType and oldPosID == "E1" and newPosID == "C1":
                                    reference[49] = posD
                                    referencePoints["A1"] = "empty"
                                    referencePoints["D1"] = player
                                    action = "White Castle Queen Side"
                                elif "King" in pieceType and oldPosID == "E1" and newPosID == "G1":
                                    reference[70] = posF
                                    referencePoints["H1"] = "empty"
                                    referencePoints["F1"] = player
                                    action = "White Castle King Side"

                                #--Play Sound--#
                                if player == "white":
                                    pygame.mixer.Sound.play(oof_sound)
                                else:
                                    pygame.mixer.Sound.play(boi_sound)

                            else:

                                illegal_move = True

                                differenceX = 0
                                differenceY = 0

                                #----Remove Aura----#
                                reference[97] = display_width * 2
                                reference[98] = display_height * 2
                                deciding = 0
                                lift = 0

                        elif opponent in referencePoints[newPosID]:

                            #----Check If It is a Legal Take----#
                            if newPosID in legal_takes:

                                illegal_move = False

                                differenceX = newXPos - reference[pieceX]
                                differenceY = newYPos - reference[pieceY]
                                deciding = 0
                                action = " take "

                                #--En Passant--#
                                enPassant = False

                                #--Play Sound--#
                                if player == "white":
                                    pygame.mixer.Sound.play(oof_sound)
                                else:
                                    pygame.mixer.Sound.play(boi_sound)

                            else:

                                illegal_move = True

                                differenceX = 0
                                differenceY = 0

                                #----Remove Aura----#
                                reference[97] = display_width * 2
                                reference[98] = display_height * 2
                                deciding = 0
                                lift = 0

                        else:

                            #----Set New Lifted Piece----#
                            select_piece(0, 94)

                            #----Aura Effect----#
                            reference[97] = reference[pieceX]
                            reference[98] = reference[pieceY]

                        #------Remove the Taken Spot------#
                        if deciding == 0 and lift == 1:
                            referencePoints[oldPosID] = "empty"

                            #----Check If Castle is Available----#
                            #--Haven't Been Moved--#
                            if piece == 12 or piece == 0:
                                blackCastle_Queen = False
                            if piece == 12 or piece == 21:
                                blackCastle_King = False
                            if piece == 60 or piece == 48:
                                whiteCastle_Queen = False
                            if piece == 60 or piece == 69:
                                whiteCastle_King = False

                            #--Haven't Been Taken--#
                            if reference[1] == display_width * 2:
                                blackCastle_Queen = False
                            if reference[22] == display_width * 2:
                                blackCastle_King = False
                            if reference[49] == display_width * 2:
                                whiteCastle_Queen = False
                            if reference[70] == display_width * 2:
                                whiteCastle_King = False

                            #----Logging the Move----#
                            if "Castle" in action:
                                game_log.append(action)
                            else:
                                game_log.append(pieceType + oldPosID + action + newPosID)

                            print(game_log[turn-1])

                    #------Mark the Taken Spot------#
                    if deciding == 0 and lift == True:

                        if enPassant == True:
                            referencePoints[newPosID] = player + " en passnt"
                        else:
                            referencePoints[newPosID] = player

                        #------When Everything Is Done------#
                        whiteTime = thinking_time
                        blackTime = thinking_time
                        lift = 0
                        turn += 1

                        #----Remove Aura----#
                        reference[97] = board_width * 2
                        reference[98] = board_height * 2

                        #----Allow Take Back----#
                        takeBack = True

        #------Animating the Movement------#
        if deciding == False and lift == False and takeBack == True:
            try:
                if int(reference[pieceX]) != int(newXPos):
                    reference[pieceX] += differenceX/(fps/2)
                elif reference[pieceX] != newXPos:
                    reference[pieceX] = newXPos #----Make Them EXACTLY Same as the Other----#
                if int(reference[pieceY]) != int(newYPos):
                    reference[pieceY] += differenceY/(fps/2)
                elif reference[pieceY] != newYPos:
                    reference[pieceY] = newYPos #----Make Them EXACTLY Same as the Other----#

                #----Move the Taken Piece Out Of the Screen----#
                for item in range(0, 94, 3):
                    if reference[item] != reference[piece] and reference[item + 1] == reference[pieceX] and reference[item + 2] == reference[pieceY]:
                        reference[item + 1] = display_width * 2
                        reference[item + 2] = display_height * 2

            except (NameError, TypeError):
                pass

        #------Placing Objects------#
        gameDisplay.fill(bright_blue)
        gameDisplay.blit(chessBoard, (boardX, boardY))
        for i in range(0, 97, 3):
            gameDisplay.blit(reference[i], (reference[i+1], reference[i+2]))

        #------Speaker------#
        if music_active == True:
            gameDisplay.blit(speaker_on, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(speaker_off, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.pause()

        #------Clock------#
        if timer_active == "On":
            try:
                #----Start the Time Only When the Animation is Finished----#
                if reference[pieceX] == newXPos and reference[pieceY] == newYPos and illegal_move == False or deciding == True:
                    if player == "black":
                        blackTime -= 1/fps
                    else:
                        whiteTime -= 1/fps
                elif illegal_move == True:
                    if player == "black":
                        blackTime -= 1/fps
                    else:
                        whiteTime -= 1/fps
            except NameError:
                if player == "black":
                    blackTime -= 1/fps
                else:
                    whiteTime -= 1/fps
            finally:
                timer("White", whiteTime, 5)
                timer("Black", blackTime, 30)

            #----Lose if Time Runs Out----#
            if blackTime <= 0:
                winner = "White"
                text_colour = white
                game_over()
            elif whiteTime <= 0:
                winner = "Black"
                text_colour = black
                game_over()
        else:

            #----message_display(text, size, colour, y = "centre", x = "centre")----#
            message_display("Timer Off", width_ratio * 5, magenta, height_ratio * 1.5)

        #------Update the Screen------#
        pygame.display.update()
        clock.tick(fps)

        #------Check If the Queen Is Dead------#
        if reference[10] == display_width * 2:
            pygame.mixer.Sound.play(queen_dead_sound)
            reference[10] = display_width * 3
        if reference[58] == display_width * 2:
            pygame.mixer.Sound.play(queen_dead_sound)
            reference[58] = display_width * 3

        #------Check If the King Is Dead------#
        if reference[13] == display_width * 2:
            winner = "White"
            text_colour = white
            game_over()
        elif reference[61] == display_width * 2:
            winner = "Black"
            text_colour = black
            game_over()

def game_over():

    pygame.mixer.Sound.play(ohh_sound)

    #------Globalize the Variables------#
    global gameExit
    global winner
    global text_colour

    press = True

    #------Pause the Music------#
    music_active = False

    while gameExit == False:

        #------Replay or Exit------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.MOUSEBUTTONUP:
                press = True

        #------Hover------#
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] >= width_ratio * 8 and mouse[0] <= width_ratio * 42 and mouse[1] >= height_ratio * 48 and mouse[1] <= height_ratio * 56.5:
            newGame_colour = bright_green
            if click[0] == 1:
                break #----Break and then use the game_loop() so that the game over screen don't show after the new game----#
        else:
            newGame_colour = green

        if mouse[0] >= width_ratio * 48 and mouse[0] <= width_ratio * 64 and mouse[1] >= height_ratio * 48 and mouse[1] <= height_ratio * 56.5:
            exit_colour = bright_red
            if click[0] == 1:
                gameExit = True
        else:
            exit_colour = red

        if mouse[0] >= width_ratio * 60 and mouse[0] <= width_ratio * 64 and mouse[1] >= height_ratio * 1 and mouse[1] <= height_ratio * 4.5 and click[0] == 1 and press == True:
            if music_active == True:
                music_active = False
                press = False
            else:
                music_active = True
                press = False

        #------Display the Texts and Buttons------#

        #----message_display(text, size, colour, y = "centre", x = "centre")----#
        #----button(text, size, text_colour, button_colour, y = "centre", x = "centre")----#
        message_display(winner + " Wins", width_ratio * 16, text_colour)
        button("New Game", width_ratio * 13, black, newGame_colour, height_ratio * 50, width_ratio * 10)
        button("Exit", width_ratio * 13, black, exit_colour, height_ratio * 50, width_ratio * 50)

        #------Speaker------#
        if music_active == True:
            gameDisplay.blit(speaker_on, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(speaker_off, ((width_ratio * 60), (height_ratio * 0.7)))
            pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(fps)

    game_loop()

def quit_game():
    pygame.quit()

    #------Save Game------#
    if len(game_log) > 0:
        save = input("Do you want to save the game? (y)es/(n)o")
        if save == "y":

            while True:
                file_name = input("Save as: ")
                try:
                    test = open("Game Log/" + file_name + ".txt", "r")
                    test.close()
                    print("File name already exist")
                    continue
                except FileNotFoundError:
                    gameLog = open("Game Log/" + file_name + ".txt", "w")
                    for moves in game_log:
                        gameLog.write(str(moves) + "\n")
                    gameLog.close()
                    break

    print("Exited")
    sys.exit()

#---------------------Execution---------------------#
start_menu()
game_loop()
quit_game()

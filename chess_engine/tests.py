from django.test import TestCase

# Create your tests here.

from chess_classes import ChessLogic, ChessBoard

''' Testing ground '''

import json
# import chess_ai
# import game

import rotemai.chess_ai as chess_ai
import rotemai.game as game


from chess_engine.chess_classes import ChessBoard, ChessPiece, ChessLogic

# from chess_classes import ChessLogic

a = ChessLogic.ChessGame(1)

# data = {"participants":{"white":{"1":1},"black":{"1":-1}},"game_options":{"winning_games":"1","name":"Machine11", "creator":1},"token":{"step":{"castle":{"white":["r1","r2"],"black":["r1","r2"]},"name":"waitCellSource","side":"white"}},"board":{"1":{"a":{"s":"w","r":"R","n":"r2"},"c":{"s":"w","r":"B","n":"b2"},"b":{"s":"w","r":"H","n":"h2"},"e":{"s":"w","r":"K","n":"k"},"d":{"s":"w","r":"Q","n":"q"},"g":{"s":"w","r":"H","n":"h1"},"f":{"s":"w","r":"B","n":"b1"},"h":{"s":"w","r":"R","n":"r1"}},"2":{"a":{"s":"w","r":"P","n":"p1"},"c":{"s":"w","r":"P","n":"p3"},"b":{"s":"w","r":"P","n":"p2"},"e":{"s":"w","r":"P","n":"p5"},"d":{"s":"w","r":"P","n":"p4"},"g":{"s":"w","r":"P","n":"p7"},"f":{"s":"w","r":"P","n":"p6"},"h":{"s":"w","r":"P","n":"p8"}},"3":{"a":"-","c":"-","b":"-","e":"-","d":"-","g":"-","f":"-","h":"-"},"4":{"a":"-","c":"-","b":"-","e":"-","d":"-","g":"-","f":"-","h":"-"},"5":{"a":"-","c":"-","b":"-","e":"-","d":"-","g":"-","f":"-","h":"-"},"6":{"a":"-","c":"-","b":"-","e":"-","d":"-","g":"-","f":"-","h":"-"},"7":{"a":{"s":"b","r":"P","n":"p1"},"c":{"s":"b","r":"P","n":"p3"},"b":{"s":"b","r":"P","n":"p2"},"e":{"s":"b","r":"P","n":"p5"},"d":{"s":"b","r":"P","n":"p4"},"g":{"s":"b","r":"P","n":"p7"},"f":{"s":"b","r":"P","n":"p6"},"h":{"s":"b","r":"P","n":"p8"}},"8":{"a":{"s":"b","r":"R","n":"r2"},"c":{"s":"b","r":"B","n":"b2"},"b":{"s":"b","r":"H","n":"h2"},"e":{"s":"b","r":"K","n":"k"},"d":{"s":"b","r":"Q","n":"q"},"g":{"s":"b","r":"H","n":"h1"},"f":{"s":"b","r":"B","n":"b1"},"h":{"s":"b","r":"R","n":"r1"}}}}
data = {"participants": {"white": {"1": 1}, "black": {"1": 1}},
        "game_options": {"winning_games": "1", "name": "Createting_New_Game_Default_options", "creator": 1}, "token": {
    "step": {"data": {"targetCell": {"column": "h", "line": "4"}, "sourceCell": {"column": "h", "line": "2"}},
             "castle": {"white": ["r1", "r2"], "black": ["r1", "r2"]}, "enpassant": {"y": 3, "x": 7},
             "name": "waitCellSource", "side": "black"}, "logs": {
      "001.": {"source": {"y": "2", "x": "h", "piece": {"s": "w", "r": "P", "n": "p8"}}, "official": "h2-h4",
               "side": "w", "target": {"y": "4", "x": "h", "piece": "-"}}}}, "board": {
    "1": {"a": {"s": "w", "r": "R", "n": "r2"}, "c": {"s": "w", "r": "B", "n": "b2"},
          "b": {"s": "w", "r": "H", "n": "h2"}, "e": {"s": "w", "r": "K", "n": "k"},
          "d": {"s": "w", "r": "Q", "n": "q"}, "g": {"s": "w", "r": "H", "n": "h1"},
          "f": {"s": "w", "r": "B", "n": "b1"}, "h": {"s": "w", "r": "R", "n": "r1"}},
    "2": {"a": {"s": "w", "r": "P", "n": "p1"}, "c": {"s": "w", "r": "P", "n": "p3"},
          "b": {"s": "w", "r": "P", "n": "p2"}, "e": {"s": "w", "r": "P", "n": "p5"},
          "d": {"s": "w", "r": "P", "n": "p4"}, "g": {"s": "w", "r": "P", "n": "p7"},
          "f": {"s": "w", "r": "P", "n": "p6"}, "h": "-"},
    "3": {"a": "-", "c": "-", "b": "-", "e": "-", "d": "-", "g": "-", "f": "-", "h": "-"},
    "4": {"a": "-", "c": "-", "b": "-", "e": "-", "d": "-", "g": "-", "f": "-", "h": {"s": "w", "r": "P", "n": "p8"}},
    "5": {"a": "-", "c": "-", "b": "-", "e": "-", "d": "-", "g": "-", "f": "-", "h": "-"},
    "6": {"a": "-", "c": "-", "b": "-", "e": "-", "d": "-", "g": "-", "f": "-", "h": "-"},
    "7": {"a": {"s": "b", "r": "P", "n": "p1"}, "c": {"s": "b", "r": "P", "n": "p3"},
          "b": {"s": "b", "r": "P", "n": "p2"}, "e": {"s": "b", "r": "P", "n": "p5"},
          "d": {"s": "b", "r": "P", "n": "p4"}, "g": {"s": "b", "r": "P", "n": "p7"},
          "f": {"s": "b", "r": "P", "n": "p6"}, "h": {"s": "b", "r": "P", "n": "p8"}},
    "8": {"a": {"s": "b", "r": "R", "n": "r2"}, "c": {"s": "b", "r": "B", "n": "b2"},
          "b": {"s": "b", "r": "H", "n": "h2"}, "e": {"s": "b", "r": "K", "n": "k"},
          "d": {"s": "b", "r": "Q", "n": "q"}, "g": {"s": "b", "r": "H", "n": "h1"},
          "f": {"s": "b", "r": "B", "n": "b1"}, "h": {"s": "b", "r": "R", "n": "r1"}}}}
fen = ''

board = data['board']
# FEN board position
for row in range(8, 0, -1):
  empty_cells = 0
  
  for c in range(97, 105):
    col = chr(c)
    cell = board[str(row)][col]
    if cell == '-':
      empty_cells += 1
    else:
      if empty_cells > 0:
        fen += str(empty_cells)
        empty_cells = 0  # reset empty cells
      pawn = cell["r"]
      # damn french!!!
      if pawn.lower() == 'h':
        pawn = 'n'
      
      fen += pawn.lower() if cell["s"] == 'b' else pawn.upper()
  
  # add number to fen string
  if empty_cells > 0:
    fen += str(empty_cells)
  if row > 1:
    fen += '/'

# fen - whos turn is it anyways
side = data['token']['step']['side']
fen += ' w ' if side == 'white' else ' b '

# I don't think this get any more junior than this

#  castling
bq = bk = wq = wk = ''
whiteCastle = data['token']['step']['castle']['white']
blackCastle = data['token']['step']['castle']['black']

if not whiteCastle == '-':  # not empty
  wq = 'Q' if whiteCastle[0] == 'r1' else ''
  wk = 'K' if whiteCastle[1] == 'r2' else ''

if not blackCastle == '-':  # not empty
  bq = 'q' if blackCastle[0] == 'r1' else ''
  bk = 'k' if blackCastle[1] == 'r2' else ''

castling = wk + wq + bk + bq

fen += '-' if castling == '' else castling

# enpassant (pawn jumps 2 cells)
# enpassant_data = self.game_data.get_data('token/step/enpassant')
enpassant = '-'

step = data['token']['step']
if 'enpassant' in step:  # Rotem TODO - this looks different in logic
  x = step['enpassant']['x']
  y = step['enpassant']['y']
  ycoords = y
  xcoords = int(x) + 97
  enpassant = chr(xcoords) + str(ycoords)
  print x, y, chr(xcoords), enpassant

fen += ' ' + enpassant + ' '

# Halfmove clock & Fullmove number:
# Halfmove clock: This is the number of halfmoves since the last capture or pawn advance. This is used to determine if a draw can be claimed under the fifty-move rule.
# Fullmove number: The number of the full move. It starts at 1, and is incremented after Black's move.
fen += '0 1'

# print 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# print fen

################### AI testing part #####################
# game = chess_ai.Game_Engine(fen) # don't need the game engine
g = game.Game(fen)
print 'g in game is: '
# if it's the damn FEN why need this instance???
print g
print 'rnbqkbnr/pppppppp/8/8/7P/8/PPPPPPP1/RNBQKBNR b KQkq h3 0 1'
print 'ai:'

ai = chess_ai.AI(g, 3)
print ai

# res = ai.ab_make_move(fen)
res = 'e7e6'
print " results from ai: "
print res

# step from
fromX = res[0]
fromY = res[1]
# step to
toX = res[2]
toY = res[3]

print fromX, fromY, toX, toY
# from e7 to e6

# I made plans and I can't neglect my friends so I"m going to pin point this part
# ROTEM TODO send results (res eg: e7e6) to ChessLogic functions (move again immidiatly) or via API
"""
ROTEM - move_piece_select_source - user / x / y
user admin x d y 2
ROTEM - move_piece_select_target - user / x / y
user admin x d y 4
"""

user = 'admin'
x = 'd'
y = 2

# ChessGame ??????????????????????????????????????????????????????????????

# aa = a.ChessGame(1)
# def move_piece_select_source(user, x, y):
# def move_piece_select_target( user, x, y):


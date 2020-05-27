import time
import shutil

from random import choice, randint
from itertools import product, filterfalse
from reprint import output

TERMINAL_WIDTH, TERMINAL_HEIGHT = shutil.get_terminal_size()
board = {}

for coord in product(range(TERMINAL_HEIGHT), range(TERMINAL_WIDTH)):
  board[(coord[0], coord[1])] = False

for i in range(randint(1, int((TERMINAL_WIDTH*TERMINAL_HEIGHT)/3))):
  random_coord = choice(list(board.keys()))
  board[random_coord] = True


def count_alive_neighbours(board, cell):
  count = 0
  cx, cy = cell[0], cell[1]
  coords = product([-1, 0, 1], repeat=2)
  coords = filterfalse(lambda x: x == (0,0), coords)
  neighbours = [ (lambda a: (a[0] + cx, a[1] + cy))(a) for a in coords ]

  for n in neighbours:
    if board.get(n) == True:
        count = count + 1

  return count


def next(board):
  new_board = board.copy()

  for cell in board:
    no_alive_neighbours = count_alive_neighbours(board, cell)

    if no_alive_neighbours == 3:
      new_board[cell] = True

    elif (no_alive_neighbours < 2) or (no_alive_neighbours > 3):
      new_board[cell] = False

  return new_board


with output(initial_len=TERMINAL_HEIGHT, interval=20) as output_list:
  while True in board.values():
    board = next(board)
    line = []

    for cell in board:
      if board[cell]:
        line.append('o')
      else:
        line.append(' ')

      if (cell[1]+1) == TERMINAL_WIDTH:
        output_list[cell[0]] = ''.join(line)
        line.clear()

    time.sleep(1)

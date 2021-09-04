from copy import deepcopy
from Square import *
import random

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)

NE = (-1, 1)
NW = (-1, -1)
SE = (1, 1)
SW = (1, -1)
COMPAS = (NW, N, NE, E, SE, S, SW, W)


class Board(object):
    COMPASS = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
##    DIR = [-9, -8, -7, 1, 9, 8, 7, -1]
    ROWS = [0, 1, 2, 3, 4, 5, 6, 7]
    COLS = [0, 1, 2, 3, 4, 5, 6, 7]
    values_list = []
    player = None

    def __init__(self, player = None):
        """
        :rtype: Board
        """
        Board.player = player
        self.board = [[Square(r, c)  for c in Board.COLS] for r in Board.ROWS]

        # you is 'X, 1' opponent is 'O, -1'
        self.board[3][3].set_status(1)
        self.board[4][4].set_status(1)
        self.board[3][4].set_status(-1)
        self.board[4][3].set_status(-1)

        self.move = None
        self.prevMove = None
        self.value = None
        self.prevValue = None

        self.frontier =[(2,2), (2,3), (2,4), (2,5), (3,2), (3,5), (4,2), (4,5), (5,2), (5,3), (5,4), (5,5)]
        self.explored = [(3,3), (3,4), (4,3), (4,4)]

        self.update_frontier_owner()
##        self.set_sqr_values()

        self.moves_list = [] #self.get_moves4player()

    def __str__(self):

##        moves_list = self.get_moves4player()
        symbol = 'X' if Board.player == 1 else 'O' if Board.player == -1 else ''

        brd_str = "\n"
##        brd_str += "Move " + str(self.move) + "  Value " + str(self.value) + "\n"
##        brd_str += "Previous Move " + str(self.prevMove) + " Previous Value " + str(self.prevValue) + "\n"
##        brd_str += "Frontier Moves " + str(self.frontier) + "\n"
##        brd_str += "Moves for Player " + str(Board.player) + ': ' + str(self.moves_list) + "\n"
##        brd_str += 'Player ' + symbol  + ' = ' + str(Board.player) + '\n'
        for i in Board.ROWS:
            for j in Board.COLS:
                brd_str = brd_str + str(self.board[i][j].owner_txt) + " "
            brd_str += "\n"
        brd_str += '****************'
        return brd_str

    def info(self):

##        moves_list = self.get_moves4player()
        symbol = 'X' if Board.player == 1 else 'O' if Board.player == -1 else ''

        brd_str = ""
##        brd_str += "Move " + str(self.move) + "  Value " + str(self.value) + "\n"
##        brd_str += "Previous Move " + str(self.prevMove) + " Previous Value " + str(self.prevValue) + "\n"
        brd_str += "Frontier Moves " + str(self.frontier) + "\n"
        brd_str += "Moves for Player " + symbol + ':' + str(Board.player) + ': ' + str(self.moves_list)

##        brd_str += 'Player ' + symbol  + ' = ' + str(Board.player) + '\n'
##        for i in range(Board.ROWS):
##            for j in Board.COLS:
##                brd_str = brd_str + str(self.board[i][j].owner_txt) + " "
##            brd_str += "\n"
##
        return brd_str


    def update_frontier_owner(self):
        for i,j in self.frontier: self.board[i][j].set_owner_txt('.')

    def add2frontier(self, _sqr):
        ''' _sqr is a (r, c) tuple
        '''
        if _sqr in self.frontier: self.frontier.remove(_sqr)

        for _dir in Board.COMPASS:
            r, c = self.moveto((_sqr , _dir))
            if (not self.off_board((r, c)) and self.board[r][c].empty and (r, c) not in self.frontier):
                self.frontier.append((r,c))
        self.update_frontier_owner()

    def empty(self, _sqr):
        r, c = _sqr
        return True if self.board[r][c].status == 0 else False

    def add2explored(self, _sqr):
        r, c = _sqr
        if _sqr not in self.explored:
            self.explored.append(_sqr)
        self.board[r][c].set_status(Board.player)

    def evaluate(self, _sqr):
        val = self.board[_sqr[0]][_sqr[1]].value
        for i,j in self.explored:
            if self.board[i][j].status == Board.player:
                val += 2
        return val

    def switch_player(self):
        Board.player = -1*Board.player

    def moveto(self, mov):
        ''' mov is a tuple of a (square, direction)'''
        _sqr, _dir = mov
        return(_sqr[0] + _dir[0], _sqr[1] + _dir[1])

##    def moveto(self, (_sqr, _dir)):
##        return(_sqr[0] + _dir[0], _sqr[1] + _dir[1])

    def flip_stones(self, mov):

        _sqr, _dir = mov
        r,c =self.moveto(mov)
        if self.off_board((r,c)): return

        lst =[]
        if self.board[r][c].get_status() == -Board.player:
            while self.board[r][c].get_status() == -Board.player:
                lst.append((r, c))

                r,c = self.moveto(((r,c) , _dir))
                if self.off_board((r,c)): return
        else:
            return

        if self.board[r][c].get_status() == Board.player:
            for r, c in lst:
                self.board[r][c].set_status(Board.player)

    def apply_move(self, mov):

        mov_lst = [m for m in self.moves_list if m[0]==mov[0]]
        print('sqr_dir = ', mov_lst)
        for mov in mov_lst:
            self.flip_stones(mov)

            self.prevValue = self.value
##        self.value = self.evaluate(mov)
            self.prevMove = self.move
            self.move = mov

            _sqr, _dir = mov
            r, c = _sqr
            self.board[r][c].set_status(Board.player)

            self.add2explored(_sqr)
            self.add2frontier(_sqr)


    def off_board(self, _sqr):
        ''' _sqr is an (row, col) tuple'''

        r,c = _sqr
        return True if r < 0 or r > 7 or c < 0 or c > 7 else False

    def is_move_legal(self, mov):
        '''
        Takes a move and a direction
        Returns true if move is legal
          '''
        sqr, _dir = mov
        player = Board.player

        r, c = sqr = self.moveto((sqr, _dir))
        if self.off_board(sqr) : return False

        if self.board[r][c].status == -player:
            while not self.off_board(sqr) and self.board[r][c].status == -player:
                r, c = sqr = self.moveto((sqr, _dir))
        else:
            return False
        if not self.off_board(sqr) and self.board[r][c].status == player:
            return True
        else:
            return False


    def is_move_legal1(self, mov):
        '''
        Takes a move and a direction
        Returns true if move is legal
          '''
        sqr, _dir = mov
        player = Board.player

        r, c = sqr = self.moveto((sqr, _dir))

        if self.off_board(sqr) : return False
        if self.board[r][c].empty: return False
        if self.board[r][c].status == player: return False

        rr, cc = sqno = self.moveto((sqr, _dir))

        if self.off_board(sqno): return False
        if self.board[r][c].empty: return False
        if self.board[rr][cc].status == player: return True

        self.is_move_legal((sqr, _dir))

    def get_moves4player1(self):
        self.moves_list = [(_sqr, _dir) for _sqr in self.frontier for _dir in Board.COMPASS if self.is_move_legal((_sqr, _dir))]
        return self.moves_list

    def get_moves4player(self):
        self.moves_list = []
        for _sqr in self.frontier:
            for _dir in Board.COMPASS:
                 if self.is_move_legal((_sqr, _dir)):
                    self.moves_list.append((_sqr, _dir))
        return self.moves_list

    def winner(self):
        p0, p1 = 0, 0
        for mov in self.explored:
            r, c = mov
            if self.board[r][c].status == Board.player:
                p1 += 1
            else:
                p0 += 1
        if p1 > p0: return 'P ' , p1 , ' > ' , p0
        if p1 < p0: return 'O ' , p1 , ' < ' , p0
        if p1 == p0: return 'N ' , p1 , ' = ' , p0

    def update_brd_data(self):

        self.add2frontier()
        self.add2explored()
        self.update_frontier_owner()

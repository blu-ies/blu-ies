from Board_2D import *
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gabi
#
# Created:     01/09/2021
# Copyright:   (c) gabi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    brd = Board(1)
    print(brd)
    lst_legal_moves = brd.get_moves4player()
    print(lst_legal_moves)
    mov = ((4,2),(0,1))
    brd.apply_move(mov)
    print(brd)



if __name__ == '__main__':
    main()

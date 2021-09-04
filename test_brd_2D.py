from Board_2D import *

#new_stati =
[
[ 0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  1,  0,  0, -1, -1, -1],
[ 0,  1,  1,  1, -1, -1, -1,  0],
[ 0,  0,  1,  1,  1,  1, -1, -1],
[ 0,  0,  1,  1,  1,  1,  1, -1],
[ 0,  1,  0,  1,  1, -1, -1, -1],
[ 0,  0,  1,  0, -1, -1,  0, -1],
[ 0,  0,  0, -1,  0,  1,  0,  0]
]
def main():
    brd = Board()
    print(brd)
    Board.player = 1
    print(brd.winner())
    ##brd_status = []
    ##for r in Board.ROWS:
    ##    for c in Board.COLS:
    ##        brd.board[r][c].set_status(new_stati[r][c])
    ##        brd_status.append( brd.board[r][c].set_status(new_stati[r][c]))
    p1=p2=0
    while brd.frontier:

        brd.moves_list = brd.get_moves4player()
        if  brd.moves_list:
            print(Board.player, brd.moves_list)
            mov = random.choice(brd.moves_list)
            brd.apply_move(mov)
            print(brd)
        p1 += 1
        print('p1=', p1,'p2=', p2, 'Player=' , Board.player)


        brd.switch_player()
        brd.moves_list = brd.get_moves4player()

        if brd.moves_list:
            print(Board.player, brd.moves_list)
            mov = random.choice(brd.moves_list)
            brd.apply_move(mov)
            print(brd)
        p2 += 1
        print('p1=', p1,'p2=', p2, 'Player=' , Board.player)
        brd.switch_player()
        if p1 > 31 or p2 > 31: break

    print(brd)
    print(brd.winner())

if __name__ == '__main__':
    main()

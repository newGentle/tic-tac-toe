n = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
win_indices = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2]]
X_ = []
O_ = []

def create_board(n):
    j = 0
    print(f'-------------')
    for i in range(3):
        print(f'| {n[i][j]} | {n[i][j + 1]} | {n[i][j + 2]} |\n'
              f'-------------')


create_board(n)

board_copy = n.copy()


def turn(a, player):
    for i in range(3):
        for j in range(3):
            if a == board_copy[i][j]:
                board_copy[i][j] = player

    win_check(board_copy)
    return board_copy

def win_check(brd_copy):
    chk = []
    for i in range(3):
        for j in range(3):
            if player == brd_copy[i][j]:
                print(brd_copy[i])
                chk.append(brd_copy[i][j])
                break


player = 'X'
while True:

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    a = int(input(': '))
    create_board(turn(a, player))

cells = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
win_indices = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['7', '4', '1'],
    ['8', '5', '2'],
    ['9', '6', '3'],
    ['7', '5', '3'],
    ['1', '5', '9']]
X_ = []
O_ = []
player = 'X'

def create_board(n):
    print(f'-------------')
    print(f'| {n[0]} | {n[1]} | {n[2]} |')
    print(f'-------------')
    print(f'| {n[3]} | {n[4]} | {n[5]} |')
    print(f'-------------')
    print(f'| {n[6]} | {n[7]} | {n[8]} |')
    print(f'-------------')


create_board(cells)

board_copy = cells.copy()


def turn(a, player):
    for i in range(0, 8):
        if str(a) == board_copy[i]:
            board_copy[i] = player

    win_check(board_copy)
    return board_copy

def win_check(brd_copy):
    chk = []
    for i in win_indices:
        if player == brd_copy[i]:
            print(brd_copy[i])
            chk.append(brd_copy[i])
            break


while True:
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    a = int(input(': '))
    create_board(turn(a, player))

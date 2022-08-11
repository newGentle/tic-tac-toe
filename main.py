# клетки по numpad
cells = ['7', '8', '9', '4', '5', '6', '1', '2', '3']

# комбинации выигрыша
win_indices = [
    ['6', '7', '8'],
    ['3', '4', '5'],
    ['0', '1', '2'],
    ['6', '3', '0'],
    ['7', '4', '1'],
    ['8', '5', '2'],
    ['6', '4', '2'],
    ['0', '4', '8']]

game = False  # новая игра не начато
play = True   # Играть снова
win = False   # выигрыш

# вступление
def intro():
    print('-' * 20)
    print('Игра крестики-нолики')
    print('-' * 20)
    print()
    player_one = input('Введите Имя первого игрока: ')
    player_two = input('Введите Имя второго игрока: ')
    players = {'X': player_one, 'O': player_two}
    return players

# создание игральной доски
def create_board(n):
    print(f'-------------')
    print(f'| {n[0]} | {n[1]} | {n[2]} |')
    print(f'-------------')
    print(f'| {n[3]} | {n[4]} | {n[5]} |')
    print(f'-------------')
    print(f'| {n[6]} | {n[7]} | {n[8]} |')
    print(f'-------------')

# ход игрока
def turn(a, player, turn_count):
    for i in range(0, 9):
        if str(a) == board_copy[i]:
            board_copy[i] = player
            break
    if turn_count >= 5:
        win_check(board_copy)
    return board_copy


# проверка на выигрышные комбинации
def win_check(brd_copy):
    for i in win_indices:
        if brd_copy[int(i[0])] == brd_copy[int(i[1])] == brd_copy[int(i[2])]:
            global win
            win = True
            break

# Основной цикл игры
while True:
    if not game:    # проверка новой игры
        if not play:    # проверка на желание играть заново
            break
        players = intro()   # получение имен игроков
        print(f'игрок {players.get("X")} играет за "Х"')
        print(f'игрок {players.get("O")} играет за "O"')
        create_board(cells)     # создание доски
        board_copy = cells.copy()   # копирование доски
        entered_number = 0  # введенные числа
        turn_check = []     # список ходов для проверки на повторение
        game = True         # игра начата
        player = 'X'        # первый ход первого игрока
        turn_count = 1      # счетчик ходов

    # проверка на заполнение доски
    if turn_count == 10:
        print('больше нет ходов')
        play_again = input('Хотите начать заново ? (y/n): ')
        play = True if play_again == 'y' else False
        game = False
        continue

    entered_number = input(f'ход {players.get(player)}: ')

    if not entered_number:  # ошибочно нажата кнопка enter
        continue
    elif not entered_number.isdigit():
        continue
    elif int(entered_number) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:        # проверка на ошибочный ввод
        continue
    elif int(entered_number) in turn_check:
        print(f'{entered_number} ход уже был\nвыберите другой ход')
        create_board(board_copy)
        continue
    else:   
        turn_check.append(int(entered_number))  
        create_board(turn(int(entered_number), player, turn_count))

    if win:
        print()
        print(f'Игрок {players.get(player)} победил !!!')
        print()
        play_again = input('Хотите начать заново ? (y/n): ')
        play = True if play_again == 'y' else False
        game = False
        win = False

    turn_count += 1
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

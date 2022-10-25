# Создайте программу для игры в "Крестики-нолики".

def game():
    turn_count, win = 0, False
    game_board = list(range(1, 10))
    while not win:
        draw_game_table(game_board)
        if turn_count % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        player_turn(player, game_board)
        win = win_condition(game_board)
        if win:
            return print(f'{player} win')
        turn_count += 1
        if turn_count == 9:
            return print('nobody win')
    return


def draw_game_table(game_board):
    print('-' * 13)
    for i in range(3):
        print('|', game_board[0 + i * 3], '|', game_board[1 + i * 3], '|', game_board[2 + i * 3], '|')
        print('-' * 13)


def player_turn(player_side, game_board):
    input_check = False
    while not input_check:
        player_input = input(f'Enter cell number for placing {player_side}: ')
        try:
            player_input = int(player_input)
        except:
            print('Wrong input, try again: ')
            continue
        if player_input in range(1, 10):
            if str(game_board[player_input - 1]) not in 'XO':
                game_board[player_input - 1] = player_side
                input_check = True
            else:
                print('This field is full')
        else:
            print('Repeat input, use numbers from 1 to 9')


def win_condition(game_board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for cord in win_combinations:
        if game_board[cord[0]] == game_board[cord[1]] == game_board[cord[2]]:
            return game_board[cord[0]]
        return False


game()

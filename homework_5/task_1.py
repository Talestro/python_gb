# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


from random import randint


def first_turn_draw():
    draw = randint(0, 2)
    if draw == 1:
        return True
    else:
        return False


def game():
    first_player_candy, second_player_candy = 0, 0
    game_continues = True
    current_player = first_turn_draw()
    remain_candy = 2021
    while game_continues:
        candy_taken = players_action(current_player)
        remain_candy -= candy_taken
        if current_player:
            first_player_candy += candy_taken
            turn_info('1-st Player', first_player_candy, remain_candy)
        else:
            second_player_candy += candy_taken
            turn_info('2-nd Player', second_player_candy, remain_candy)
        if remain_candy <= 0:
            break
        current_player = not current_player
    if current_player:
        print('1-st Player win!!! 1-st Player get all candy.')
    else:
        print('2-nd Player win!!! 2-nd Player get all candy.')


def players_action(player):
    if player:
        name_player = '1-st Player'
    else:
        name_player = '2-nd Player'

    while True:
        try:
            candy_taken = int(input(f'{name_player} - enter the amount of candy you want to take: '))
        except ValueError:
            print('Wrong input - try again: ')
        else:
            break
    while candy_taken not in range(1, 29):
        candy_taken = int(input(f'{name_player} - wrong candy amount, try again (use numbers form 1 to 28): '))
    return candy_taken


def turn_info(player, current_candy, remain):
    print(f'Now {player} have {current_candy} candy. Candy left on the table: {remain}.')


game()

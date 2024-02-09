import sys
from colorama import Fore, Style, init
from winner import winner
from hashing import Hmac
from help import Table

init()

RESET = Style.RESET_ALL
RED = Fore.RED
GREEN = Fore.GREEN


def send_menu():
    print('Available moves:')
    for i, move in enumerate(moves):
        print(f'{i + 1} - {move}')
    print('0 - Exit')
    print('? - Help')
    return input('Enter your move: ')


def send_table():
    print(f"{GREEN}Here's a table displaying the winner depending on your and PC's moves:{RESET}")
    table = Table(moves)
    table.print_ascii_table()
    print('Now please make a move')


def make_move():
    computer = Hmac(moves)
    print('HMAC:', computer.get_hmac())

    user_move = ''
    while not (user_move.isdigit() and int(user_move) in range(1, len(moves) + 1)):
        if user_move == '?':
            send_table()
        elif user_move == '0':
            print('Game Over.')
            return
        elif user_move == '':
            pass
        else:
            print(f"{RED}Invalid input. You should choose from the menu provided below.{RESET}")
        user_move = send_menu()

    print('Your move:', moves[int(user_move) - 1])
    print('Computer move:', computer.move)
    print(winner(moves, computer.move_index, int(user_move) - 1) + '!')
    print('HMAC key:', computer.key)


moves = sys.argv[1:]

# Handle the incorrect arguments
errorMessages = []
if len(moves) % 2 == 0:
    errorMessages.append('The number of moves should be odd.')
if len(moves) < 3:
    errorMessages.append('There should be at least 3 moves.')
if len(set(moves)) != len(moves):
    errorMessages.append('Move names should be unique.')

if len(errorMessages) > 0:
    print(' '.join(errorMessages) + ' Try again.')
else:
    make_move()

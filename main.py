import sys
from colorama import Fore, Style, init
from winner import winner
from hashing import Hmac
from help import Table

# Initialize colorama
init()

# Output colors
RESET = Style.RESET_ALL
RED = Fore.RED
GREEN = Fore.GREEN


def make_move():
    # Generate computer's move
    computer = Hmac(moves)
    print('HMAC:', computer.get_hmac())

    # Display the menu
    print('Available moves:')
    for i, move in enumerate(moves):
        print(f'{i + 1} - {move}')
    print('0 - Exit')
    print('? - Help')

    user_move = input('Enter your move: ')
    if user_move == '?':
        print(f"{GREEN}Here's a table displaying the winner depending on your and PC's moves:{RESET}")
        table = Table(moves)
        table.print_ascii_table()
        print('Now please make a move')
        make_move()
    elif user_move == '0':
        print('Game Over.')
    elif user_move.isdigit() and int(user_move) in range(1, len(moves) + 1):
        print('Your move:', moves[int(user_move) - 1])
        print('Computer move:', computer.move)
        print(winner(moves, computer.move_index, int(user_move) - 1) + '!')
        print('HMAC key:', computer.key)
    else:
        print(f"{RED}Invalid input. You should choose from the menu provided below.{RESET}")
        make_move()


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

import random

def play():
    continue_play = 'y'

    while True:
        player = input("'r' - rock, 'p' - paper, 's' - scissors: ")
        computer = random.choice(['r', 'p', 'c'])

        if player == computer:
            print(f"It's a tie. Player: {player}, PC: {computer}")
        elif is_win(player, computer):
            print(f"You won! Player: {player}, PC: {computer}")
        else:
            print(f"You lost! Player: {player}, PC: {computer}")

        continue_play = input("Continue playing (n to exit) ")
        if continue_play == 'n':
            break


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
    or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True


play()
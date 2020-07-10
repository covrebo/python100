from classes import Player, Roll
import random
import time

def main():
    print_title()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def print_title():
    print('-' * 40)
    print()
    print(' ' * 9 + 'ROCK, PAPER, SCISSORS')
    print()
    print('-' * 40)
    print()

def get_players_name():
    name = input('What is your name: ')
    return name

def build_the_three_rolls():
    rolls = []
    rolls.append(Roll('Rock', 'Scissors', 'Paper'))
    rolls.append(Roll('Scissors', 'Paper', 'Rock'))
    rolls.append(Roll('Paper', 'Rock', 'Scissors'))
    return rolls

def game_loop(player1, player2, rolls):
    count = 1
    while count < 6:
        player2.roll = random.choice(rolls)
        #TODO: validate user input and store roll as object - correct can_defeat method
        player1.roll = input('Enter [Rock], [Paper], or [Scissors]: ')

        outcome = player2.roll.can_defeat(player1.roll)

        time.sleep(1)

        print(f'{player2.name} has rolled {player2.roll.name}')

        time.sleep(1)

        # TODO: add win counts and handle ties better
        if outcome == 'Win':
            print(f'{player1.roll} beats {player2.roll.name}, {player1.name} wins!')
        elif outcome == 'Lose':
            print(f'{player2.roll.name} beats {player1.roll}, {player2.name} wins!')
        else:
            print("It's a tie!")

        count += 1

    # TODO: Compute who won

if __name__ == '__main__':
    main()


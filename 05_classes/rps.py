from classes import Player, Roll
import random
import time

def main():
    print_title()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("RPS Bot")

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

    # prompt the user for the number of rounds and validate the input
    while True:
        num_games = input(f'How many rounds do you want? ')
        try:
            val = int(num_games)
            if val > 0:
                num_games = int(num_games)
                break
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Please enter an integer.")

    # set the round counter
    count = 0

    # convert the number of games to an int
    num_games = int(num_games)

    while count < num_games:

        # assign player 2 a random roll
        player2.roll = random.choice(rolls)

        # prompt the user for a roll and validate input
        player1.roll = input('Enter [R]ock, [P]aper, or [S]cissors: ')
        while True:
            if player1.roll == 'R':
                for roll in rolls:
                    if roll.name == 'Rock':
                        player1.roll = roll
                break
            elif player1.roll == 'P':
                for roll in rolls:
                    if roll.name == 'Paper':
                        player1.roll = roll
                break
            elif player1.roll == 'S':
                for roll in rolls:
                    if roll.name == 'Scissors':
                        player1.roll = roll
                break
            else:
                print("Input not recognized.")
                player1.roll = input('Enter [R]ock, [P]aper, or [S]cissors: ')

        outcome = player1.roll.can_defeat(player2.roll)

        time.sleep(1)

        # report the player 2 roll
        print(f'{player2.name} has rolled {player2.roll.name}')

        time.sleep(1)

        # award the win and increment the round if there is a winner
        if outcome == 'Win':
            player1.wins += 1
            count += 1
            print(f'{player1.roll.name} beats {player2.roll.name}, {player1.name} wins!')
            time.sleep(1)
            print(f'That concludes round {count}. {player1.name} has '
                  f'{player1.wins} wins and {player2.name} has {player2.wins} wins.')
        elif outcome == 'Lose':
            player2.wins += 1
            count += 1
            print(f'{player2.roll.name} beats {player1.roll.name}, {player2.name} wins!')
            time.sleep(1)
            print(f'That concludes round {count}. {player1.name} has '
                  f'{player1.wins} wins and {player2.name} has {player2.wins} wins.')
        else:
            print("It's a tie. Doesn't count!")

    # Compute the winner
    if player1.wins > player2.wins:
        winner = player1.name
    elif player2.wins > player1.wins:
        winner = player2.name
    else:
        winner = None

    # Report the results
    print(f'The final score is:')
    print(f'\t {player1.name} with {player1.wins} wins')
    print(f'\t {player2.name} with {player2.wins} wins')
    if winner:
        print(f'The winner is {winner}!')
    else:
        print(f'Looks like a tie. Next time, pick an odd number of rounds to avoid a tie.')

if __name__ == '__main__':
    main()


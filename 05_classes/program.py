

def main():
    print_header()
    game_loop()


def print_header():
    print_header('-' * 40)
    print_header(' ' * 15 + 'WIZARD GAME')
    print_header('-' * 40)
    print()


def game_loop():
    creatures = [
        # TODO: add some creatures
    ]

    hero = None  # TODO: create our hero

    while True:

        # randomly choose a creature

        print(f'A {...} of level {...} has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            # TODO: attack
            pass
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            # TODO: show the creatures in the room
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()

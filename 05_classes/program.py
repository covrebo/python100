from actors import Creature, Wizard, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('-' * 40)
    print(' ' * 15 + 'WIZARD GAME')
    print('-' * 40)
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil Wizard', 1000),
    ]

    print(creatures)

    hero = Wizard("Griswold", 75)

    while True:

        # randomly choose a creature
        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f"The wizard, {hero.name}, defeated {active_creature.name}!")
            else:
                print('The wizard has been dealt a defeat.')
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for creature in creatures:
                print(f' * {creature.name} of level {creature.level}')
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()

if __name__ == '__main__':
    main()
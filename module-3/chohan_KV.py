# Khaile Vallejo
#Module 3.2 Assignment
# Change documentation:
#Changed input prompts to KV:
#Changed house fee from 10% to 12%.
# Added notice of 10 mon bonus for a dice total of 2 or 7.
#Added bonus message and purse update for a total of 2 or 7.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the dice total is 2 or 7, you get a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('KV: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('KV: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Bonus: total of 2 or 7 adds 10 mon to the purse.
    if diceTotal == 2 or diceTotal == 7:
        print('The dice total is', diceTotal, 'and you get a 10 mon bonus!')
        purse = purse + 10

    # Determine whether the player won.
    rollIsEven = diceTotal % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        houseFee = pot * 12 // 100  # House fee is 12%.
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee
    else:
        purse = purse - pot
        print('You lost!')

    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()

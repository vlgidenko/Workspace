#Player and computer both choose a number
#Numbers are added up and then player guesses if the number is odd or even
#Vasiliy Gidenko

import random
#Chooses a number 0 through 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

comp = random.choice(numbers)
play = False
player = 0
#String for winning or losing
winner = 'You Win. The number was'
loser = 'You Lose. The number was'

print('Odds or evens')

#plays the game until it is broken
while play == False:
    player = int(input('Pick a number(Type 0 to stop playing): '))
    if player == 0: #breaks out of while loop if player chooses 0
        print ('Game over')
        break
    else:
        end = player + comp
        play = input('Choose Odd or Even: ')
        #checking if player won based on the remainder
        if end %2 == 0 and play.lower() == "even":
          print(winner, end)
        elif end %2 == 0 and play.lower() == "odd":
            print(loser, end)
        if end %2 != 0 and play.lower() == "even":
            print(loser, end)
        elif end %2 != 0 and play.lower() == "odd":
            print(winner, end)
        elif play.lower() != "odd" and play.lower() != "even":
            print('Invalid Choice')
    comp = random.choice(numbers)
    play = False
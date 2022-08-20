import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

comp = random.choice(numbers)
play = False
player = 0
winner = 'You Win. The number was'
loser = 'You Lose. The number was'

print('Odds or evens')

while play == False:
    player = int(input('Pick a number(Type 0 to stop playing): '))
    if player == 0:
        print ('Game over')
        break
    else:
        end = player + comp
        play = input('Choose Odd or Even: ')

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
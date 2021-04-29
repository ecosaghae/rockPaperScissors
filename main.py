import random

print('Enter rock, paper, or scissors')
print('\U0001F914')
# input user to enter their pick
pick = input('> ')
# print out user's pick
print('My pick is', pick)

picks = ['rock', 'paper', 'scissors']
# generate random number from picks
computer_pick = picks[random.randint(0, len(picks) - 1)]
# print out computer's pick
print('Computer pick is', computer_pick)

"""
Every emoji has a Unicode associated with it. Emojis also have a CLDR short name, which can also be used.

From the list of unicodes, replace “+” with “000”. For example – “U+1F600” will become “U0001F600” and 
prefix the unicode with “\” and print it.
"""
if pick in picks: # only print out if user's input is acceptable
    if pick == computer_pick:
        print('Tie \U0001F914')
    if pick == 'rock':
        if computer_pick == 'paper':
            print('You lost \U0001F923')
        elif computer_pick == 'scissors':
            print('You won \U0001F609')
    if pick == 'paper':
        if computer_pick == 'scissors':
            print('You lost \U0001F923')
        elif computer_pick == 'rock':
            print('You won \U0001F609')
    if pick == 'scissors':
        if computer_pick == 'rock':
            print('You lost \U0001F923')
        elif computer_pick == 'paper':
            print('You won \U0001F609')
else: # only print out if user enters invalid pick
    print('Invalid choice, Try again')

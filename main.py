import random
import os
from art import logo

answer = random.randint(1,100)
print(logo)

print("Welcome to the number guesssing game !\nI'm thinking of a number between 1-10\n")
quest = input("Choose a difficulty. Type 'easy' or 'hard:' ")

def take_a_guess():
     
    if quest == 'easy':
        max_attempts = 10
    else:
        max_attempts = 5
        
    
    for i in range(max_attempts):
        print(f'You have {max_attempts} attempts reamaining to guess the number')
        user = int(input('Make a guess:\n'))
        if user != answer:
            if user < answer and max_attempts > 1:
                max_attempts -= 1
                print('Too Low.\nGuess again.')
            elif user > answer and max_attempts > 1:
                max_attempts -= 1
                print('Too High.\nGuess again.')
            elif user != answer and max_attempts == 1:
                print('Game over.\nYou Lose.')
                
        else:
            if user == answer:
                print(f'Yay! you got it right, the answer is {answer} !')
                
                
    while input("Do you want to play agin. Type 'y' or 'n': ") == 'n':
        os.system('clear')
        return

take_a_guess()

                


        

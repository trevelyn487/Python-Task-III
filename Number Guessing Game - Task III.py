import random


#Ensuring user enters integer while making guesses.
def guess_validation(instructions):
    while True:
        try:
            entry = int(input(instructions))
        except ValueError:
            print("Entry error! Please enter an integer.")
        else:
            return entry
            break


def easy():
    number = random.randint(1, 10)
    guesses_made = 1
    
    print('''\nYou've selected Easy. 
For this level, you're to guess a number from 1 to 10. 
You have 6 guesses in total.''')
   
    while guesses_made <= 6:
        guess = guess_validation("\nMake a Guess: ")
        if guess == number:
            print("You got it right!")
            break
        
        else:
            guesses_left = int(6 - guesses_made)
            print('''That was wrong! 
You have ''' + str(guesses_left) + ''' guess(es) left.''')
            guesses_made += 1
              
    else:
        print('''
Game over! The correct number was ''' + str(number) + ".")
        
    
def medium():
    number = random.randint(1, 20)
    guesses_made = 1
    
    print('''\nYou've selected Medium. 
For this level, you're to guess a number from 1 to 20. 
You have 4 guesses in total.''')
    
    while guesses_made <= 4:
        guess = guess_validation("\nMake a Guess: ")
        if guess == number:
            print("You got it right!")
            break
        
        else:
            guesses_left = int(4 - guesses_made)
            print('''That was wrong! 
You have ''' + str(guesses_left) + ''' guess(es) left.''')
            guesses_made += 1
              
    else:
        print('''
Game over! The correct number was ''' + str(number) + ".")
        

def hard():
    number = random.randint(1, 50)
    guesses_made = 1
    
    print('''\nYou've selected Hard. 
For this level, you're to guess a number from 1 to 50. 
You have 3 guesses in total.''')
    
    while guesses_made <= 3:
        guess = guess_validation("\nMake a Guess: ")
        if guess == number:
            print("You got it right!")
            break
        
        else:
            guesses_left = int(3 - guesses_made)
            print('''That was wrong! 
You have ''' + str(guesses_left) + ''' guess(es) left.''')
            guesses_made += 1
              
    else:
        print('''
Game over! The correct number was ''' + str(number) + ".")
        
    
play = True
while True:
    level = True
    
    level = input('''
Welcome to my Number Guessing Game! 
This game has 3 levels - "Easy", "Medium" and "Hard". 
Select a level to start: ''').lower()
    
    while True:
        if level == "easy":
            easy()
            break
        
        elif level == "medium":
            medium()
            break
        
        elif level == "hard":
            hard()
            break 
        
        #Ensuring user selects level correctly.
        else:
            if level != "easy" or "medium" or "hard":
                level = input("Invalid selection. Please select an appropriate level: ")
    
    #Giving user the ability to choose to play again or not.
    keep_playing = input('''\nWould you like to play again? Respond accordingly with either a "Yes" or "No": ''').lower()
    
    if keep_playing == "yes":
        play = True
    
    elif keep_playing == "no":
        level = False
        play = False
        print("\nEnjoyed the game? Come play again soon.")
        break


import random

print("***Game of Guess***")

question = input("Hello! \nWould you like to play a guess game? \nEnter y/n : ")

tries = 1

if question == 'y' or question == 'Y':
    
    howmany = int(input("Enter how many games would you like to play :"))
    
    for game in range(howmany):
        
        print("I am going to think a number between 1-25")
        number = random.randint(1,26) 
        guess = int(input("Guess a number between 1-25 : "))
        
        while guess != number:
            
            if guess > number:
                print("your selction is high")
            
            else:
                print("you selection is low")
            
            guess = int(input("Wrong, try again: "))
             
            tries += 1
            
        if number == guess:
            
            print("Your guess is correct\n")
            print("The number was ",number)
            print("No of tries:",tries)
        
else:
    print("Okay")
        

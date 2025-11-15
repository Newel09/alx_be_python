import random

"""
Import the random module: At the beginning of your code, add the line import random. 
This allows you to use functions from the random module, like generating random numbers.
Generate a secret number: Use random.randint(1, 10) to generate a random number between 1 and 10 (you can adjust the range if you want). 
Store this in a variable called secret_number.
Get user’s guess: Prompt the user to guess the number using input(). 
Convert the user’s input to an integer using int(). Store this in a variable called guess.
Match the guess:Use a Match Case statement to compare the user’s guess with the secret number:
If the guess is correct, display a message like “Congratulations, you guessed it!”
If the guess is too high, display a message like “Oops, your guess is a bit high. Try again!”
If the guess is too low, display a message like “Nope, your guess is a bit low. Give it another shot!”
Offer to play again: Ask the user if they want to play again using an if statement and user input.
"""

secret_number = random.randint(1,15) # Random numbers in between from 1 to 15

while True:
 guess = int(input("I am thinking of a number can you guess it: "))


 match guess:
    case _ if guess == secret_number: # if guess is exactly equal to secret
     print("Congratulations, you guessed it!")
    
    case _ if guess > secret_number:
      print("Oops, your guess is a bit high. Try again!")

    case _ if guess < secret_number:
      print("Nope, your guess is a bit low. Give it another shot!")
    
    case _:
      print("Nice! You got it!")  # stop the loop when they are right

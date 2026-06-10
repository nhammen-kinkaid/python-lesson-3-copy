import random

secret_number = random.randrange(1,10)
player_guess = int(input("Guess the random number: "))

while player_guess != secret_number:
    print("That was incorrect.")
    player_guess = int(input("Guess the random number: "))

if player_guess == secret_number:
    print("You were right!")
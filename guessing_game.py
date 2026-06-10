import random

player_response = "yes"

while player_response == "yes":
    player_guess = 0
    secret_number = random.randrange(1,3)

    while player_guess != secret_number:
        player_guess = int(input("Guess the random number: "))
        if player_guess > secret_number:
            print("That was too high.")
        if player_guess < secret_number:
            print("That was too low.")

    if player_guess == secret_number:
        print("You were right!")

    player_response = input("Do you want to play again? ")
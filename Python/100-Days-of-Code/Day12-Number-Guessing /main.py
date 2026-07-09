from random import randint
from art import logo
from art import logo2

EASY = 10
HARD = 5


def check_guess(user_guess, actual_guess, turns):
    if user_guess > actual_guess:
        print("Your guess is too high.")
        return turns - 1
    elif user_guess < actual_guess:
        print("Your guess is too low.")
        return turns - 1
    else:
        print(f"Your guess is correct: {actual_guess}, congrats!!!")
        print(logo2)




def set_difficulty():
    while True:
        level= input("Choose a difficulty 'easy' or 'hard': ")
        if level == "easy":
            return EASY
        elif level == "hard":
            return HARD
        else:
            print("Wrong, try again ")


def game():
    print(logo)
    print("Welcome to Number Guessing Project")
    print("I'm thinking a number between 1 and 100")
    answer = randint(1, 100)
    print("The correct answer is:", answer)


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining ")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You have lost the game")
            break
        elif guess != answer:
            print("Try again...")


game()

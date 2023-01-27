import random

Input = "The number you guessed:", int(input("Enter a guess"))

randomnumber = random.randint(1, 100)

number = randomnumber


def Game():
    print("The random number program guessed is:", randomnumber)

    print(Input)

    number = randomnumber


if Input > number:

    print("Too high than what program guessed, try again")

elif Input < number:

    print("Too low than what program guessed, try again")

elif Input < 2:

    print("Guessed too low, guessing range is 1 - 100, try again")

elif Input > 100:

    print("Guessed too high, guessing range is 1 - 100, try again")

elif Input == randomnumber:

    print("Congratulations you guessed it right!")

else:

    print("Invalid input! Guess the number between 1 to 100")

Game()
import random



def main():

    # Create a list

    numbers = [0] * 7

    # populate the list with random numbers

    for index in range(7):

        numbers[index] = random.randint(0, 9)


    # Display the random numbers

    print('Here are your lottery numbers:')

    for index in range(7):

        print(numbers[index], end=',')

    print()



main()


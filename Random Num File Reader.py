def main():

    total = count = 0


    try:

        f = open("file.txt", "r")

        print("Print random numbers read from the file: ")

        for number in f:

            n = int(number)

            total = total + n

            count = count + 1

            print(n)

        print("The total of the numbers read from file is {}".format(total))

        print("The numbers of random numbers read from the file is {}".format(count))

    except ValueError:

        print("Invalid value")


main()


def multiply(x, y):

    if x == 1:

        return y

    else:

        return y + multiply(x-1, y)


def main ():

  x = int (input("Enter the first number:"))

  y = int (input("Enter the second number:"))

  print (x, "x", y, "=", end="")

  print (" =", multiply (x, y))


#Call the main() function.


if __name__ == "__main__":

  main()


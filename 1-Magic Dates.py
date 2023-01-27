#Magic Dates

month = int(input("Enter the month (numbers only) : "))

day = int(input("Enter the day (numbers only) : "))

year = int(input("Enter the year (last two digits only) : "))


if month == 6 and day == 10 and year == month * day:

    print("The date is magic!")


else:

    print("The date is not magic!")
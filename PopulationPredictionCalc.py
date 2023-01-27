organisms = int(input("Starting number of the organism"))

increase = float(input("Average daily increase (%): "))

multiply = int(input("Number of days to multiply:"))



for i in range(1, multiply +1):

  print("Days:", i, "Population:", organisms)

  organisms = round(organisms * (1 + increase/100), 2)

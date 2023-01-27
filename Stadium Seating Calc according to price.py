def Total_Income(Seat_Cost_ClassA, Seat_Cost_ClassB, Seat_Cost_ClassC):

  return Seat_Cost_ClassA + Seat_Cost_ClassB + Seat_Cost_ClassC


aCount = int(input("Number of Class A tickets sold: "))

bCount = int(input("Number of Class B tickets sold: "))

cCount = int(input("Number of Class C tickets sold: "))



Seat_Cost_ClassA = aCount * 20

Seat_Cost_ClassB = bCount * 15

Seat_Cost_ClassC = cCount * 10


def seats():

  global Seat_Cost_ClassA

  global Seat_Cost_ClassB

  global Seat_Cost_ClassC

  print("Class A tickets amount:", Seat_Cost_ClassA)

  print("Class B tickets amount:", Seat_Cost_ClassB)

  print("Class C tickets amount:", Seat_Cost_ClassC)

seats()


sum = Total_Income(Seat_Cost_ClassA, Seat_Cost_ClassB, Seat_Cost_ClassC)


print("Total Income of {} ClassA, {} ClassB and {} ClassC tickets is {}".format(aCount, bCount, cCount, sum))
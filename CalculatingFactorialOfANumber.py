Number = int(input("Enter a number:"))

while Number < 0:
    Number = int(input("Enter a nonnegative number:"))

Integer = 1

for i in range(1, Number + 1):
    Integer = Integer * i

print("Fictorial of", Number, "is: ", Integer)
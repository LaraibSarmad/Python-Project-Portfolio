import random

number = int(input("Type the numbers you want to write in file in range 1 to 500 : "))

file = open( 'file.txt' , 'w')

for i in range(number):

    file.write(str(random.randint( 1 , 500 ))+ "\n")

file.close()

print("FILE WRITTEN SUCESSFULLY!!")

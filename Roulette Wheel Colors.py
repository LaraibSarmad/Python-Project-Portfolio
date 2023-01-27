pocket = int (input("Pocket Number"))

if pocket < 0 or pocket >36:

  print("The pocket should be numbered from 0 to 36")

elif pocket == 0:

  print("Green")

elif pocket >= 1 and pocket <= 10 or pocket>=19 and pocket <=28:

  if pocket % 2 == 0:

    print("Black")

  else:

    print ("Red")

elif pocket >= 11 and pocket <=18 or pocket >=29 and pocket <=36:

  if pocket % 2 == 0:

    print("Red")

else:

    print ("Black")

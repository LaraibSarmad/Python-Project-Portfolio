import matplotlib.pyplot as plt


filename = input('Enter the name of file : ')


# open file in read mode


fptr = open(filename , 'r')


# set the labels


categories = [ 'Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc' ]


# store the expenses in the order of labels


expenses = []


# read the content of file


strng = fptr.read()


# read the file line by line


for line in strng.split('\n'):

expenses.append( int( line ) )


colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green', 'red']


# plot the pie chart


plt.pie(expenses, labels = categories, colors = colors, autopct='%1.1f%%', shadow=True, startangle=140)


# set the axis as equsl


plt.axis('equal')


# display the chart


plt.show()
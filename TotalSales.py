#Total Sales


# store the sales

sales = []


#input


for i in range(7):

    sales += [int(input('Enter day '+str(i+1)+' sales: '))]


# loop

total = 0

for sale in sales:

    total += sale

print('\nTotal sales for the week is : $'+str(total))
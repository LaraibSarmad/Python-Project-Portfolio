# store rainfall data

rainfall = []


# list with month names

months = ['January','February','March','April','May','June',

          'July','August','September','October','November','December']


# accept input

for month in months:

    rainfall += [float(input('Enter rainfall for '+month+': '))]


# determine the month with lowest / highest rainfall

lowest = highest = 0


for i in range(1,12):

    if(rainfall[i]<rainfall[lowest]):

        lowest = i

    elif(rainfall[i]>rainfall[highest]):

        highest = i


# calculate the total and average monthly rainfall

total = 0

for reading in rainfall:

    total+=reading


avg_rainfall = total/12


# print the results

print('\nTotal rainfall : '+str(total)+' units')

print('Average monthly rainfall : '+str(round(avg_rainfall,2))+' units')

print('Lowest rainfall was in the month of '+months[lowest])

print('Highest rainfall was in the month of '+months[highest])

import matplotlib.pyplot as plt


def drawChart():
    file = open('1994_Weekly_Gas_Averages.txt')

    input_data = file.read()

    gas_value = input_data.split()

    file.close()

    for i in range(0, len(gas_value)):
        gas_value[i] = float(gas_value[i].strip())

    x_coords = list(range(1, 53))

    plt.plot(x_coords, gas_value)

    plt.xlim([1, 52])

    plt.title('1994 Weekly Gas Prices')

    plt.xlabel('Week')

    plt.ylabel('Price')

    plt.show()


# call the function


drawChart()


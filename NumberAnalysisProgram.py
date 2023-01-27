#Lowest number

def Lowest(num_list):

    Lowest = min(num_list)

    return Lowest



#Highest numbers

def Highest(num_list):

    Highest = max(num_list)

    return Highest



#Sum of the numbers

def Sum(num_list):

    Sum = sum(num_list)

    return Sum



#Average of the numbers in a list

def Average(num_list):

    Average = sum(num_list) / len(num_list)

    return Average


def main():

    inputs = input("Enter 20 numbers seperated by space: ")

    inputs = list(map(int, inputs.split()))


    num_list_Lowest = Lowest(inputs)

    print(f"Lowest : {num_list_Lowest}")


    num_list_Highest = Highest(inputs)

    print(f"Highest : {num_list_Highest}")


    num_list_Sum = Sum(inputs)

    print(f"Sum : {num_list_Sum}")


    num_list_Average = Average(inputs)

    print(f"Average : {num_list_Average}")



# Call function

if __name__ == '__main__':

    main()

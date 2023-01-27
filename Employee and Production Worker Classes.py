class Employee:

    def __init__(self, name, number):
        self.__name = name

        self.__number = number

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift, hourly_pay_rate):
        Employee.__init__(self, name, number)

        self.__shift = shift

        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


def main():
    # Prompt the user to enter data for the ProductionWorker object

    name = input("Enter the employee's name: ")

    number = input("Enter the employee's number: ")

    shift = input("Enter the employee's shift (1 for day, 2 for night): ")

    hourly_pay_rate = input("Enter the employee's hourly pay rate: ")

    # Create a ProductionWorker object

    worker = ProductionWorker(name, number, shift, hourly_pay_rate)

    # Display the data for the object

    print("Employee Name:", worker.get_name())

    print("Employee Number:", worker.get_number())

    print("Shift:", worker.get_shift())

    print("Hourly Pay Rate:", worker.get_hourly_pay_rate())


main()

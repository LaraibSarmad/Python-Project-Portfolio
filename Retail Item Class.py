class RetailItem:

    def __init__(self, description, units, price):

        self.description = description

        self.units = units

        self.price = price

    def displayDesc(self):

      print ("Description: "), self.description

    def displayUnits(self):

      print ("Units in inventory: "), self.units

    def displayUnits(self):

      print ("Price: $",self.price)


item1 = RetailItem("Jacket", 12, 59.95)

item2 = RetailItem("Designer Jeans", 40, 34.95)

item3 = RetailItem("Shirt", 20, 24.95)


print ("\nRetail Item 1:")

item1.displayDesc();

item1.displayUnits();

item1.displayPrice();


print ("\nRetail Item 2:")

item2. displayDesc();

item2.displayUnits();

item2.displayPrice();


print ("\nRetail Item 3:")

item3. displayDesc();

item3.displayUnits();

item3.displayPrice();
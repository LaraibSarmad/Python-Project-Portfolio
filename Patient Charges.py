import datetime #importing package

class Patient:

  def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):

    self.first_name = first_name

    self.middle_name = middle_name

    self.last_name = last_name

    self.address = address

    self.city = city

    self.state = state

    self.zip_code = zip_code

    self.phone_number = phone_number

    self.emergency_contact_name = emergency_contact_name

    self.emergency_contact_phone = emergency_contact_phone

  p=Patient(fname,lname,date1, address,phone_number)


p.display() #calling display() method of Patient class throught instance of Patient class


#Creating three instances of Appointment class and passing the values

a1=Appointment("11/110/2022", "Physical Rxam", "Dr. Irvine", 250)

a2=Appointment("11/10/2022", "Blood Test", "Dr. Smith", 200)

a3=Appointment("11/10/2022", "X-ray", "Dr. Jamison", 500)

#calling display() method of Appointment class throught 3 instances of Appointment class one by one

a1.display()

a2.display()

a3.display()

#calculating total bill of a patient

print("Total charge is: %.2f "%(a1.bill+a2.bill+a3.bill))
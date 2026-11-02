# Khaile Vallejo Assignment 10.2
# 10/04/2026
# Creating 2 classes Employee Class & Production Worker Class

print("Hello User!")

# Employee Class
class Employee:
    def __init__(self):
        self.employee_name = ""
        self.employee_gender = ""
        self.hourly_pay_rate = 0.0
        self.employee_number = 0

    # Setters
    def set_employee_name(self, name):
        self.employee_name = name

    def set_employee_gender(self, gender):
        self.employee_gender = gender

    def set_hourly_pay_rate(self, pay_rate):
        self.hourly_pay_rate = pay_rate

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    # Getters
    def get_employee_name(self):
        return self.employee_name

    def get_employee_gender(self):
        return self.employee_gender

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def get_employee_number(self):
        return self.employee_number


# Production Worker Class inherits from Employee
class ProductionWorker(Employee):
    def __init__(self):
        super().__init__()
        self.shift_number = 0

    # Setter
    def set_shift_number(self, shift):
        self.shift_number = shift

    # Getter
    def get_shift_number(self):
        return self.shift_number


# Main Class
class Main:
    def main(self):

        # Create two Employee objects
        employee1 = Employee()
        employee2 = Employee()

        # Set Employee 1 values
        employee1.set_employee_name("John Smith")
        employee1.set_employee_gender("Male")
        employee1.set_hourly_pay_rate(18.50)
        employee1.set_employee_number(1001)

        # Set Employee 2 values
        employee2.set_employee_name("Sarah Johnson")
        employee2.set_employee_gender("Female")
        employee2.set_hourly_pay_rate(21.75)
        employee2.set_employee_number(1002)

        # Create two Production Worker objects
        worker1 = ProductionWorker()
        worker2 = ProductionWorker()

        # Set Production Worker 1 values
        worker1.set_employee_name("Mike Brown")
        worker1.set_employee_gender("Male")
        worker1.set_hourly_pay_rate(22.50)
        worker1.set_employee_number(2001)
        worker1.set_shift_number(1)

        # Set Production Worker 2 values
        worker2.set_employee_name("Lisa Davis")
        worker2.set_employee_gender("Female")
        worker2.set_hourly_pay_rate(24.25)
        worker2.set_employee_number(2002)
        worker2.set_shift_number(2)

        # Display Employee information
        print("\nEMPLOYEE INFORMATION")

        print("\nEmployee 1")
        print("Name:              ", employee1.get_employee_name())
        print("Gender:            ", employee1.get_employee_gender())
        print("Employee Number:   ", employee1.get_employee_number())
        print("Hourly Pay Rate:   ${:.2f}".format(employee1.get_hourly_pay_rate()))

        print("\nEmployee 2")
        print("Name:              ", employee2.get_employee_name())
        print("Gender:            ", employee2.get_employee_gender())
        print("Employee Number:   ", employee2.get_employee_number())
        print("Hourly Pay Rate:   ${:.2f}".format(employee2.get_hourly_pay_rate()))

        # Display Production Worker information
        print("\nPRODUCTION WORKER INFORMATION")

        print("\nProduction Worker 1")
        print("Name:              ", worker1.get_employee_name())
        print("Gender:            ", worker1.get_employee_gender())
        print("Employee Number:   ", worker1.get_employee_number())
        print("Hourly Pay Rate:   ${:.2f}".format(worker1.get_hourly_pay_rate()))
        print("Shift:             ", get_shift_name(worker1.get_shift_number()))

        print("\nProduction Worker 2")
        print("Name:              ", worker2.get_employee_name())
        print("Gender:            ", worker2.get_employee_gender())
        print("Employee Number:   ", worker2.get_employee_number())
        print("Hourly Pay Rate:   ${:.2f}".format(worker2.get_hourly_pay_rate()))
        print("Shift:             ", get_shift_name(worker2.get_shift_number()))


# Converts the shift number into a readable description
def get_shift_name(shift_number):
    if shift_number == 1:
        return "Day Shift"
    elif shift_number == 2:
        return "Swing Shift"
    elif shift_number == 3:
        return "Graveyard Shift"
    else:
        return "Unknown Shift"


# Create a Main object and run the program
program = Main()
program.main()
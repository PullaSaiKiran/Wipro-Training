class Employee:
    def __init__(self, emp_id, name, salary, pf=0.0, da=0.0):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary
        self.__pf = pf
        self.__da = da

    # Getters
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_pf(self):
        return self.__pf

    def get_da(self):
        return self.__da

    # Setters
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_pf(self, pf):
        self.__pf = pf

    def set_da(self, da):
        self.__da = da

    # Display employee info
    def display_info(self):
        print("\n===== Employee Information =====")
        print(f"Employee ID: {self.__emp_id}")
        print(f"Employee Name: {self.__name}")
        print(f"Base Salary: {self.__salary}")
        print(f"PF: {self.__pf}")
        print(f"DA: {self.__da}")
        print(f"Net Salary: {self.__salary + self.__da - self.__pf}")

    # Salary hike method
    def give_hike(self, percentage):
        if percentage > 0:
            hike_amount = self.__salary * (percentage / 100)
            self.__salary += hike_amount
            print(f"Salary increased by {percentage}%. New Salary: {self.__salary}")
        else:
            print("Percentage must be positive!")


# Menu-driven program
def main():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Base Salary: "))
    pf = float(input("Enter PF amount: "))
    da = float(input("Enter DA amount: "))

    emp = Employee(emp_id, name, salary, pf, da)

    while True:
        print("\n--- Employee Menu ---")
        print("1. Display Employee Info")
        print("2. Update PF")
        print("3. Update DA")
        print("4. Give Salary Hike")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp.display_info()
        elif choice == 2:
            pf_val = float(input("Enter new PF amount: "))
            emp.set_pf(pf_val)
            print("PF updated successfully.")
        elif choice == 3:
            da_val = float(input("Enter new DA amount: "))
            emp.set_da(da_val)
            print("DA updated successfully.")
        elif choice == 4:
            hike = float(input("Enter hike percentage: "))
            emp.give_hike(hike)
        elif choice == 5:
            print("Exiting Employee Management System...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

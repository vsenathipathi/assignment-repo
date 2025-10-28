# Design a class for an "Emp Management System" that tracks employee details, calculates salaries, handles promotions.
import json
class Employee:
    company_name = "Venkat Corporation"
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
    
    def __init__(self,emp_id,name,department,designation,base_salary,exp_yrs,promotion_history):
        self.emp_id = emp_id
        self.name = name 
        self.department = department
        self.designation = designation
        self.base_salary = base_salary
        self.exp_yrs = exp_yrs
        self.promotion_history = promotion_history

    def calculate_salary(self):
        if self.exp_yrs < 5:
            return self.base_salary
        elif self.exp_yrs < 10:
            return self.base_salary * 1.1
        else:
            return self.base_salary * 1.2
        
    def promote(self,new_designation,increment_percentage):
        self.promotion_history.append(self.designation)
        self.designation = new_designation
        self.base_salary =self.base_salary * (1+ increment_percentage/100)
        
    def display_info(self):
        # print(f"Employee ID: {self.emp_id}")
        # print(f"Name: {self.name}")
        # print(f"Department: {self.department}")
        # print(f"Designation: {self.designation}")
        # print(f"Base Salary: ${self.base_salary}")
        # print(f"Experience Years: {self.exp_yrs}")
        # print(f"Promotion History: {self.promotion_history}")
        # print(f"Current Salary: ${self.calculate_salary()}")
        # print(f"Company Name: {Employee.company_name}")
        # print("====================================")
        import pandas as pd
        df = pd.DataFrame([self.to_dict()])
        print(df)

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "base_salary": self.base_salary,
            "exp_yrs": self.exp_yrs,
            "promotion_history": self.promotion_history
        }

# emp_id,name,department,designation,base_salary,exp_yrs,promotion_history

from abc import ABC, abstractmethod
class EMS:
    def __init__(self):
        self.employees=[]
        self.load_from_file()

    def add_employee(self,emp):
        for i in self.employees:
            if i.emp_id==emp.emp_id:
                print("Employee Already Exists. Enter different emp ID")
                return
        self.employees.append(emp)
        print("Employee Added Successfully")
        self.save_to_file()

    def remove_employee(self):
        entered_id=int(input("Enter Employee ID to Delete: "))
        for i in self.employees:
            if i.emp_id==entered_id:
                self.employees.remove(i)
                print("Employee Removed Successfully")
                self.save_to_file()
                break
        else:
            print("Employee Not Found")
            exit

    def update_employee_data(self):
        entered_id=int(input("Enter Employee ID to Update (Name,Dep,Desig): "))
        for i in self.employees:
            if i.emp_id==entered_id:
                print("Employee Found! Current details:")
                i.display_info()
                print("Enter new details (press Enter to skip):")
                new_name=input("New Name: ")
                if new_name.strip():
                    i.name=new_name
                new_dep=input("New Department: ")
                if new_dep.strip():
                    i.department=new_dep
                print("Employee details updated successfully!")
                self.save_to_file()
                break
    def search_for_employee(self):
        entered_string=input("Enter Employee ID or Name to search: ")
        for i in self.employees:
# came to know, this is simple version. if entered_string.lower() in i.name.lower():
            if (i.name.lower()).find(entered_string.lower())!=-1:
                print("Hey, Employee Found!")
                i.display_info()
                break
            elif str(i.emp_id)==entered_string:
                print("Hey, Employee Found!")
                i.display_info()
                break
        else:
            print("Employee Not Found")
            return
        # i.name=entered_string
        # i.name.find(entered_string)

    def display_all_employees(self):
        # for i in self.employees:
        #     i.display_info()
        import pandas as pd
        df = pd.DataFrame([i.to_dict() for i in self.employees])
        print("====================== DISPLAYING ALL EMPLOYEES ========================")
        print(df)

    def promote_employee(self):
        entered_id=int(input("Enter Employee ID to Promote: "))
        for i in self.employees:
            if i.emp_id==entered_id:
                print("\nEmployee Found, His Details are:")
                print("====================================")
                i.display_info()
                new_designation=input("Enter New Designation: ")
                increment_percentage=int(input("Enter Increment Percentage: "))
                i.promote(new_designation, increment_percentage)
                print("Employee Promoted Successfully")
                break
        else:
            print("Employee Not Found")
            exit

    def calculate_total_payroll(self):
        total_payroll=0
        for i in self.employees:
            total_payroll+=i.calculate_salary()
        print(f"Total Payroll CTC to Comparny: ${total_payroll}")

    def display_all_employees(self):
        # for i in self.employees:
        #     i.display_info()
        import pandas as pd
        df = pd.DataFrame([i.to_dict() for i in self.employees])
        print("====================== DISPLAYING ALL EMPLOYEES ========================")
        print(df)
    
    def save_to_file(self):
        with open("employees.json", "w") as file:
            json.dump([i.to_dict() for i in self.employees], file, indent=4)
        print("Employee data saved successfully.")

    def load_from_file(self):
        try:
            with open("employees.json", "r") as file:
                data = json.load(file)
                for e in data:
                    # emp = Employee(e["emp_id"], e["name"], e["department"], e["designation"], e["base_salary"], e["exp_yrs"], e["promotion_history"])
                    emp = Employee(**e)
                    self.employees.append(emp)

        except FileNotFoundError:
            print("No existing employee data found.")
        except Exception as e:
            print(f"Error loading employee data: {e}")

if __name__ == "__main__":
    ems=EMS()
    # e1 = Employee(1, "Sathish", "IT", "Developer", 50000, 3, [])
    # e2 = Employee(2, "Anandhi", "IT", "DevOps Consultant", 60000, 6, [])
    # ems.add_employee(e1)
    # ems.add_employee(e2)

    while True:
        print("\n1. Add Employee | 2. Remove Employee | 3. Promote Employee | 4. Calculate Total Payroll | 5. Display All Employees | 6. Update Employee | 7. Search |q. Exit ")
        choice=int(input("Enter Your Choice: "))
        if choice==1: # Add Emp
            print("Ok, Lets add the employee details:")
            emp_id=int(input("Enter Employee ID: "))
            name=input("Enter Employee Name: ")
            department=input("Enter Employee Department: ")
            designation=input("Enter Employee Designation: ")
            base_salary=int(input("Enter Employee Base Salary: "))
            exp_yrs=int(input("Enter Employee Experience Years: "))
            promotion_history=[]
            emp=Employee(emp_id, name, department, designation, base_salary, exp_yrs, promotion_history)
            ems.add_employee(emp)

        elif choice==2:
            ems.remove_employee()
        elif choice==3:
            ems.promote_employee()
        elif choice==4:
            ems.calculate_total_payroll()
        elif choice==5:
            ems.display_all_employees()
        elif choice==6:
            ems.update_employee_data()
        elif choice==7:
            ems.search_for_employee()
        elif choice=="q":
            break
        else:
            print("Invalid Choice")


# [
#     {
#         "emp_id": 2,
#         "name": "Anandhi A",
#         "department": "HR",
#         "designation": "BPHR",
#         "base_salary": 20000,
#         "exp_yrs": 6,
#         "promotion_history": []
#     },
#     {
#         "emp_id": 3,
#         "name": "Sathish",
#         "department": "CIS",
#         "designation": "Manager",
#         "base_salary": 30000,
#         "exp_yrs": 15,
#         "promotion_history": []
#     },
#     {
#         "emp_id": 4,
#         "name": "Pramya",
#         "department": "OG",
#         "designation": "Doc",
#         "base_salary": 1000,
#         "exp_yrs": 9,
#         "promotion_history": []
#     }
# ]
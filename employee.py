class Employee:
    """
    Parent class for all employees.
    """

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print("\n----- Employee Details -----")
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Department  :", self.department)


class Developer(Employee):
    """
    Child class that inherits from Employee.
    """

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience
    ):
        # Call parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.programming_language = programming_language
        self.experience = experience

    def display_details(self):
        # Call parent class method
        super().display_details()

        print("Programming Language :", self.programming_language)
        print("Experience           :", self.experience, "years")
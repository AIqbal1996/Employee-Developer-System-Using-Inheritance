from employee import Employee, Developer


def main():

    print("========================================")
    print("   EMPLOYEE & DEVELOPER SYSTEM")
    print("========================================")

    # Create Employee objects
    employee1 = Employee(
        "E001",
        "Rahul",
        50000,
        "HR"
    )

    employee2 = Employee(
        "E002",
        "Priya",
        55000,
        "Finance"
    )

    # Create Developer object
    developer1 = Developer(
        "D001",
        "Arif",
        90000,
        "IT",
        "Python",
        5
    )

    # Display Employee details
    employee1.display_details()
    employee2.display_details()

    # Display Developer details
    developer1.display_details()

    # Demonstrate inheritance
    print("\n----- Inheritance Demonstration -----")

    print("Developer Name       :", developer1.name)
    print("Developer Salary     :", developer1.salary)
    print("Developer Department :", developer1.department)

    print(
        "Developer Language   :",
        developer1.programming_language
    )

    print(
        "Developer Experience :",
        developer1.experience,
        "years"
    )


if __name__ == "__main__":
    main()
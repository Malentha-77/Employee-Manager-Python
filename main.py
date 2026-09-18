employees = [
    {"name": "Alice", "age": 22, "salary": 9000, "active": True},
    {"name": "Brian", "age": 17, "salary": 12000, "active": True},
    {"name": "Chris", "age": 30, "salary": 15000, "active": False}
]


def show_employees(employees):
    for person in employees:
        print(
            f"{person['name']} - Age: {person['age']} - "
            f"Salary: {person['salary']} - Active: {person['active']}"
        )


def find_employee(employees, name):
    for person in employees:
        if person['name'] == name:
            return person
    return None


choice = ""

while choice != "4":
    print("\n1. Show employees")
    print("2. Find employee")
    print("3. Add employee")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_employees(employees)

    elif choice == "2":
        name = input("Enter employee name: ")
        employee = find_employee(employees, name)

        if employee:
            print(employee)
        else:
            print("Employee not found")

    elif choice == "3":
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = int(input("Enter employee salary: "))

        new_employee = {
            "name": name,
            "age": age,
            "salary": salary,
            "active": True
        }

        employees.append(new_employee)
        print("Employee added.")

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice")
import json

with open("employees.json", "r") as file:
    employees = json.load(file)

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

def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)



choice = ""

while choice != "5":
    print("\n1. Show employees")
    print("2. Find employee")
    print("3. Add employee")
    print("4. Remove employee")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_employees(employees)

    elif choice == "2":
        name = input("Enter employee name: ")

        if not name:
            print("Name cannot be empty.")
            continue

        employee = find_employee(employees, name)

        if employee:
            print(employee)

        else:
            print("Employee not found")

    elif choice == "3":
        name = input("Enter employee name: ")

        if not name:
            print("Name cannot be empty.")
            continue

        try:
            age = int(input("Enter employee age: "))
        except ValueError:
            print("Invalid age. Please enter a number.")
            continue

        try:
            salary = int(input("Enter employee salary: "))      
        except ValueError: 
            print("Invalid salary. Please enter a number.")
            continue    

        new_employee = {
            "name": name,
            "age": age,
            "salary": salary,
            "active": True
        }

        employees.append(new_employee)
        print("Employee added.")

    elif choice == "4":
        name = input("Enter employee name: ")

        if not name:
            print("Name cannot be empty.")
            continue

        employee = find_employee(employees, name)

        if employee:
            employees.remove(employee)
            print("Employee removed.")
        else:
            print("Employee not found")

    elif choice == "5":
        print("Goodbye!")

    else:
        print("Invalid choice")
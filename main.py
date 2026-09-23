import json
# Load employee data 
with open("employees.json", "r") as file:
    employees = json.load(file)

#Display all employees
def show_employees(employees):
    for person in employees:
        print(
            f"{person['name']} - Age: {person['age']} - "
            f"Salary: {person['salary']} - Active: {person['active']}"
        )

# Search for an employee by name
def find_employee(employees, name):
    for person in employees:
        if person['name'].lower() == name.lower():
            return person
    return None

# Find and display an employee's details
def find_and_display_employee(employees):
    name = input("Enter employee name: ")
    
    if not name:
        print("Name cannot be empty.")
        return

    employee = find_employee(employees, name)
    
    if employee:
        print(employee)
    
    else:
        print("Employee not found")

# Save the updated employee data
def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

# Get employee details from user input
def get_employee_details():
    name = input("Enter employee name: ")
    
    if not name:
        print("Name cannot be empty.")
        return None
    
    try:
        age = int(input("Enter employee age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return None

    try:
        salary = int(input("Enter employee salary: "))
    except ValueError:
        print("Invalid salary. Please enter a number.")
        return None

    return name, age, salary

# Add a new employee
def add_employee(employees):
    details = get_employee_details()

    if details is None:
        return

    name, age, salary = details

    if find_employee(employees, name):
            print("Employee already exists.")
            return
   
    new_employee = {
        "name": name,
        "age": age,
        "salary": salary,
        "active": True
    }
# Add the new employee to the list and save the updated data
    employees.append(new_employee)
    save_employees(employees)
    print("Employee added.")

# Remove an employee by name
def remove_employee(employees):
    name = input("Enter employee name: ")

    if not name:
        print("Name cannot be empty.")
        return

    employee = find_employee(employees, name)

    if employee:
        employees.remove(employee)
        save_employees(employees)
        print("Employee removed.")
    else:
        print("Employee not found")

# Show only active employees
def show_active_employees(employees):
    for person in employees:
        if person['active']:
            print(person['name'], person['age'], person['salary'])

# Menu function to interact with the user
def menu(employees):
    choice = ""

    while choice != "6":
        print("\n1. Show employees")
        print("2. Find employee")
        print("3. Add employee")
        print("4. Remove employee")
        print("5. Show active employees")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_employees(employees)

        elif choice == "2":
            find_and_display_employee(employees)

        elif choice == "3":
            add_employee(employees)
            
        elif choice == "4":
            remove_employee(employees)

        elif choice == "5":
            show_active_employees(employees)

        elif choice == "6":
            print("Goodbye!")

        else:
            print("Invalid choice")

menu(employees)


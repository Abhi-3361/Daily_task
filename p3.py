# Function to accept employee details and store them in a dictionary
def accept_employee_details():
    employee_details = {}

    # Accepting employee details as input from the user
    employee_details['name'] = input("Enter employee name: ")
    employee_details['no'] = input("Enter employee number: ")
    employee_details['ID'] = input("Enter employee ID: ")
    employee_details['dep'] = input("Enter department: ")
    employee_details['des'] = input("Enter designation: ")
    employee_details['DOJ'] = input("Enter date of joining (DD/MM/YYYY): ")
    employee_details['DOB'] = input("Enter date of birth (DD/MM/YYYY): ")
    employee_details['salary'] = float(input("Enter salary: "))

    return employee_details

# Function to display key, value and items from the dictionary
def display_employee_details(employee_details):
    print("\nEmployee Details:")
    
    # Display key-value pairs using a loop
    for key, value in employee_details.items():
        print(f"Key: {key}, Value: {value}")

# Main program
employee_details = accept_employee_details()  # Accept details from user
display_employee_details(employee_details)    # Display key, value, and items

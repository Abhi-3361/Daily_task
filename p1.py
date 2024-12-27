# Function to calculate the mean of marks
def calculate_mean(marks_dict):
    total_marks = sum(marks_dict.values())  # Sum of all the marks
    num_students = len(marks_dict)  # Number of students
    mean = total_marks / num_students  # Calculate mean
    return mean

# Accept student names and marks from the user
student_marks = {}

# Ask the user for how many students' data they want to enter
num_students = int(input("How many students' marks do you want to enter? "))

# Loop to accept input for student names and marks
for _ in range(num_students):
    student_name = input("Enter student name: ")
    
    while True:
        try:
            marks = float(input(f"Enter marks for {student_name}: "))
            if marks < 0:
                print("Marks cannot be negative. Please enter a valid mark.")
            else:
                student_marks[student_name] = marks
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")

# Calculate and display the mean
if student_marks:
    mean_marks = calculate_mean(student_marks)
    print(f"The mean of the marks is: {mean_marks}")
else:
    print("No student data to calculate mean.")


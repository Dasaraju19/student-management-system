students = {}
def add_student():
name = input("Enter Student Name: ")
roll_number = int(input("Enter Roll Number: "))

if roll_number in students:
print("Student with this roll number already exists.")
else:
students[roll_number] = {
'name': name,
'roll_number': roll_number,
'marks': [],
'attendance': set()
}
print("Student added successfully!")
def update_marks():
roll_number = int(input("Enter Roll Number: "))
if roll_number not in students:
print("Student not found.")
else:
marks_input = input("Enter Marks (comma-separated): ")
marks = [int(mark) for mark in marks_input.split(',')]
students[roll_number]['marks'] = marks
print("Marks updated successfully!")

def mark_attendance():
roll_number = int(input("Enter Roll Number: "))
if roll_number not in students:
print("Student not found.")
else:
date = input("Enter Attendance Date (YYYY-MM-DD): ")
students[roll_number]['attendance'].add(date)
print("Attendance recorded successfully!")
def view_student_details():
roll_number = int(input("Enter Roll Number to View Details: "))
if roll_number not in students:
print("Student not found.")
else:
student = students[roll_number]
name = student['name']
marks = student['marks']
attendance = student['attendance']
average_marks = sum(marks) / len(marks) if marks else 0
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Attendance: {attendance}")
def delete_student():
roll_number = int(input("Enter Roll Number to Delete: "))
if roll_number not in students:
print("Student not found.")

else:
del students[roll_number]
print("Student record deleted successfully!")
def menu():
while True:
print("\n--- Student Management System ---")
print("1. Add a Student")
print("2. Update Marks")
print("3. Mark Attendance")
print("4. View Student Details")
print("5. Delete a Student Record")
print("6. Exit")
choice = input("Enter your choice: ")
if choice == '1':
add_student()
elif choice == '2':
update_marks()
elif choice == '3':
mark_attendance()
elif choice == '4':
view_student_details()
elif choice == '5':
delete_student()
elif choice == '6':
print("Exiting the system. Goodbye!")
break
else:

print("Invalid choice, please try again.")
if __name__ == "__main__":
menu()

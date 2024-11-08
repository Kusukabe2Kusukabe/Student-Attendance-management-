# Initialize student list and attendance list
students = []
attendance = {}

# Main loop for user interaction
while True:
    print("\nStudent Attendance Management System")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Remove Attendance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # Add a student to the list
    if choice == "1":
        student_name = input("Enter the student's name: ")
        students.append(student_name)
        attendance[student_name] = "Absent"  # Initially mark as absent
        print(f"Student '{student_name}' added to the list.")

    # Mark attendance
    elif choice == "2":
        if not students:
            print("No students to mark attendance for.")
        else:
            print("\nMark Attendance:")
            present_students = input("Enter the names of present students (separate by space): ").split()

            # Mark selected students as present
            for student in present_students:
                if student in students:
                    attendance[student] = "Present"
                    print(f"Marked {student} as Present.")
                else:
                    print(f"Student '{student}' not found in the list.")

    # View attendance
    elif choice == "3":
        if not students:
            print("No students in the list.")
        else:
            print("\nAttendance Records:")
            for student in students:
                status = attendance.get(student, "Absent")
                print(f"{student}: {status}")

    # Remove attendance (mark as absent)
    elif choice == "4":
        if not students:
            print("No students in the list.")
        else:
            print("\nRemove Attendance:")
            students_to_remove = input("Enter the names of students to remove attendance (separate by space): ").split()

            # Mark selected students as absent
            for student in students_to_remove:
                if student in students:
                    attendance[student] = "Absent"
                    print(f"Marked {student} as Absent.")
                else:
                    print(f"Student '{student}' not found in the list.")

    # Exit the program
    elif choice == "5":
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please choose a valid option (1-5).")

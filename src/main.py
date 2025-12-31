from auth import login, signup
from dashboard import student_dashboard, faculty_dashboard

def main():
    print("\n🎓 Secure Examination Monitoring System (SEMS) v1.0")

    while True:
        print("\n1. Login")
        print("2. Signup")
        print("3. Exit")
        action = input("Choose an option: ")

        if action in ['1', '2']:
            role = input("Are you a Student or Faculty? (student/faculty): ").strip().lower()
            if role not in ["student", "faculty"]:
                print("❌ Invalid role. Please enter 'student' or 'faculty'.")
                continue

            username = input("Enter username: ")
            password = input("Enter password: ")

            if action == '1':
                success, result = login(username, password, role)
                if success:
                    print("✅ Login successful!")
                    if role == 'student':
                        student_dashboard(username)
                    else:
                        faculty_dashboard(username)
                else:
                    print("❌", result)

            elif action == '2':
                success, result = signup(username, password, role)
                if success:
                    print("✅ Signup successful! Please login to continue.")
                else:
                    print("❌", result)

        elif action == '3':
            print("👋 Exiting SEMS. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

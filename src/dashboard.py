from cheat_detection import start_monitoring_session
from marks import update_student_marks, view_student_marks
from notifications import save_notification, show_notifications
from heatmap import generate_heatmap
from export import export_to_csv, export_to_pdf
from feedback import submit_feedback
from hash_check import initialize_hashes, check_file_integrity

def student_dashboard(username):
    while True:
        print(f"\n🎓 Welcome, {username} [STUDENT]")
        print("1. View Marks")
        print("2. View Notifications")
        print("3. Submit Anonymous Feedback")
        print("4. Logout")

        choice = input(">> ")
        if choice == '1':
            view_student_marks(username)
        elif choice == '2':
            show_notifications()
        elif choice == '3':
            submit_feedback()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

def faculty_dashboard(username):
    while True:
        print(f"\n🧑‍🏫 Welcome, {username} [FACULTY]")
        print("1. Update Student Marks")
        print("2. Post Notification")
        print("3. Start Cheating Detection (AI)")
        print("4. Generate Suspicion Heatmap")
        print("5. Export Suspicion Report (CSV)")
        print("6. Export Suspicion Report (PDF)")
        print("7. Logout")
        print("8. Initialize File Hashes")
        print("9. Check for File Tampering")

        choice = input(">> ")
        if choice == '1':
            student = input("Enter student username: ").strip()
            subject = input("Enter subject name: ").strip()
            score = input("Enter score: ").strip()
            try:
                score = float(score)
                update_student_marks(student, subject, score)
                print("✅ Marks updated successfully.")
            except ValueError:
                print("❌ Invalid score.")
        elif choice == '2':
            message = input("Enter the notification message: ").strip()
            save_notification(message, username)
            print("✅ Notification posted successfully.")
        elif choice == '3':
            mins = input("⏱️ Enter monitoring duration in minutes (default = 1): ")
            try:
                start_monitoring_session(int(mins))
            except:
                start_monitoring_session()
        elif choice == '4':
            generate_heatmap()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            export_to_pdf()
        elif choice == '7':
            break
        elif choice == '8':
            initialize_hashes()
        elif choice == '9':
            check_file_integrity()
        else:
            print("❌ Invalid choice.")

from datetime import datetime
import os

FEEDBACK_FILE = '../data/feedback.txt'

def submit_feedback():
    feedback = input("Enter your anonymous feedback (or 'exit' to cancel): ").strip()
    if feedback.lower() == 'exit':
        return
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(FEEDBACK_FILE, 'a') as f:
        f.write(f"[{timestamp}] {feedback}\n")
    print("✅ Feedback submitted anonymously.")

import json
import os
from datetime import datetime

NOTIF_FILE = '../data/notifications.json'

def save_notification(message, faculty_name):
    notif = {
        "message": message,
        "faculty": faculty_name,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    if os.path.exists(NOTIF_FILE):
        with open(NOTIF_FILE, 'r') as f:
            try:
                notifications = json.load(f)
                if not isinstance(notifications, list):
                    notifications = []
            except:
                notifications = []
    else:
        notifications = []

    notifications.append(notif)

    with open(NOTIF_FILE, 'w') as f:
        json.dump(notifications, f, indent=4)

def show_notifications():
    if not os.path.exists(NOTIF_FILE):
        print("No notifications yet.")
        return

    with open(NOTIF_FILE, 'r') as f:
        notifications = json.load(f)
        for n in reversed(notifications[-5:]):
            print(f"[{n['timestamp']}] {n['faculty']}: {n['message']}")

import json
import os
from hashing import hash_password, verify_password

USERS_FILE = '../data/users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def signup(username, password, role):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    hashed = hash_password(password)
    users[username] = {"password": hashed, "role": role}
    save_users(users)
    return True, None

def login(username, password, role):
    users = load_users()
    if username in users:
        stored_hash = users[username]['password']
        stored_role = users[username]['role']
        if stored_role != role:
            return False, "Role mismatch. Are you logging in with the right role?"
        if verify_password(password, stored_hash):
            return True, None
        else:
            return False, "Incorrect password."
    return False, "Username not found."

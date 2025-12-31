import os
import json
import hashlib

HASH_FILE = '../data/file_hashes.json'
WATCHED_FILES = [
    '../data/marks.json',
    '../data/notifications.json',
    '../data/suspicion_log.json'
]

def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def initialize_hashes():
    hashes = {}
    for file in WATCHED_FILES:
        if os.path.exists(file):
            hashes[file] = calculate_file_hash(file)
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)
    print("✅ File hashes initialized.")

def check_file_integrity():
    if not os.path.exists(HASH_FILE):
        print("⚠️ Hash file not found.")
        return
    with open(HASH_FILE, 'r') as f:
        saved_hashes = json.load(f)
    tampered = False
    for file, original_hash in saved_hashes.items():
        if os.path.exists(file):
            current_hash = calculate_file_hash(file)
            if current_hash != original_hash:
                print(f"🚨 Tampering detected: {file}")
                tampered = True
    if not tampered:
        print("✅ All files are intact.")

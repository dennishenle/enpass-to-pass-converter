#!/usr/bin/env python3
"""
Script to convert Enpass passwords to pass (Linux password manager)
"""

import json
import subprocess
import sys
import os
from pathlib import Path

def load_enpass_json(file_path):
    """Load and parse the Enpass JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)

def get_password_field(fields):
    """Extract password value from fields list"""
    for field in fields:
        if field.get('type') == 'password' and field.get('value'):
            return field['value']
    return None

def get_username_field(fields):
    """Extract username value from fields list"""
    # First, try to find explicit username field
    for field in fields:
        if field.get('type') == 'username' and field.get('value'):
            return field['value']

    # If no username field, try to find email field as fallback
    for field in fields:
        if field.get('type') == 'email' and field.get('value'):
            return field['value']

    return None

def get_title(item):
    """Get title for the password entry"""
    return item.get('title', 'Untitled')

def add_to_pass(entry_name, fields_data, note_data):
    """Add password to pass manager with all fields"""
    try:
        # Create the password entry with pass
        cmd = ['pass', 'insert', '-m', entry_name]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Build the entry content with all fields
        password_entry = ""
        for field in fields_data:
            if field.get('label') and field.get('value'):
                password_entry += f"{field['label']}: {field['value']}\n"

        # Add note field if it exists
        if note_data and note_data.strip():
            password_entry += f"Note: {note_data}\n"

        # Add a newline at the end
        password_entry = password_entry.rstrip() + "\n"

        stdout, stderr = process.communicate(input=password_entry)

        if process.returncode == 0:
            print(f"✓ Added: {entry_name}")
            return True
        else:
            print(f"✗ Failed to add {entry_name}: {stderr}")
            return False
    except Exception as e:
        print(f"✗ Error adding {entry_name}: {e}")
        return False

def main():
    """Main function to convert Enpass passwords to pass"""
    # Check if pass is installed
    try:
        subprocess.run(['pass', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: pass command not found. Please install pass (the password manager).")
        sys.exit(1)

    # Load the Enpass JSON file
    json_file = 'pass.json'
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found")
        sys.exit(1)

    try:
        data = load_enpass_json(json_file)
    except Exception as e:
        print(f"Error reading {json_file}: {e}")
        sys.exit(1)

    # Process items
    items = data.get('items', [])
    total_items = len(items)
    successful_adds = 0
    not_saved_items = 0

    print(f"Processing {total_items} items from {json_file}")

    for item in items:
        # Get title for the entry
        title = get_title(item)

        # Get note field
        note = item.get('note', '')

        # Add to pass with all fields
        if add_to_pass(title, item.get('fields', []), note):
            successful_adds += 1
        else:
            print(f"⚠ Failed to save: {title}")
            not_saved_items += 1

    print(f"\nConversion complete: {successful_adds}/{total_items} items processed")
    if not_saved_items > 0:
        print(f"Warning: {not_saved_items} items were not saved")

if __name__ == "__main__":
    main()
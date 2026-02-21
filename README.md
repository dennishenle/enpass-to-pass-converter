# Enpass to Pass Converter

This script converts passwords from an Enpass JSON export to the pass (Linux password manager).

## Usage

1. Export your passwords from Enpass as JSON
2. Run the script with the path to your Enpass JSON file:
   ```bash
   python main.py /path/to/enpass_export.json
   ```

## Requirements

- Python 3.13+
- pass (Linux password manager) installed and configured

## Features

- Automatically detects login items in the Enpass export
- Extracts passwords and usernames (uses email fields as usernames when no explicit username field exists)
- Adds entries to pass with the item title as the entry name
- Skips items without passwords
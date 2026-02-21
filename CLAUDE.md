# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python script that converts passwords from an Enpass JSON export to the pass (Linux password manager). The tool processes Enpass login items and adds them to the pass password manager.

## Key Files

- `main.py`: The main script that handles the conversion process
- `test_setup.py`: Test setup script that creates sample Enpass JSON data for testing
- `pass.json`: Sample Enpass export file (not included in repo, must be provided by user)
- `pyproject.toml`: Project configuration file

## How to Run

1. Export your passwords from Enpass as JSON
2. Place the exported JSON file as `pass.json` in this directory
3. Run the script:
   ```bash
   python main.py
   ```

## Development Commands

- Run the main script: `python main.py`
- Run tests: `python test_setup.py` (creates test data) then `python main.py`
- The script requires Python 3.13+ and the pass password manager to be installed and configured

## Code Architecture

The script follows a straightforward architecture:
1. `load_enpass_json()` - Loads and parses the Enpass JSON file
2. `get_password_field()` - Extracts password values from fields
3. `get_username_field()` - Extracts username values, falling back to email fields
4. `add_to_pass()` - Adds entries to the pass password manager using subprocess
5. `main()` - Main function that orchestrates the conversion process

The script specifically targets 'login' category items from Enpass and handles both explicit username fields and fallback to email fields when no username is present.
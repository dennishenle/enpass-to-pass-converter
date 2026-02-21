#!/usr/bin/env python3
"""
Test script for the enpass2pass converter
"""

import json
import os

# Create a simple test JSON structure
test_data = {
    "folders": [
        {
            "icon": "1008",
            "parent_uuid": "",
            "title": "Test Folder",
            "updated_at": 1587457235,
            "uuid": "4221c8b8-2658-438e-a278-e284cb03d77f"
        }
    ],
    "items": [
        {
            "archived": 0,
            "auto_submit": 1,
            "category": "login",
            "category_name": "Login",
            "createdAt": 1533802643,
            "favorite": 0,
            "field_updated_at": 1686648460,
            "fields": [
                {
                    "deleted": 0,
                    "label": "Benutzername",
                    "order": 1,
                    "sensitive": 0,
                    "type": "username",
                    "uid": 10,
                    "updated_at": 1533802814,
                    "value": "testuser",
                    "value_updated_at": 1533802814
                },
                {
                    "deleted": 0,
                    "label": "Passwort",
                    "order": 3,
                    "sensitive": 1,
                    "type": "password",
                    "uid": 11,
                    "updated_at": 1666724743,
                    "value": "testpassword123",
                    "value_updated_at": 1533802643
                }
            ],
            "icon": {
                "fav": "",
                "image": {
                    "file": "web/test.com"
                },
                "type": 1,
                "uuid": ""
            },
            "note": "",
            "subtitle": "testuser",
            "template_type": "login.default",
            "title": "Test Website With Username",
            "trashed": 0,
            "updated_at": 1707593446,
            "uuid": "D9517A7C-8986-475C-A088-6FD7720C5D4A"
        },
        {
            "archived": 0,
            "auto_submit": 1,
            "category": "login",
            "category_name": "Login",
            "createdAt": 1533802643,
            "favorite": 0,
            "field_updated_at": 1686648460,
            "fields": [
                {
                    "deleted": 0,
                    "label": "E-Mail",
                    "order": 2,
                    "sensitive": 0,
                    "type": "email",
                    "uid": 12,
                    "updated_at": 1533802814,
                    "value": "testuser2@example.com",
                    "value_updated_at": 1533802814
                },
                {
                    "deleted": 0,
                    "label": "Passwort",
                    "order": 3,
                    "sensitive": 1,
                    "type": "password",
                    "uid": 11,
                    "updated_at": 1666724743,
                    "value": "testpassword456",
                    "value_updated_at": 1533802643
                }
            ],
            "icon": {
                "fav": "",
                "image": {
                    "file": "web/test2.com"
                },
                "type": 1,
                "uuid": ""
            },
            "note": "",
            "subtitle": "testuser2@example.com",
            "template_type": "login.default",
            "title": "Test Website With Email",
            "trashed": 0,
            "updated_at": 1707593446,
            "uuid": "D9517A7C-8986-475C-A088-6FD7720C5D4B"
        }
    ]
}

# Write test data to file
with open('test_pass.json', 'w') as f:
    json.dump(test_data, f, indent=2)

print("Created test_pass.json file for verification")
print("You can now run: python main.py")
#A simple program to save data in a file and then read it
import json
from json.decoder import JSONDecodeError

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except (FileNotFoundError,JSONDecodeError): #If file is empty, Python will throw JSONDecodeError, need to handle that and FileNotFoundError both.
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username:"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

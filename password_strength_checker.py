# importing re will be used to check for password requirements.
# Update: We removed getpass, GUI will handle the password "hide" instead.
import re

import random # We will use the random library to randomly select characters for the password.


# List of common passwords to avoid. Found using sources from NordPass.
common_passwords = ["123456", "admin", "12345678", "123456789", "12345", 
                    "password", "Aa123456", "Pass@123", "admin123"]

# Create list's the contain different characters to be used in the password generator function.
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*"

def check_strength(password):
    # Counter variable to keep track of password strength score.
    counter = 0

    # Update: Created a dictionary called results to store results of each password 
    # requirement check. This will be used in the UI to display which requirements
    # were met and which were not. This is also to make our UI look nicer and more
    # informative to the user (me).

    results = {
        "length_8": False,
        "length_12": False,
        "has_upper": False,
        "has_lower": False,
        "has_number": False,
        "has_special": False
    }

    # REMOVED PASSWORD INPUT, GUI will handle this instead. 

    # ---- Statements Below Will Check for Password Strength ----

    # If found in common passwords, exit.
    if password in common_passwords:
        return 0, "Too Common", "red", results
    

    # Check for length. If less than 8, exit, else, do the other checks.
    if len(password) >= 12:
        counter+=2
        results["length_12"] = True
        results["length_8"] = True
    elif 8 <= len(password) < 12:
        counter+=1
        results["length_8"] = True
    else:
        return 0, "Too Short", "red", results

    # Check password for numbers.

    if re.search(r'\d', password):
        counter+=1
        results["has_number"] = True

    # Check password for capital letters

    if re.search(r"[A-Z]", password):
        counter+=1
        results["has_upper"] = True

    # Check password for lowercase letters

    if re.search(r"[a-z]", password):
        counter+=1
        results["has_lower"] = True

    # Check password for special characters
    if re.search(r"[!@#$%^&*]", password):
        counter+=1
        results["has_special"] = True

    # ---- Statements Below Will Report Password Strengh 0-6 ----

    # Change here: We will return counter, rating, and color instead of printing.
    # This is so that the UI can use information instead of just printing it to the 
    # console.

    if counter == 6:
        rating = "Very Secure"
        color = "green"
    elif 4 <= counter <= 5:
        rating = "Secure"
        color = "yellow"
    elif 2 <= counter <= 3:
        rating = "Moderate"
        color = "orange"
    else:
        rating = "Weak"
        color = "red"

    return counter, rating, color, results


# Create a function to generate a random password. This will be used in the UI too!
# NOTE: These passwords will be RANDOMLY generated, meaning it won't follow your typical
# password for example: "Password123!" but it will be something like "aB3$eFgH". This is to ensure that
# the generated password is as secure as possible and not easily guessable. The user can then use this
# generated password as a base and modify it to their liking if they want to. 
# This is just to give them a starting point, or can be used as is if they want a completely random password.

def generatePassword():
    password_length = 16 # Password will be 16 characters long, very secure.
    password = ""

    # Ensure password contains at least one of each char type to meet requirements.
    password += random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(numbers)
    password += random.choice(special_characters)

    # Create a string that combines all characters to choose from for remaining characters in password.
    all_chars = lowercase_letters + uppercase_letters + numbers + special_characters

    for i in range(password_length - 4): # We already added 4 characters, so we need to add 12 more.
        password += random.choice(all_chars)

    password_list = list(password) # Convert password string to a list to shuffle it.
    random.shuffle(password_list) # Shuffle the list to ensure randomness.
    password = ''.join(password_list) # Convert list back to string.

    return password

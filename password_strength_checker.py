# importing re will be used to check for password requirements.
# Update: We removed getpass, GUI will handle the password "hide" instead.
import re

# List of common passwords to avoid. Found using sources from NordPass.
common_passwords = ["123456", "admin", "12345678", "123456789", "12345", 
                    "password", "Aa123456", "Pass@123", "admin123"]

def check_strength(password):
    # Counter variable to keep track of password strength score.
    counter = 0

    # REMOVED PASSWORD INPUT, GUI will handle this instead. 

    # ---- Statements Below Will Check for Password Strength ----

    # If found in common passwords, exit.
    if password in common_passwords:
        return 0, "Too Common", "red"


    # Check for length. If less than 8, exit, else, do the other checks.
    if len(password) >= 12:
        counter+=2
    elif 8 <= len(password) < 12:
        counter+=1
    else:
        return 0, "Too Short", "red"

    # Check password for numbers.

    if re.search(r'\d', password):
        counter+=1

    # Check password for capital letters

    if re.search(r"[A-Z]", password):
        counter+=1

    # Check password for lowercase letters

    if re.search(r"[a-z]", password):
        counter+=1

    # Check password for special characters
    if re.search(r"[!@#$%^&*]", password):
        counter+=1

    # ---- Statements Below Will Report Password Strengh 0-6 ----

    # Change here: We will return counter, rating, and color instead of printing.
    # This is so that the UI can use information instead of just printing it to the 
    # console.

    if counter == 6:
        rating = "Very Secure"
        color = "green"
    elif 4 <= counter <= 5:
        rating = "Secure"
        color = "blue"
    elif 2 <= counter <= 3:
        rating = "Moderate"
        color = "orange"
    else:
        rating = "Weak"
        color = "red"

    return counter, rating, color

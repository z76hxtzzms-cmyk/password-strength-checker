# Import both getpass module and re module. getpass will be used to hide user input,
# and re will be used to check for password requirements.
import getpass
import re

# List of common passwords to avoid. Found using sources from NordPass.
common_passwords = ["123456", "admin", "12345678", "123456789", "12345", 
                    "password", "Aa123456", "Pass@123", "admin123"]

# Counter variable to keep track of password strength score.
counter = 0

# Ask user for password. The getpass module will hide the input for security reasons.
password = getpass.getpass("Enter Password: ")

# ---- Statements Below Will Check for Password Strength ----

# If found in common passwords, exit.
if password in common_passwords:
    print("The password you entered is too common. Please choose a stronger password.")
    exit()


# Check for length. If less than 8, exit, else, do the other checks.
if len(password) >= 12:
    counter+=2
elif 8 <= len(password) < 12:
    counter+=1
else:
    print("The password you entered is too short. Please choose a stronger password.")
    exit()

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

print("Password Strength Results")
print("Password Strength Score: ", counter)
if counter == 6:
    print("Your password is very strong.")
elif 4 <= counter <= 5:
    print("Your password is strong.")
elif 2 <= counter < 3:
    print("Your password is moderate.")
else:
    print("Your password is weak.")
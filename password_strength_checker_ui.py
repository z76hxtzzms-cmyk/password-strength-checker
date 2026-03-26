# Password Strength Checker UI
import tkinter as tk
# Import the check_password_strength function from password_strength_checker.py
# THIS IS CRUICAL: We need to import the function so that we can get our password 
# strength score and rating to display in the UI.
import password_strength_checker

# Function to get password from the user_input entry
def check_password():
    password = user_input.get()  # Store given password into variable password.
    # This will call the check_strength function in password_strength_checker
    # and then store the returned values into its respective variables.
    score, rating, color = password_strength_checker.check_strength(password) 
    # Update the result_label with the password strength rating and color.
    result_label.config(text=f"Result: {rating} (Score: {score}/6)", fg=color)

window = tk.Tk()
# Set the title and size of the window
# Should display a window when run.
window.title("Password Strength Checker")
window.geometry("400x500")

# Create a label called title_label and add it to the window. This will be the title of the UI.
title_label = tk.Label(window, text = "Enter Password Below")
title_label.pack(pady=10)   # Add some vertical spacing around title_label

# Create an entry widget called user_input and add it to window. 
# NEW: show="*" will hide the input! New to me!
user_input = tk.Entry(window, show="*")  
user_input.pack(pady=10)    

button = tk.Button(window, text = "Check Strength", command=check_password) 
button.pack(pady=10)

result_label = tk.Label(window)
result_label.pack(pady=10)

# Start the window's event loop
# Keeps it open until the user closes, then terminates the program.
window.mainloop()
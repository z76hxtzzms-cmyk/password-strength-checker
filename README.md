# Password Strength checker

This mini python desktop application analyzes password strength in real time using regex pattern matching and security best practices.

This was build as part of my cybersecurity learning journey as a first-year CIS student at Cal Poly Pomona. 


# Screenshot

![Password Strength Checker](screenshot.png)

# Features

- Real time password strength analysis that scores password out 0 -> 6
- Checks for uppercase, lowercase, numbers, and special characters. This showcases best practices.
- Bonous scoring for passwords that are longer (12 + characters)
- Blocklist check against top most common passwords based on NordPass
- Dark mode GUI built using Tkinter for a more "professional" look
- Color coded checklist showing exactly what requirements passed and which failed.
- Secure password input - Characters are hidden while typing.

# Technologies used
- **Python 3** - Core programming language
-**Tkinter** - Built-in Python Library for the desktop GUI
- **re (Regex)** - Pattern matching for password rule validation
- **getpass** - Secure password input, this was removed after GUI was implemented.

## How to Run

1. Make sure Python 3 is installed on your machine
2. Clone this repository:
```
   git clone https://github.com/z76hxtzzms-cmyk/password-strength-checker.git
```
3. Navigate into the project folder:
```
   cd password-strength-checker
```
4. Run the GUI application:
```
   python password_strength_checker_gui.py
```
5. Or run the command line version:
```
   python password_strength_checker.py
```

> No external libraries required — everything uses Python's standard library!

## Project Structure
password-strength-checker/
│── password_strength_checker.py      # Core logic — strength analysis engine
│── password_strength_checker_gui.py  # Tkinter GUI — dark mode desktop app
│── README.md
│── screenshot.png

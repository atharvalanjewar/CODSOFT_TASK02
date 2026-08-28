# CODSOFT_TASK02
# Password Generator Application

A command-line application built in Python that generates strong, random 
passwords based on a user-specified length, with an option to include 
custom characters.

## Features
- Prompts the user for the desired password length
- Generates a password using a mix of letters, digits, and symbols
- Allows the user to optionally include their own custom characters in the password
- Displays the generated password on the screen

## Technologies Used
- Python 3.x
- `random` module
- `string` module

## How to Run
1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the file.
3. Run the application:
   ```bash
   python password_generator.py
   ```
4. Enter the desired password length when prompted.
5. Optionally enter any custom characters you'd like included, or press Enter to skip.

## How It Works
- The user specifies how long the password should be.
- A base character pool is built using letters, digits, and symbols (`string.ascii_letters`, `string.digits`, `string.punctuation`).
- Any custom characters entered by the user are added to this pool.
- Random characters are picked from the combined pool to build the password.
- The final password is printed to the screen.

## Future Improvements
- Add a password strength indicator
- Add input validation for zero or negative lengths
- Add option to generate and save multiple passwords at once

## Author
Atharva Lanjewar

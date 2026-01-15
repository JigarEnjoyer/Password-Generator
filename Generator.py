import random
import string
from tkinter import messagebox # For popup messages

class PasswordGenerator:
    def __init__(self, length=12, useUppercase = True, useLowercase = True, useNums = True, useSymbols = True, excludeAmbiguous = False, minSymbolLength = 1, minNumLength = 1):
        self.length = length # Password length
        self.useUppercase = useUppercase # Uppercase letters
        self.useLowercase = useLowercase # Lowercase letters
        self.useNums = useNums # Numbers
        self.useSymbols = useSymbols # Symbols like !, @, #, etc.
        self.excludeAmbiguous = excludeAmbiguous # Exclude ambiguous characters like {}, [], (), etc.
        self.minSymbolLength = minSymbolLength # Minimum number of symbols
        self.minNumLength = minNumLength # Minimum number of numbers

    def generate(self):
        allChars = "" # Initialize empty character pool
        ambiguousChars = "{}[]()/\'\"`~,;:.<>" # Define ambiguous characters

        # If a user picks an option, add those characters to the pool
        if self.useUppercase:
            allChars += string.ascii_uppercase # Add uppercase letters
        if self.useLowercase:
            allChars += string.ascii_lowercase # Add lowercase letters
        if self.useNums:
            allChars += string.digits # Add numbers
        if self.useSymbols:
            allChars += string.punctuation # Add symbols

        if self.excludeAmbiguous:
            allChars = ''.join(c for c in allChars if c not in ambiguousChars) # Remove ambiguous characters

        # Ensure there is at least one character type selected
        if not allChars:
            messagebox.showerror("Error", "No character types selected for password generation.")
            return None

        password = [] # Initialize empty password list
        
        # Add user defined minimum number of special characters
        if self.minSymbolLength > 0:
            if self.useSymbols == False:
                messagebox.showerror("Error", "Minimum symbols specified but 'Include Symbols' option is not selected.") # Show error if symbols not selected but min symbols > 0
                return None
            elif self.excludeAmbiguous: # Exclude ambiguous characters if option is selected
                    filteredSymbols = ''.join(c for c in string.punctuation if c not in ambiguousChars)
                    password.extend(random.choice(filteredSymbols) for _ in range(self.minSymbolLength))
            else:
                password.extend(random.choice(string.punctuation) for _ in range(self.minSymbolLength)) # Add symbols
        
        # Add user defined minimum number of digits
        if self.minNumLength > 0:
            if self.useNums == False:
                messagebox.showerror("Error", "Minimum numbers specified but 'Include Numbers' option is not selected.") # Show error if numbers not selected but min numbers > 0
                return None
            else:
                password.extend(random.choice(string.digits) for _ in range(self.minNumLength))

        # Fill the rest of the password length with random choices from the pool
        remainingLength = self.length - len(password)
        if remainingLength > 0:
            password.extend(random.choice(allChars) for _ in range(remainingLength))
        
        # Shuffle the password list to ensure randomness
        random.shuffle(password)
        
        # Convert list to string and return
        return ''.join(password)
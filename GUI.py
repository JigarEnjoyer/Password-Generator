import tkinter as tk
from tkinter import messagebox
import pyperclip # For clipboard operations
from Generator import PasswordGenerator

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")  # Set the window title

        # Password length
        tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.lengthVar = tk.IntVar(value=12)
        tk.Spinbox(root, from_=4, to=64, textvariable=self.lengthVar).grid(row=0, column=1, padx=10, pady=5)

        # Uppercase option
        self.useUppercaseVar = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.useUppercaseVar).grid(row=1, columnspan=2, sticky='w', padx=10, pady=5)

        # Lowercase option
        self.useLowercaseVar = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.useLowercaseVar).grid(row=2, columnspan=2, sticky='w', padx=10, pady=5)

        # Numbers option
        self.useNumsVar = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Numbers", variable=self.useNumsVar).grid(row=3, columnspan=2, sticky='w', padx=10, pady=5)

        # Symbols option
        self.useSymbolsVar = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Symbols", variable=self.useSymbolsVar).grid(row=4, columnspan=2, sticky='w', padx=10, pady=5)

        # Exclude ambiguous characters option
        self.excludeAmbiguousVar = tk.BooleanVar(value=False)
        tk.Checkbutton(root, text="Exclude Ambiguous Characters", variable=self.excludeAmbiguousVar).grid(row=5, columnspan=2, sticky='w', padx=10, pady=5)

        # Minimum numbers label and option
        tk.Label(root, text="Minimum Numbers:").grid(row=6, column=0, sticky='w', padx=10, pady=5)
        self.minNumVar = tk.IntVar(value=0)
        tk.Spinbox(root, from_=0, to=10, textvariable=self.minNumVar).grid(row=6, column=1, padx=10, pady=5)

        # Minimum symbols label and option
        tk.Label(root, text="Minimum Symbols:").grid(row=7, column=0, sticky='w', padx=10, pady=5)
        self.minSymbolVar = tk.IntVar(value=0)
        tk.Spinbox(root, from_=0, to=10, textvariable=self.minSymbolVar).grid(row=7, column=1, padx=10, pady=5)

        # Password display
        self.passwordVar = tk.StringVar()

        # Create an Entry widget for password display
        self.passwordDisplay = tk.Entry(root, textvariable=self.passwordVar, width=50, relief="solid", state="readonly")
        self.passwordDisplay.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        # Generate password button
        tk.Button(root, text="Generate Password", command=self.generatePassword).grid(row=9, columnspan=2, pady=10)

        # Copy password button
        tk.Button(root, text="Copy to Clipboard", command=self.copyToClipboard).grid(row=10, columnspan=2, pady=10)

    def generatePassword(self):
        # Collect user input values from the GUI
        length = self.lengthVar.get()
        useUppercase = self.useUppercaseVar.get()
        useLowercase = self.useLowercaseVar.get()
        useNums = self.useNumsVar.get()
        useSymbols = self.useSymbolsVar.get()
        excludeAmbiguous = self.excludeAmbiguousVar.get()
        minSymbolLength = self.minSymbolVar.get()
        minNumLength = self.minNumVar.get()

        # Create an instance of PasswordGenerator
        passwordGenerator = PasswordGenerator(
            length=length,
            useUppercase=useUppercase,
            useLowercase=useLowercase,
            useNums=useNums,
            useSymbols=useSymbols,
            excludeAmbiguous=excludeAmbiguous,
            minSymbolLength=minSymbolLength,
            minNumLength=minNumLength
        )

        # Generate the password using generate function from Generator.py
        generatedPassword = passwordGenerator.generate()

        # Display the generated password in the Entry widget
        if generatedPassword:
            self.passwordVar.set(generatedPassword)
            messagebox.showinfo("Generated Password", f"Your generated password is: {generatedPassword}")
        else:
            messagebox.showerror("Error", "Password generation failed. Please check your settings.")

    def copyToClipboard(self):
        # Copy the current password to clipboard if one exists
        password = self.passwordVar.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Password Copied", "The password has been copied to your clipboard.")
        else:
            messagebox.showwarning("No Password", "Please generate a password first.")
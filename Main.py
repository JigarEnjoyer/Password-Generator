import tkinter as tk
from GUI import PasswordGeneratorGUI  # Import the GUI class

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)  # Create an instance of the GUI
    root.mainloop()  # Start the Tkinter app
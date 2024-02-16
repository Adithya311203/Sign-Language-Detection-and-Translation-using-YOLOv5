import tkinter as tk
from tkinter import filedialog
import subprocess

def execute_exe():
    file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if file_path:
        try:
            subprocess.run([file_path])
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="No file selected.")

# Create the main window
app = tk.Tk()
app.title("Executable Runner")

# Create a button to choose an executable file
choose_file_button = tk.Button(app, text="Choose Executable", command=execute_exe)
choose_file_button.pack(pady=10)

# Display the result or error
result_label = tk.Label(app, text="")
result_label.pack()

# Start the GUI event loop
app.mainloop()

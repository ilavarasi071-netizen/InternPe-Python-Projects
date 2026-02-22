import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.configure(bg="black")

# Create clock label
clock_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="cyan"
)

clock_label.pack(expand=True)

# Start updating time
update_time()

# Run the application
root.mainloop()

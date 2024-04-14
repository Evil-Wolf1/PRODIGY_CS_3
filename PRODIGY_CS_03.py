import re
import tkinter as tk
import tkinter.ttk as ttk

def check_password_strength(password):
    # Criteria flags
    length_flag = len(password) >= 8
    uppercase_flag = bool(re.search(r'[A-Z]', password))
    lowercase_flag = bool(re.search(r'[a-z]', password))
    number_flag = bool(re.search(r'\d', password))
    special_char_flag = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))

    # Assess strength based on flags
    if length_flag and uppercase_flag and lowercase_flag and number_flag and special_char_flag:
        return "Strong: Password meets all criteria."
    elif length_flag and (uppercase_flag or lowercase_flag) and number_flag:
        return "Moderate: Password meets most criteria but lacks special characters."
    else:
        return "Weak: Password does not meet minimum complexity requirements."

def update_strength(event=None):
    password = password_entry.get()

    # Update feedback message
    strength_feedback = check_password_strength(password)
    feedback_label.config(text=strength_feedback)

    # Update progress bar
    strength = calculate_strength(password)
    progress_bar['value'] = strength

    # Change progress bar color based on strength
    if strength >= 80:
        progress_bar_style = 'green.Horizontal.TProgressbar'
    elif strength >= 40:
        progress_bar_style = 'orange.Horizontal.TProgressbar'
    else:
        progress_bar_style = 'red.Horizontal.TProgressbar'

    s = ttk.Style()
    s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
    s.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

    progress_bar.configure(style=progress_bar_style)

def calculate_strength(password):
    # Calculate password strength
    criteria_met = [
        len(password) >= 8,
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))
    ]
    criteria_count = sum(criteria_met)
    return (criteria_count / 5) * 100

def toggle_password_visibility():
    # Toggle password visibility
    if password_entry['show'] == '*':
        password_entry.config(show='')
        show_hide_button.config(text='Hide')
    else:
        password_entry.config(show='*')
        show_hide_button.config(text='Show')

# Create GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=0, column=1, padx=10, pady=5)

# Show/Hide password button
show_hide_button = tk.Button(root, text="Show", command=toggle_password_visibility)
show_hide_button.grid(row=0, column=2, padx=5, pady=5)

# Progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=200)
progress_bar.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Feedback label
feedback_label = tk.Label(root, text="", fg='black')
feedback_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Update password strength on key release
password_entry.bind('<KeyRelease>', update_strength)

root.mainloop()

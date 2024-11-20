import tkinter as tk
import re

def check_password_strength():
    
    password = password_entry.get()
    
    length_criteria = len(password)  >= 8
    
    digit_criteria = bool(re.search(r"\d", password))
    
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    
    symbol_criteria = bool(re.search(r"[!@#$%%^&*(),.?\:{|<>}]", password))
    
    criteria_met = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, symbol_criteria])
    
    

    if criteria_met <= 2:
        strength = "Weak"
        
    elif criteria_met == 3 or criteria_met == 4:
        strength = "Medium"
        
    else:
        strength = "Strong"
        
    result_label.config(text=f"Password strength: {strength}")
    

root = tk.Tk()
root.title("Password strength checker")
root.geometry("300x200")

password_label = tk.Label(root, text="Enter password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check strength", command=check_password_strength)

check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
import tkinter as tk

def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm / 30.48
        result_label.config(text=f"{feet:.2f} feet")
    except ValueError:
        result_label.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label.config(text=f"{inches:.2f} inches")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_sqm():
    try:
        sqft = float(sqft_entry.get())
        sqm = sqft / 10.764
        result_label.config(text=f"{sqm:.2f} square meters")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_hectare_acres():
    try:
        sqft = float(sqft_to_ha_entry.get())
        hectares = sqft / 107639.104
        acres = sqft / 43560
        result_label.config(text=f"{hectares:.2f} hectares\n{acres:.2f} acres")
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Unit Conversion")

# Configure the background color and GUI elements' shape
root.configure(bg="#f0f0f0")  

# Labels and entry widgets
tk.Label(root, text="Centimeter to Feet:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=cm_to_feet, bg="#4caf50", fg="white", relief=tk.RAISED).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Feet to Inches:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=feet_to_inches, bg="#2196f3", fg="white", relief=tk.RAISED).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Sqft to Sqm:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_sqm, bg="#ff9800", fg="white", relief=tk.RAISED).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Sqft to Hectare/Acres:", bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5)
sqft_to_ha_entry = tk.Entry(root)
sqft_to_ha_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_hectare_acres, bg="#e91e63", fg="white", relief=tk.RAISED).grid(row=3, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", bg="#f0f0f0")
result_label.grid(row=4, columnspan=3, padx=5, pady=5)

root.mainloop()

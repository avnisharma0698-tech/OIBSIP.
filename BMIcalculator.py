from tkinter import *

def calculate():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = round(weight / (height * height), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result.config(text=f"{name_entry.get()}\nBMI: {bmi}\nCategory: {category}")

root = Tk()
root.title("BMI Calculator")
root.geometry("350x350")

Label(root, text="BMI Calculator", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Weight (kg)").pack()
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Height (m)").pack()
height_entry = Entry(root)
height_entry.pack()

Button(root, text="Calculate BMI", command=calculate).pack(pady=10)

result = Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

root.mainloop()
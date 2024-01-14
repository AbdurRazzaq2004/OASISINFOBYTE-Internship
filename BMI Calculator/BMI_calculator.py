import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

# Define BMI categories and ranges
bmi_categories = {
    "Underweight": (0, 18.5),
    "Normal Weight": (18.5, 24.9),
    "Overweight": (25, 29.9),
    "Obese": (30, float("inf"))
}

# Create a BMI Calculator GUI class
class BMICalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        
        # Create labels and entry fields
        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_entry = tk.Entry(self)
        
        self.height_label = tk.Label(self, text="Height (m):")
        self.height_entry = tk.Entry(self)
        
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_bmi)
        
        # Arrange labels, entry fields, and button using grid layout
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.height_label.grid(row=1, column=0, padx=10, pady=10)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
    def calculate_bmi(self):
        # Get weight and height inputs
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
            return
        
        # Validate inputs within reasonable ranges
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Invalid input. Please enter positive values.")
            return
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Classify BMI into categories
        category = ""
        for key, value in bmi_categories.items():
            if value[0] <= bmi < value[1]:
                category = key
                break
        
        # Display BMI result in a message box
        messagebox.showinfo("BMI Result", f"Your BMI: {bmi:.2f}\nCategory: {category}")
        
        # Store BMI data
        self.store_bmi_data(weight, height, bmi, category)
        
    def store_bmi_data(self, weight, height, bmi, category):
        # Store data in a CSV file
        with open("bmi_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([weight, height, bmi, category])
        
    def visualize_bmi_data(self):
        # Read BMI data from CSV file
        weights = []
        heights = []
        bmis = []
        categories = []
        with open("bmi_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                weights.append(float(row[0]))
                heights.append(float(row[1]))
                bmis.append(float(row[2]))
                categories.append(row[3])
        
        # Plot bar chart of BMI categories
        plt.bar(categories, bmis)
        plt.xlabel("BMI Category")
        plt.ylabel("BMI")
        plt.title("BMI Analysis")
        plt.show()

# Create an instance of the BMICalculatorGUI class
bmi_calculator = BMICalculatorGUI()

# Start the GUI event loop
bmi_calculator.mainloop()
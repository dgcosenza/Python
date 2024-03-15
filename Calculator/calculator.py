#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tkinter as tk


def clear_screen():
	# Clear screen on Windows
	if os.name == "nt":
		os.system("cls")

	# Clear screen on macOS and Linux
	else:
		os.system("clear")


clear_screen()


def validate_input(a_str, b_str):
	try:
		float(a_str)
		float(b_str)
	except ValueError:
		print("Please enter valid numbers in both fields.\n")
		return False
	return True


def result_int(result):
	# Convert the result to an integer if the decimal is zero.
	if result.is_integer():
		result = int(result)
	return result


def perform_operation(a_str, b_str, operation):
	if not validate_input(a_str, b_str):
		return

	a = float(a_str)
	b = float(b_str)

	if operation == "sum":
		result = a + b
		print(f"The sum of the chosen numbers is: {result_int(result)}\n")
	elif operation == "subtract":
		result = a - b
		print(f"The subtraction of the chosen numbers is: {result_int(result)}\n")
	elif operation == "multiply":
		result = a * b
		print(f"The multiplication of the chosen numbers is: {result_int(result)}\n")
	elif operation == "divide":
		if b == 0:
			print("Division by zero is not allowed.\n")
			return
		result = a / b
		print(f"The division of the chosen numbers is: {result_int(result)}\n")


def get_input_values():
	a_str = num1.get()
	b_str = num2.get()
	return a_str, b_str


def addition():
	a_str, b_str = get_input_values()
	perform_operation(a_str, b_str, "sum")


def subtract():
	a_str, b_str = get_input_values()
	perform_operation(a_str, b_str, "subtract")


def multiply():
	a_str, b_str = get_input_values()
	perform_operation(a_str, b_str, "multiply")


def divide():
	a_str, b_str = get_input_values()
	perform_operation(a_str, b_str, "divide")


def clean_entry():
	num1.delete(0, tk.END)
	num2.delete(0, tk.END)


# Tkinter Interface
window = tk.Tk()

# Here goes all the tkinter code.
window.config(width=270, height=180)
window.title("Magic Calculator v1.0")

# Labels
label1 = tk.Label(text="Enter the number")
label1.place(x=10, y=10)

label2 = tk.Label(text="Enter the number")
label2.place(x=140, y=10)

# Text Input
num1 = tk.Entry()
num1.place(x=10, y=30, width=120, height=25)

num2 = tk.Entry()
num2.place(x=140, y=30, width=120, height=25)

# Buttons
button1 = tk.Button(text="Sum", command=addition)
button1.place(x=10, y=65, width=120)

button2 = tk.Button(text="Subtract", command=subtract)
button2.place(x=140, y=65, width=120)

button3 = tk.Button(text="Multiply", command=multiply)
button3.place(x=10, y=100, width=120)

button4 = tk.Button(text="Divide", command=divide)
button4.place(x=140, y=100, width=120)

button5 = tk.Button(text="Clear Fields", command=clean_entry)
button5.place(x=10, y=135, width=120)

button6 = tk.Button(text="Clear Screen", command=clear_screen)
button6.place(x=140, y=135, width=120)

window.mainloop()

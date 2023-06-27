from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.grid(row=0, column=1)

miles_unit_label = Label(text="Miles")
miles_unit_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(row=1, column=0)

kms_label = Label(text="0")
kms_label.grid(row=1, column=1)

kms_unit_label = Label(text="Km")
kms_unit_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate")
calculate_button.grid(row=2, column=1)


def calculate():
    try:
        miles_entry = int(miles.get())
    except ValueError:
        miles_entry = 0

    kms = int(miles_entry * 1.609)
    kms_label.config(text=f"{kms}")


calculate_button.config(command=calculate)

window.mainloop()
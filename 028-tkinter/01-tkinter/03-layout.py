import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

clicks = 0
# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()
my_label["text"] = "New text"
my_label.config(text=f"Button clicked {clicks} times.", padx=20, pady=20)


def button_clicked():
    global clicks
    clicks += 1
    print(entry.get())
    my_label.config(text=f"Button clicked {clicks} times. {entry.get()}")


my_button = tkinter.Button(text="Click me", command=button_clicked)
# my_button.pack()

# Entry
entry = tkinter.Entry()
# entry.pack()

# Layout Managers: 1) Pack, 2) Place, 3) Grid
# Pack: Packs the widgets next to each other in a vague format, the downside is that is too vague.
# Place: Is about precise positioning, the downside is that is too precise.
# Grid:
# my_label.place(x=100, y=150)
my_label.grid(column=0, row=0)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

entry.grid(column=3, row=2)

window.mainloop()

from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Read data


try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("./data/french_words.csv")
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, ...]
to_learn = words.to_dict(orient="records")
time_flipper = None
word = None


def correct():
    global word, words
    words = words.drop(word.index.values[0])
    words.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global time_flipper, word
    if time_flipper is not None:
        window.after_cancel(time_flipper)
    word = words.sample()
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"].values[0], fill="black")
    time_flipper = window.after(3000, flip_card)


def flip_card():
    global word
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"].values[0], fill="white")


# UI Interface
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0, background=BACKGROUND_COLOR, command=correct)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()

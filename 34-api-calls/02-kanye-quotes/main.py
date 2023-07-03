from tkinter import *
import requests


def get_quote():
    res = requests.get("https://api.kanye.rest")
    res.raise_for_status()
    data = res.json()
    canvas.itemconfig(quote, text=data.get("quote"))


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, background="white")

quote_background = PhotoImage(file="background.png")
canvas = Canvas(width=300, height=440, bg="white", highlightthickness=0)
canvas.create_image(150, 200, image=quote_background)
quote = canvas.create_text(150, 200, text="...", fill="white", font=("Arial", 30, "bold"), width=280)
canvas.pack()

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, background="white", command=get_quote)
kanye_button.pack()

get_quote()

window.mainloop()

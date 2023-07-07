from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global rounds
    if timer is not None:
        window.after_cancel(timer)
        label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        rounds = 0
        check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global rounds
    rounds += 1

    if rounds % 8 == 0:
        # counter_time = LONG_BREAK_MIN * 60
        counter_time = 7
        label.config(text="Break", fg=RED)
    elif rounds % 2 == 0:
        # counter_time = SHORT_BREAK_MIN * 60
        counter_time = 6
        label.config(text="Break", fg=PINK)
    else:
        # counter_time = WORK_MIN * 60
        counter_time = 5
        label.config(text="Work", fg=GREEN)

    count_down(counter_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_minutes = str(math.floor(count / 60))
    count_seconds = str(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_minutes.zfill(2)}:{count_seconds.zfill(2)}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if label.cget("text") == "Work":
            check_label.config(text=f"{check_label.cget('text')}✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 50))
label.grid(row=0, column=1)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", borderwidth=0, highlightthickness=0, bg=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", borderwidth=0, highlightthickness=0, bg=YELLOW, command=timer_reset)
reset_btn.grid(row=2, column=2)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()

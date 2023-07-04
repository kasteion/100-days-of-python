from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", font=FONT, bg=THEME_COLOR, justify="left")
        self.score.grid(row=0, column=1, pady=20, padx=20)

        self.question = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.question.create_text(150, 125, text="", font=FONT, fill=THEME_COLOR,
                                                       width=280)
        self.question.grid(row=1, column=0, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=question_text)
        else:
            self.question.itemconfig(self.question_text, text=f"You've get {self.quiz.score}/10 questions right.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def feedback(self, ans):
        if ans:
            self.question.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.question.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def true_pressed(self):
        ans = self.quiz.check_answer("true")
        self.feedback(ans)

    def false_pressed(self):
        ans = self.quiz.check_answer("false")
        self.feedback(ans)


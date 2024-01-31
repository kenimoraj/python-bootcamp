from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
WINDOW_PADDING = 20
CANVAS_PADDING = 50
FONT = ('Arial', 20, 'italic')
THEME_COLOR = "#375362"
BUTTON_SIZE = 120
class QuizInterface:

    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz
        self.quiz_is_on = True
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=THEME_COLOR)


        #Score

        self.scoreLabel = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        #Question Canvas
        self.question_canvas = Canvas(width=CANVAS_WIDTH,
                                      height=CANVAS_HEIGHT,
                                      bg="white")
        self.question_text = self.question_canvas.create_text(CANVAS_WIDTH/2,
                                                              CANVAS_HEIGHT/2,
                                                              text="Test",
                                                              font=FONT,
                                                              width=CANVAS_WIDTH-WINDOW_PADDING)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=CANVAS_PADDING)


        #Buttons
        img = Image.open("./images/true_ans.png")
        img = img.resize((BUTTON_SIZE, BUTTON_SIZE))

        true_img = ImageTk.PhotoImage(img)

        true_button = Button(image=true_img,
                             bg=THEME_COLOR,
                             activebackground=THEME_COLOR,
                             highlightthickness=0,
                             command=self.true_pressed)
        true_button.grid(row=2, column=0)

        img = Image.open("./images/false_ans.png")
        img = img.resize((BUTTON_SIZE, BUTTON_SIZE))

        false_img = ImageTk.PhotoImage(img)

        true_button = Button(image=false_img,
                             bg=THEME_COLOR,
                             activebackground=THEME_COLOR,
                             highlightthickness=0,
                             command=self.false_pressed)
        true_button.grid(row=2, column=1)



        #START
        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        self.process_answer(True)

    def false_pressed(self):
        self.process_answer(False)


    def process_answer(self, ans: bool):

        ans_txt: str
        if ans:
            ans_txt = "True"
        else:
            ans_txt = "False"

        if self.quiz_is_on:
            is_correct = self.quiz.check_answer(self.quiz.question_list[self.quiz.question_number - 1], ans_txt)
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            # print(self.quiz.question_number)
            self.give_feedback(is_correct)

            if self.quiz.still_has_questions():
                self.window.after(1000, func=self.get_next_question)
            else:
                self.quiz_is_on = False
                self.window.after(1000, func=self.end_text)


    def give_feedback(self, is_correct: bool):

        color: str
        if is_correct:
            color = "green"
        else:
            color = "red"

        self.question_canvas.config(bg=color)


    def end_text(self):
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(self.question_text, text=f"You finished the quiz with "
                                                                 f"{self.quiz.score}/"
                                                                 f"{len(self.quiz.question_list)} points!")
    def get_next_question(self):
        question = self.quiz.next_question()
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(self.question_text, text=question.question_text)
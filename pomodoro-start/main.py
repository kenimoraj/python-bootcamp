from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    #stop timer
    global timer
    window.after_cancel(timer)

    #reset clock to 00:00
    canvas.itemconfig(clock, text="00:00")

    #clear checkmarks
    global reps
    reps = 0
    check_marks.config(text="")

    #set top text to 'Timer'

    top_text.config(text="Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    reps %= 8


    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        top_text.config(text="Long Break", fg=RED)
        countdown_sec = long_break_sec
    elif reps % 2 == 0:
        top_text.config(text="Short Break", fg=PINK)
        countdown_sec = short_break_sec
    else:
        top_text.config(text="Work", fg=GREEN)
        check_marks_txt = ""
        for _ in range((reps + 1) // 2):
            check_marks_txt += "✔"
        check_marks.config(text=check_marks_txt)

        countdown_sec = work_sec

    window.after(0, countdown, countdown_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(seconds):
    min = seconds // 60
    sec = seconds % 60
    txt = "{min:02d}:{sec:02d}".format(min=min, sec=sec)
    canvas.itemconfig(clock, text=txt)
    global timer
    if seconds > 0:
        timer = window.after(1, countdown, seconds-1)
    else:
        window.after(0, start_timer)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, padx=100, pady=50, bg=YELLOW, )

tomato_img = PhotoImage(file="tomato.png", )


top_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), width=len("Short Break"))
top_text.grid(row=0, column=1)

canvas = Canvas(width=tomato_img.width(), height=tomato_img.height(), bg=YELLOW, highlightthickness=0)
canvas.create_image(tomato_img.width()/2, tomato_img.height()/2, image=tomato_img)
canvas.grid(row=1, column=1)


clock = canvas.create_text(tomato_img.width()/2, tomato_img.height()/2+20, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)



window.mainloop()

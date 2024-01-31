from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
INITIAL_TEXT_FONT = ('Courier', 30, "bold")
LANGUAGE_FONT = ('Courier', 30, "italic")
WORD_FONT = ('Courier', 30, "bold")
CARD_SIZE = (800, 526)
TEXT_ADJUST = 10

words_to_learn = []
current_card = {}
started = False
card_flip_timer = None
canvas_language = None
canvas_word = None
# --------------- BUTTON LOGIC ----------------- #


def word_learned():

    global words_to_learn, current_card
    try:
        words_to_learn.remove(current_card)
        print("Word has been removed")
    except ValueError:
        print("No more cards")


    #save to file
    csv_to_save = pandas.DataFrame(words_to_learn).to_csv()
    with open("./data/words_to_learn.csv", "w", encoding="utf-8") as file:
        file.write(csv_to_save)


def end_screen():
    global canvas
    canvas.itemconfig(image_on_canvas, image=card_front_img)
    canvas.itemconfig(card_title, text="No more words", fill="black")
    canvas.itemconfig(card_word, text="Congrats!", fill="black")


def load_new_word():

    global current_card, canvas, card_front_img, card_flip_timer

    current_card = random.choice(words_to_learn)
    canvas.itemconfig(image_on_canvas, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")

    word = current_card["French"]

    canvas.itemconfig(card_word, text=word, fill="black")

    card_flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card, canvas, card_back_img

    canvas.itemconfig(image_on_canvas, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")

    word = current_card["English"]

    canvas.itemconfig(card_word, text=word, fill="white")


def right_button():

    global window, started, card_flip_timer, words_to_learn

    if card_flip_timer is not None:
        window.after_cancel(card_flip_timer)

    if started:
        word_learned()
    else:
        started = True

    if len(words_to_learn) > 0:
        load_new_word()
    else:
        end_screen()



def wrong_button():

    if card_flip_timer is not None:
        window.after_cancel(card_flip_timer)

    global started
    if started and len(words_to_learn) > 0:
        load_new_word()




# --------------- UI SETUP --------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

#canvas
canvas = Canvas(width=CARD_SIZE[0], height=CARD_SIZE[1], bg=BACKGROUND_COLOR, highlightthickness=0)
image_on_canvas = canvas.create_image(CARD_SIZE[0]/2, CARD_SIZE[1]/2, image=card_front_img)
card_title = canvas.create_text(CARD_SIZE[0]/2-TEXT_ADJUST, CARD_SIZE[1]/4, text="FLASHCARDS",
                                    font=LANGUAGE_FONT, fill="black")
card_word = canvas.create_text(CARD_SIZE[0]/2-TEXT_ADJUST, CARD_SIZE[1]/2, text="Press the right button to start",
                                    font=WORD_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=3)

#buttons
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")


right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button)
right_button.grid(row=1, column=2)

wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button)
wrong_button.grid(row=1, column=0)

#load data
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    print("filefilefile0")
    df = pandas.read_csv("./data/french_words.csv")
finally:
    words_to_learn = [{"French": row.French, "English": row.English} for (index, row) in df.iterrows()]


window.mainloop()


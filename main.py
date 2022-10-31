# Imports

from tkinter import *
import setupdatechoose
import random

""" Game plan

1. create Excel sheet with 3 columns - Chinese symbol, chinese pronunciation, english meaning X
2. create csv file of it so program can read X
3. Design UI X
    3a. create menu - add symbols, start practicing button, choose language set to test on ( possible future update)
    3b. create functionality - when start practice button is pressed all labels and buttons disappear and several
    labels show up and a text box and buttons show up
    3c. scoring to be introduced and weighting of words( the more success with a word the less it appears
    [possible future update])
4. create logic of flash cards X
5. save different factors to a separate file (csv or json not sure yet)



"""

# variables ----------------------------------

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91c2af"
FONT_CANTONESE = ("Arial", 40, "italic")
FONT_SYMBOL = ("Arial", 60, "bold")
FONT_BTN = ("Arial", 30)
FONT_CARD_BTN = ("Arial", 15)
FONT_INNER = ("Arial", 15)
FONT_INNER_LRG = ("Arial", 50)
global key_list
global current_card
language_set = None


# initializations ----------------------------

def flashcard_page():
    remove_main_menu()
    remove_update_widgets()
    title_label.place(x=300, y=50)
    symbol_label.place(x=400, y=200)
    pronunciation_label.place(x=350, y=300)
    unknown_btn.place(x=100, y=400)
    known_btn.place(x=690, y=400)
    next_card()


def next_card():
    global current_card
    current_card = random.choice(key_list)
    print(current_card)
    canvas.itemconfig(canvas_image, image=card_back)
    title_label["bg"] = CARD_BACK_COLOR
    symbol_label["bg"] = CARD_BACK_COLOR
    pronunciation_label["bg"] = CARD_BACK_COLOR
    title_label["fg"] = "white"
    symbol_label["fg"] = "white"
    pronunciation_label["fg"] = "white"
    symbol_label["text"] = current_card
    pronunciation_label["text"] = language_set[current_card][0]
    window.after(5000, func=english_side)


def english_side():
    canvas.itemconfig(canvas_image, image=card_front)
    title_label["bg"] = "white"
    symbol_label["bg"] = "white"
    pronunciation_label["bg"] = "white"
    title_label["fg"] = "black"
    symbol_label["fg"] = "black"
    pronunciation_label["fg"] = "black"
    symbol_label["text"] = current_card
    pronunciation_label["text"] = language_set[current_card][1]


def remove_main_menu():
    title_label.place(x=2000, y=2000)


def remove_flash_page():
    symbol_label.place(x=2000, y=2000)
    pronunciation_label.place(x=2000, y=2000)


def remove_update_widgets():
    file_name_text.place(x=2000, y=2000)
    file_name_label.place(x=2000, y=2000)
    new_word_label.place(x=2000, y=2000)
    new_word_text.place(x=2000, y=2000)
    new_symbol_label.place(x=2000, y=2000)
    new_symbol_text.place(x=2000, y=2000)
    new_translation_label.place(x=2000, y=2000)
    new_translation_text.place(x=2000, y=2000)
    change_set_btn.place(x=2000, y=2000)
    update_set_btn.place(x=2000, y=2000)


def main_page():
    remove_update_widgets()
    remove_flash_page()
    title_label.place(x=300, y=50)


def update_page():
    remove_main_menu()
    remove_flash_page()
    title_label.place(x=300, y=50)
    file_name_label.place(x=100, y=130)
    file_name_text.place(x=100, y=160)
    new_word_label.place(x=100, y=230)
    new_word_text.place(x=100, y=260)
    new_symbol_label.place(x=100, y=330)
    new_symbol_text.place(x=100, y=360)
    new_translation_label.place(x=100, y=430)
    new_translation_text.place(x=100, y=460)
    change_set_btn.place(x=300, y=160)
    update_set_btn.place(x=300, y=360)
    file_name_text.focus()


def update_set():
    file_name = file_name_text.get()
    new_pronunciation = new_word_text.get()
    new_symbol = new_symbol_text.get()
    new_translation = new_translation_text.get()
    setupdatechoose.update_language(file_name, new_symbol, new_pronunciation, new_translation)


def change_set():
    global language_set
    global key_list
    file_name = file_name_text.get()
    language_set = setupdatechoose.choose_language(file_name)
    key_list = list(language_set)
    language_loaded_label["text"] = "a set of flash cards have been uploaded. You may study."


# Functions ----------------------------------

window = Tk()
window.title("Flashcard Memorizer")
window.config(padx=50, pady=50, bg="lightblue")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
known = PhotoImage(file="images/right.png")
unknown = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=900, height=600, bg="lightblue", highlightthickness=0)
canvas_image = canvas.create_image((460, 300), image=card_front)
canvas.grid(column=0, row=1, columnspan=3)

start_btn = Button(text="Start Practicing", highlightthickness=0, font=FONT_BTN, width=15, command=flashcard_page)
start_btn.grid(column=0, row=2)

main_btn = Button(text="Main Menu", highlightthickness=0, font=FONT_BTN, width=15, command=main_page)
main_btn.grid(column=1, row=2)

choose_btn = Button(text="Choose/Update Set", highlightthickness=0, font=FONT_BTN, width=15, command=update_page)
choose_btn.grid(column=2, row=2)

# main menu widgets

title_label = Label(text="Flashcard Helper", font=FONT_CANTONESE, bg="white", fg="black")
title_label.place(x=300, y=50)

language_loaded_label = Label(text="Language set has not been uploaded into program. Upload please.",
                              highlightthickness=0, font=FONT_INNER, bg="lightblue", fg="black")
language_loaded_label.place(x=230, y=570)

# update/choose file widgets

file_name_label = Label(text="input new filename.csv to use/update (file must be in data directory)",
                        highlightthickness=0, font=FONT_INNER, bg="white",
                        fg="black")
file_name_label.place(x=2000, y=2000)

file_name_text = Entry()
file_name_text.insert(0, "cantonese_flash.csv")
file_name_text.place(x=2000, y=2000)

change_set_btn = Button(text="Update language stored (include .csv)", highlightthickness=0, font=FONT_CARD_BTN,
                        width=25, command=change_set)
change_set_btn.place(x=2000, y=2000)

update_set_btn = Button(text="Update Set with New Word", highlightthickness=0, font=FONT_CARD_BTN, width=25,
                        command=update_set)
update_set_btn.place(x=2000, y=2000)

new_word_label = Label(text="input new word to place in set", highlightthickness=0, font=FONT_INNER, bg="white",
                       fg="black")
new_word_label.place(x=2000, y=2000)

new_word_text = Entry()
new_word_text.place(x=2000, y=2000)

new_symbol_label = Label(text="input symbol (if any)", highlightthickness=0, font=FONT_INNER, bg="white", fg="black")
new_symbol_label.place(x=2000, y=2000)

new_symbol_text = Entry()
new_symbol_text.place(x=2000, y=2000)

new_translation_label = Label(text="English Translation", highlightthickness=0, font=FONT_INNER, bg="white", fg="black")
new_translation_label.place(x=2000, y=2000)

new_translation_text = Entry()
new_translation_text.place(x=2000, y=2000)

# flash card page

symbol_label = Label(text=f"", highlightthickness=0, font=FONT_INNER_LRG, bg=CARD_BACK_COLOR, fg="white")
symbol_label.place(x=2000, y=2000)

pronunciation_label = Label(text=f"", highlightthickness=0, font=FONT_INNER_LRG, bg=CARD_BACK_COLOR, fg="white")
pronunciation_label.place(x=2000, y=2000)

known_btn = Button(image=known, highlightthickness=0, bg=CARD_BACK_COLOR, command=next_card)
known_btn.place(x=2000, y=2000)

unknown_btn = Button(image=unknown, highlightthickness=0, bg=CARD_BACK_COLOR, command=next_card)
unknown_btn.place(x=2000, y=2000)

window.mainloop()

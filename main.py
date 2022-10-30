# Imports

from tkinter import *
import SetUpdateChoose

""" Game plan

1. create Excel sheet with 3 columns - Chinese symbol, chinese pronunciation, english meaning X
2. create csv file of it so program can read
3. Design UI
    3a. create menu - add symbols, start practicing button, choose language set to test on ( possible future update)
    3b. create functionality - when start practice button is pressed all labels and buttons disappear and several
    labels show up and a text box and buttons show up
    3c. scoring to be introduced and weighting of words( the more success with a word the less it appears
    [possible future update])
4. create logic of flash cards
5. save different factors to a separate file (csv or json not sure yet)



"""

# variables ----------------------------------

BACKGROUND_COLOR = "#B1DDC6"
FONT_CANTONESE = ("Arial", 40, "italic")
FONT_SYMBOL = ("Arial", 60, "bold")
FONT_BTN = ("Arial", 30)
FONT_CARD_BTN = ("Arial", 15)
FONT_INNER = ("Arial", 15)
language_set = None


# initializations ----------------------------

def print_whatever():
    global language_set
    print(language_set)

def remove_main_menu():
    timer_label.place(x=2000, y=2000)
    timer_text.place(x=2000, y=2000)
    title_label.place(x=2000, y=2000)


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


def flashcard_page():
    time_per_card = timer_text.get()
    remove_main_menu()
    remove_update_widgets()


def main_page():
    remove_update_widgets()
    timer_label.place(x=100, y=130)
    timer_text.place(x=100, y=160)
    title_label.place(x=300, y=50)


def update_page():
    remove_main_menu()
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


def update_set():
    file_name = file_name_text.get()
    SetUpdateChoose.update_language(file_name, language_set)


def change_set():
    global language_set
    file_name = file_name_text.get()
    language_set = SetUpdateChoose.choose_language(file_name)
    print_whatever()


# Functions ----------------------------------

window = Tk()
window.title("Flashcard Memorizer")
window.config(padx=50, pady=50, bg="lightblue")
card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=900, height=600, bg="lightblue", highlightthickness=0)
canvas.create_image((460, 300), image=card_front)
canvas.grid(column=0, row=1, columnspan=3)

start_btn = Button(text="Start Practicing", highlightthickness=0, font=FONT_BTN, width=15, command=flashcard_page)
start_btn.grid(column=0, row=2)

main_btn = Button(text="Main Menu", highlightthickness=0, font=FONT_BTN, width=15, command=main_page)
main_btn.grid(column=1, row=2)

choose_btn = Button(text="Choose/Update Set", highlightthickness=0, font=FONT_BTN, width=15, command=update_page)
choose_btn.grid(column=2, row=2)

# main menu widgets

title_label = Label(text="Flashcard Helper", font=FONT_CANTONESE, bg="white")
title_label.place(x=300, y=50)

timer_label = Label(text="Input time amount seconds per flashcard", highlightthickness=0, font=FONT_INNER, bg="white",
                    fg="black")
timer_label.place(x=100, y=130)

timer_text = Entry()
timer_text.place(x=100, y=160)
timer_text.insert(0, 10)

# update/choose file widgets

file_name_label = Label(text="input new filename.csv to use/update (file must be in data directory)",
                        highlightthickness=0, font=FONT_INNER, bg="white",
                        fg="black")
file_name_label.place(x=2000, y=2000)

file_name_text = Entry()
file_name_text.place(x=2000, y=2000)

change_set_btn = Button(text="Change Set (include .csv)", highlightthickness=0, font=FONT_CARD_BTN, width=20,
                        command=change_set)
change_set_btn.place(x=2000, y=2000)

update_set_btn = Button(text="Update Set with New Word", highlightthickness=0, font=FONT_CARD_BTN, width=20,
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

window.mainloop()

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
reps = 0
timer_start = ''


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer_start)
    canvas.itemconfig(timer_text, text=f'00:00')
    timer.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        timer['text'] = 'Work'
        timer['fg'] = GREEN
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer['text'] = 'Break'
        timer['fg'] = RED
    else:
        count_down(short_break_sec)
        timer['text'] = 'Break'
        timer['fg'] = PINK


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = '00'
    if len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min} : {count_sec}')
    if count > 0:
        global timer_start
        timer_start = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark['text'] += ' ✔'


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Tomato Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="0:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)
start_button = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='Rest', highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)
checkmark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark.grid(column=1, row=3)

window.mainloop()

"""---Imports---"""
from tkinter import *

"""---Constants---"""
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


"""---Timer Reset---"""


def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    reps = 0


"""---Timer Mechanism---"""


def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        num_of_checks = ((reps % 8) // 2) + 1
        check_label.config(text=f"{'✔' * num_of_checks}")
        countdown(WORK_MIN * 60)


"""---Countdown Mechanism---"""


def time_format(time):
    if 0 <= time <= 9:
        return f"0{time}"
    return time


def countdown(count):
    minutes = int(count / 60)
    minutes = time_format(minutes)
    seconds = count % 60
    seconds = time_format(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer

        timer = window.after(1000, countdown, count - 1)
    else:
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        start_timer()


"""---UI Setup---"""


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()

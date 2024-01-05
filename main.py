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
count_timer = "None"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(count_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break)
        #     pink
        timer.config(text="Break", fg=PINK)

    elif reps % 8 == 0:
        count_down(long_break)
        #     red
        timer.config(text="Break", fg=RED)

    else:
        count_down(work_sec)
        #         green
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global count_timer
        count_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
            check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
timer.grid(row=1, column=2)

start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(row=3, column=1)

reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(row=3, column=3)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(row=4, column=2)

window.mainloop()

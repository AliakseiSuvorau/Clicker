import tkinter as tk
import os
import pygame

pygame.mixer.init()
os.system("xset r off")


def play_sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


def inc_score(event):
    if not paused:
        global count_clicks
        global count_coins
        global plus_point
        global hidden_count_clicks
        count_clicks += 1
        hidden_count_clicks += plus_point
        clicks_lbl["text"] = str(count_clicks)
        count_coins = hidden_count_clicks // 10
        coins_lbl["text"] = str(f"Coins: {count_coins}")
        play_sound("sounds/click.mp3")


def make_x2_boost(event):
    if not paused:
        global plus_point
        global count_coins
        global needed_for_x2
        global hidden_count_clicks
        if count_coins >= needed_for_x2:
            play_sound("sounds/upgrade.wav")
            count_coins -= needed_for_x2
            hidden_count_clicks -= needed_for_x2 * 10
            plus_point *= 2
            coins_lbl["text"] = str(f"Coins: {count_coins}")
            needed_for_x2 *= 5
            lbl_needed_for_x2["text"] = str(needed_for_x2)
        else:
            play_sound("sounds/error.wav")


def auto_click_start(event):
    if not paused:
        global auto_click_bool
        global count_coins
        global d_time
        global needed_for_auto_click
        global hidden_count_clicks
        if count_coins >= needed_for_auto_click:
            auto_click_bool = False
            play_sound("sounds/upgrade.wav")
            count_coins -= needed_for_auto_click
            hidden_count_clicks -= needed_for_auto_click * 10
            needed_for_auto_click *= 2
            lbl_needed_for_auto_click["text"] = str(needed_for_auto_click)
            coins_lbl["text"] = str(f"Coins: {count_coins}")
            auto_click()
            auto_click_bool = True
        else:
            play_sound("sounds/error.wav")


def auto_click():
    global count_coins
    global window
    global count_clicks
    global hidden_count_clicks
    if not paused:
        if auto_click_bool:
            play_sound("sounds/click.mp3")
        count_clicks += 1
        hidden_count_clicks += plus_point
        clicks_lbl["text"] = str(count_clicks)
        count_coins = hidden_count_clicks // 10
        coins_lbl["text"] = str(f"Coins: {count_coins}")
        window.after(d_time, auto_click)
    else:
        window.after(d_time, auto_click)


def pause(event):
    global paused
    if not paused:
        paused = True
        lbl_pause.pack()
    else:
        paused = False
        lbl_pause.pack_forget()


file = open("record.txt", "r")
highest_score = file.read()
window = tk.Tk()
window.title("Clicker")
window.geometry("1080x720")
window.resizable(width=False, height=False)

count_clicks = 0
hidden_count_clicks = 0
count_coins = 0
plus_point = 1
needed_for_x2 = 10
auto_click_bool = 0
needed_for_auto_click = 50
d_time = 5000
paused = False

bg = tk.PhotoImage(file="images/fon.png")
bg_png = tk.Label(window, image=bg)
bg_png.place(x=0, y=0)

high_score_lbl = tk.Label(window, text="Highest score: " + highest_score, bg="white", font=("Times New Roman", 20), width=25)
high_score_lbl.pack(side=tk.BOTTOM)

clicks_lbl = tk.Label(window, text="0", bg="white", font=("Times New Roman", 40), width=12)
clicks_lbl.pack(side=tk.BOTTOM)

coins_lbl = tk.Label(window, text="Coins: 0", bg="white", font=("Times New Roman", 40), width=40)
coins_lbl.pack()

img_x2_boost = tk.PhotoImage(file="images/img_x2_boost.png")
x2_boost = tk.Button(window, image=img_x2_boost)
x2_boost.place(x=0, y=320)

lbl_needed_for_x2 = tk.Label(window, text="10", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
lbl_needed_for_x2.place(x=0, y=270)

img_auto_click = tk.PhotoImage(file="images/img_auto_click.png")
auto_click_btn = tk.Button(window, image=img_auto_click)
auto_click_btn.place(x=0, y=180)

lbl_needed_for_auto_click = tk.Label(window, text="50", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
lbl_needed_for_auto_click.place(x=0, y=130)

pause_img = tk.PhotoImage("images/pause.png")
lbl_pause = tk.Label(window, text="PAUSE", bg="white", font=("Times New Roman", 40))

window.bind("<space>", inc_score)
x2_boost.bind("<Button-1>", make_x2_boost)
auto_click_btn.bind("<Button-1>", auto_click_start)
window.bind("<Escape>", pause)

window.mainloop()
file.close()
file = open("record.txt", "w")
file.write(str(max(count_clicks, int(highest_score))))
file.close()
os.system("xset r on")

import tkinter as tk
import os
import pygame
import functions as f
import Globals as g
import asyncio


async def main():
    while True:
        window.bind("<space>", lambda event: f.inc_score(clicks_lbl, coins_lbl))
        x2_boost.bind("<Button-1>", lambda event: f.make_x2_boost(coins_lbl, lbl_needed_for_x2))
        auto_click_btn.bind("<Button-1>",
                            lambda event: f.auto_click_start(lbl_needed_for_auto_click, coins_lbl, clicks_lbl, window))
        window.bind("<Escape>", lambda event: f.pause(lbl_pause))
        await asyncio.sleep(1 / 1000)


pygame.mixer.init()
os.system("xset r off")


file = open("../record.txt", "r")
highest_score = file.read()
window = tk.Tk()
window.title("Clicker")
window.geometry("1080x720")
window.resizable(width=False, height=False)

bg = tk.PhotoImage(file="../images/fon.png")
bg_png = tk.Label(window, image=bg)
bg_png.place(x=0, y=0)

high_score_lbl = tk.Label(window, text="Highest score: " + highest_score, bg="white", font=("Times New Roman", 20), width=25)
high_score_lbl.pack(side=tk.BOTTOM)

clicks_lbl = tk.Label(window, text="0", bg="white", font=("Times New Roman", 40), width=12)
clicks_lbl.pack(side=tk.BOTTOM)

coins_lbl = tk.Label(window, text="Coins: 0", bg="white", font=("Times New Roman", 40), width=40)
coins_lbl.pack()

img_x2_boost = tk.PhotoImage(file="../images/img_x2_boost.png")
x2_boost = tk.Button(window, image=img_x2_boost)
x2_boost.place(x=0, y=320)

lbl_needed_for_x2 = tk.Label(window, text="10", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
lbl_needed_for_x2.place(x=0, y=270)

img_auto_click = tk.PhotoImage(file="../images/img_auto_click.png")
auto_click_btn = tk.Button(window, image=img_auto_click)
auto_click_btn.place(x=0, y=180)

lbl_needed_for_auto_click = tk.Label(window, text="50", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
lbl_needed_for_auto_click.place(x=0, y=130)

lbl_pause = tk.Label(window, text="PAUSE", bg="white", font=("Times New Roman", 40))

window.bind("<space>", lambda event: f.inc_score(clicks_lbl, coins_lbl))
x2_boost.bind("<Button-1>", lambda event: f.make_x2_boost(coins_lbl, lbl_needed_for_x2))
auto_click_btn.bind("<Button-1>", lambda event: f.auto_click_start(lbl_needed_for_auto_click, coins_lbl, clicks_lbl, window))
window.bind("<Escape>", lambda event: f.pause(lbl_pause))
window.mainloop()


file.close()
file = open("../record.txt", "w")
file.write(str(max(g.count_clicks, int(highest_score))))
file.close()
os.system("xset r on")


print("End")

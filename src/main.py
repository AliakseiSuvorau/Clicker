import tkinter as tk
import os
import pygame
import functions as f
import Globals as g


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
bg_png.place(x=g.x_bg_png, y=g.y_bg_png)

high_score_lbl = tk.Label(window, text="Highest score: " + highest_score, bg="white", font=(g.font, g.high_score_label_font_size), width=g.high_score_label_width)
high_score_lbl.pack(side=tk.BOTTOM)

clicks_lbl = tk.Label(window, text="0", bg="white", font=(g.font, g.click_lbl_font_size), width=g.click_lbl_width)
clicks_lbl.pack(side=tk.BOTTOM)

coins_lbl = tk.Label(window, text="Coins: 0", bg="white", font=(g.font, g.coins_lbl_font_size), width=g.coins_lbl_width)
coins_lbl.pack()

img_x2_boost = tk.PhotoImage(file="../images/img_x2_boost.png")
x2_boost = tk.Button(window, image=img_x2_boost)
x2_boost.place(x=g.x2_button_x, y=g.x2_button_y)

lbl_needed_for_x2 = tk.Label(window, text="10", width=4, height=1, bg="white", font=(g.font, g.x2_lbl_needed_font_size, "bold"))
lbl_needed_for_x2.place(x=g.x2_lbl_needed_x, y=g.x2_lbl_needed_y)

img_auto_click = tk.PhotoImage(file="../images/img_auto_click.png")
auto_click_btn = tk.Button(window, image=img_auto_click)
auto_click_btn.place(x=g.auto_click_button_x, y=g.auto_click_button_y)

lbl_needed_for_auto_click = tk.Label(window, text="50", width=g.auto_click_needed_lbl_width,
                                     height=g.auto_click_needed_lbl_height,
                                     bg="white",
                                     font=(g.font, g.auto_click_needed_lbl_font_size, "bold"))
lbl_needed_for_auto_click.place(x=g.auto_click_needed_lbl_x, y=g.auto_click_needed_lbl_y)

lbl_pause = tk.Label(window, text="PAUSE", bg="white", font=(g.font, g.pause_lbl_font_size))

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

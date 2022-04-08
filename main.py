# sudo apt-get install python3-tk
import tkinter as tk
import os
os.system("xset r off")


def inc_score(event):
    global count_clicks
    global count_coins
    global plus_point
    global hidden_count_clicks
    count_clicks += 1
    hidden_count_clicks += plus_point
    clicks_lbl["text"] = str(count_clicks)
    count_coins = hidden_count_clicks // 10
    coins_lbl["text"] = str(f"Coins: {count_coins}")


def make_x2_boost(event):
    global plus_point
    global count_coins
    global needed_for_x2
    global hidden_count_clicks
    if count_coins >= needed_for_x2:
        count_coins -= needed_for_x2
        hidden_count_clicks -= needed_for_x2 * 10
        plus_point *= 2
        coins_lbl["text"] = str(f"Coins: {count_coins}")
        needed_for_x2 *= 5
        lbl_needed_for_x2["text"] = str(needed_for_x2)


# def auto_click_start(event):
#     global auto_click_bool
#     auto_click_bool = 1
#
#     if auto_click_bool:
#         window.after(500, inc_score)
#         window.after(500, auto_click_start)


# def stop_auto_click(event):
#     pass


window = tk.Tk()
window.title("Clicker")
window.geometry("1080x720")
window.resizable(width=False, height=False)
window['bg'] = 'lightblue'
count_clicks = 0
hidden_count_clicks = 0
count_coins = 0
plus_point = 1
needed_for_x2 = 10
auto_click_bool = 0

clicks_lbl = tk.Label(window, text="0", bg="white", font=("Times New Roman", 40), width=10)
clicks_lbl.pack(side=tk.BOTTOM)

coins_lbl = tk.Label(window, text="Coins: 0", bg="white", font=("Times New Roman", 40), width=40)
coins_lbl.pack()

img_x2_boost = tk.PhotoImage(file="images/img_x2_boost.png")
x2_boost = tk.Button(window, image=img_x2_boost)
x2_boost.place(x=0, y=320)

lbl_needed_for_x2 = tk.Label(window, text="10", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
lbl_needed_for_x2.place(x=0, y=270)

# img_auto_click = tk.PhotoImage(file="images/img_auto_click.png")
# auto_click = tk.Button(window, image=img_auto_click)
# auto_click.place(x=0, y=180)

# lbl_needed_for_auto_click = tk.Label(window, text="100", width=4, height=1, bg="white", font=("Times New Roman", 30, "bold"))
# lbl_needed_for_auto_click.place(x=0, y=130)
# window.after(10000, stop_auto_click)

window.bind("<space>", inc_score)
x2_boost.bind("<Button-1>", make_x2_boost)
# auto_click.bind("<Button-1>", auto_click_start)

window.mainloop()

os.system("xset r on")

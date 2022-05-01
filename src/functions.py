import pygame
import Globals as g
import random

def play_sound(sound):
    """
    This function plays the sound
    :param sound: path to the file with a sound
    :return: nothing, just plays the sound :)
    """
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


def inc_score(clicks_lbl, coins_lbl, high_score_lbl, new_rec_lbl, afk_lbl):
    """
    This function increases the amount of clicks by 1 and updates the amount of coins
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :param new_rec_lbl: Label, which shows "New Record!" phrase
    :param high_score_lbl: Label, which shows current high score
    :param clicks_lbl: Label, which shows the amount of clicks
    :param coins_lbl: Label, which shows the amount of coins
    :return: nothing
    """
    if not g.paused:
        g.afk = False
        afk_lbl_turn_off(afk_lbl)
        g.count_clicks += 1
        g.hidden_count_clicks += g.plus_point
        clicks_lbl["text"] = str(g.count_clicks)
        g.count_coins = g.hidden_count_clicks // g.coeff
        coins_lbl["text"] = str(f"Coins: {g.count_coins}")
        change_high_score(high_score_lbl, new_rec_lbl)
        play_sound("../sounds/click.mp3")


def make_x2_boost(coins_lbl, lbl_needed_for_x2, afk_lbl):
    """
    This function checks if there are enough coins to buy an upgrade and eventually
    makes it bought, then it increases the price of the upgrade for the next purchase
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :param coins_lbl: Label, which shows the amount of coins
    :param lbl_needed_for_x2: Label, which shows the amount of coins needed to buy the x2 upgrade
    :return: nothing
    """
    if not g.paused:
        if g.count_coins >= g.needed_for_x2:
            afk_lbl_turn_off(afk_lbl)
            play_sound("../sounds/upgrade.wav")
            g.count_coins -= g.needed_for_x2
            g.hidden_count_clicks -= g.needed_for_x2 * g.coeff
            g.plus_point *= 2
            coins_lbl["text"] = str(f"Coins: {g.count_coins}")
            g.needed_for_x2 *= 5
            lbl_needed_for_x2["text"] = str(g.needed_for_x2)
        else:
            play_sound("../sounds/error.wav")


def auto_click_start(lbl_needed_for_auto_click, coins_lbl, clicks_lbl, window, high_score_lbl, new_rec_lbl, afk_lbl):
    """
    This function checks if there are enough coins to buy an upgrade and eventually
    makes it bought, then it increases the price of the upgrade for the next purchase
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :param new_rec_lbl: Label, which shows "New Record!" phrase
    :param high_score_lbl: Label, which shows current high score
    :param lbl_needed_for_auto_click: Label, which shows the amount of coins needed to buy the auto click upgrade
    :param coins_lbl: Label, which shows the amount of coins
    :param clicks_lbl: Label, which shows the amount of clicks
    :param window: the window, on which everything is displayed
    :return: nothing
    """
    if not g.paused:
        if g.count_coins >= g.needed_for_auto_click:
            afk_lbl_turn_off(afk_lbl)
            g.auto_click_bool = False
            play_sound("../sounds/upgrade.wav")
            g.count_coins -= g.needed_for_auto_click
            g.hidden_count_clicks -= g.needed_for_auto_click * g.coeff
            g.needed_for_auto_click *= 2
            lbl_needed_for_auto_click["text"] = str(g.needed_for_auto_click)
            coins_lbl["text"] = str(f"Coins: {g.count_coins}")
            auto_click(clicks_lbl, coins_lbl, window, high_score_lbl, new_rec_lbl)
            g.auto_click_bool = True
        else:
            play_sound("../sounds/error.wav")


def auto_click(clicks_lbl, coins_lbl, window, high_score_lbl, new_rec_lbl):
    """
    This function make a click: it increases the amount of points,
    puts the results on the screen and runs itself after some time
    :param new_rec_lbl: Label, which shows "New Record!" phrase
    :param high_score_lbl: Label, which shows current high score
    :param clicks_lbl: Label, which shows the amount of clicks
    :param coins_lbl: Label, which shows the amount of coins
    :param window: the window, on which everything is displayed
    :return: nothing
    """
    if not g.paused:
        if g.auto_click_bool:
            play_sound("../sounds/click.mp3")
        g.count_clicks += 1
        g.hidden_count_clicks += g.plus_point
        clicks_lbl["text"] = str(g.count_clicks)
        g.count_coins = g.hidden_count_clicks // g.coeff
        coins_lbl["text"] = str(f"Coins: {g.count_coins}")
        change_high_score(high_score_lbl, new_rec_lbl)
        window.after(g.d_time, lambda: auto_click(clicks_lbl, coins_lbl, window, high_score_lbl, new_rec_lbl))
    else:
        window.after(g.d_time, lambda: auto_click(clicks_lbl, coins_lbl, window, high_score_lbl, new_rec_lbl))


def pause(lbl_pause, afk_lbl):
    """
    Puts the game to pause, makes the Label with thew "PAUSE" word visible.
    With the second click ends the pause and continues the game
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :param lbl_pause: Label, which shows the word "PAUSE"
    :return: nothing
    """
    if not g.paused:
        g.paused = True
        lbl_pause.pack()
        afk_lbl_turn_off(afk_lbl)

    else:
        g.paused = False
        lbl_pause.pack_forget()


def change_high_score(high_score_lbl, new_rec_lbl):
    """
    This function changes high score if it was beaten
    :param high_score_lbl: Label, which shows current highest score
    :param new_rec_lbl: Label, which shows "New Record!" phrase
    :return: nothing
    """
    # Reading high record from the file
    file = open("../record.txt", "r")
    highest_score = file.read()
    file.close()

    if g.count_clicks > int(highest_score):
        new_rec_lbl.place(x=0, y=0)

    # Updating record
    file = open("../record.txt", "w")
    file.write(str(max(g.count_clicks, int(highest_score))))
    file.close()

    # Reading high record from the file
    file = open("../record.txt", "r")
    highest_score = file.read()
    file.close()

    high_score_lbl['text'] = str(f"Highest score: {highest_score}")


def afk_check(window, afk_lbl):
    """
    This function checks if the player is afk
    :param window: The window, on which everything is displayed
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :return: nothing
    """
    if g.afk and not g.paused:
        afk_lbl.place(x=random.randint(0, g.x_range), y=random.randint(0, g.y_range))
    g.afk = True
    window.after(g.time_afk_check, lambda: afk_check(window, afk_lbl))


def afk_lbl_turn_off(afk_lbl):
    """
    This function makes the afk label disappear
    :param afk_lbl: Label, which shows "Are you here?" phrase
    :return: nothing
    """
    afk_lbl.place_forget()

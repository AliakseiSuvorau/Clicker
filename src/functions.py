import pygame
import Globals as g


def play_sound(sound):
    """
    This function plays the sound
    :param sound: path to the file with a sound
    :return: nothing, just plays the sound :)
    """
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


def inc_score(clicks_lbl, coins_lbl):
    """
    This function increases the amount of clicks by 1 and updates the amount of coins
    :param clicks_lbl: Label, which shows the amount of clicks
    :param coins_lbl: Label, which shows the amount of coins
    :return: nothing
    """
    if not g.paused:
        g.count_clicks += 1
        g.hidden_count_clicks += g.plus_point
        clicks_lbl["text"] = str(g.count_clicks)
        g.count_coins = g.hidden_count_clicks // 10
        coins_lbl["text"] = str(f"Coins: {g.count_coins}")
        play_sound("../sounds/click.mp3")


def make_x2_boost(coins_lbl, lbl_needed_for_x2):
    """
    This function checks if there are enough coins to buy an upgrade and eventually
    makes it bought, then it increases the price of the upgrade for the next purchase
    :param coins_lbl: Label, which shows the amount of coins
    :param lbl_needed_for_x2: Label, which shows the amount of coins needed to buy the x2 upgrade
    :return: nothing
    """
    if not g.paused:
        if g.count_coins >= g.needed_for_x2:
            play_sound("../sounds/upgrade.wav")
            g.count_coins -= g.needed_for_x2
            g.hidden_count_clicks -= g.needed_for_x2 * 10
            g.plus_point *= 2
            coins_lbl["text"] = str(f"Coins: {g.count_coins}")
            g.needed_for_x2 *= 5
            lbl_needed_for_x2["text"] = str(g.needed_for_x2)
        else:
            play_sound("../sounds/error.wav")


def auto_click_start(lbl_needed_for_auto_click, coins_lbl, clicks_lbl, window):
    """
    This function checks if there are enough coins to buy an upgrade and eventually
    makes it bought, then it increases the price of the upgrade for the next purchase
    :param lbl_needed_for_auto_click: Label, which shows the amount of coins needed to buy the auto click upgrade
    :param coins_lbl: Label, which shows the amount of coins
    :param clicks_lbl: Label, which shows the amount of clicks
    :param window: the window, on which everything is displayed
    :return: nothing
    """
    if not g.paused:
        if g.count_coins >= g.needed_for_auto_click:
            g.auto_click_bool = False
            play_sound("../sounds/upgrade.wav")
            g.count_coins -= g.needed_for_auto_click
            g.hidden_count_clicks -= g.needed_for_auto_click * 10
            g.needed_for_auto_click *= 2
            lbl_needed_for_auto_click["text"] = str(g.needed_for_auto_click)
            coins_lbl["text"] = str(f"Coins: {g.count_coins}")
            auto_click(clicks_lbl, coins_lbl, window)
            g.auto_click_bool = True
        else:
            play_sound("../sounds/error.wav")


def auto_click(clicks_lbl, coins_lbl, window):
    """
    This function make a click: it increases the amount of points,
    puts the results on the screen and runs itself after some time
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
        g.count_coins = g.hidden_count_clicks // 10
        coins_lbl["text"] = str(f"Coins: {g.count_coins}")
        window.after(g.d_time, lambda: auto_click(clicks_lbl, coins_lbl, window))
    else:
        window.after(g.d_time, lambda: auto_click(clicks_lbl, coins_lbl, window))


def pause(lbl_pause):
    """
    Puts the game to pause, makes the Label with thew "PAUSE" word visible.
    With the second click ends the pause and continues the game
    :param lbl_pause: Label, which shows the word "PAUSE"
    :return: nothing
    """
    if not g.paused:
        g.paused = True
        lbl_pause.pack()
    else:
        g.paused = False
        lbl_pause.pack_forget()

"""File containing all the main function for the auto testing for TFT.
"""
from __future__ import annotations
from typing import Any, Optional
import pyautogui
import time
import pydirectinput


def click(obj: str, printability: bool = True, butt: str = 'left') -> None:
    """Click a location on the screen by a picture

    Invariance Attributes:
    obj: A string represents the path of a image
    """
    x, y = pyautogui.locateCenterOnScreen(obj)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.mouseDown(button=butt)
    pyautogui.mouseUp(button=butt)
    pyautogui.moveTo(50, 50)
    if printability:
        print('Click ' + obj + ' successfully!')


def click_xy(x: int, y: int, printability: bool = True, butt: str = 'left') -> None:
    """Click a location by given (x, y).
    """
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.mouseDown(button=butt)
    pyautogui.mouseUp(button=butt)
    pyautogui.moveTo(50, 50)
    if printability:
        print(f'Click ({x}, {y}) successfully!')


def find(obj: str, confidence: float = 0.8, printability: bool = True) -> Any:
    """Return the position of the object we want to search on the screen
    """
    location = pyautogui.locateOnScreen(obj, confidence)
    if location is not None:
        if printability:
            print('Find ' + obj + '!!!')
    else:
        if printability:
            print('Find ' + obj + ' FAILED :<')
    return location


def exist(obj: str, confidence: float = 0.8, printability: bool = True) -> bool:
    """Return true if find the object in the screen.
    """
    result = pyautogui.locateOnScreen(obj, confidence)
    if result is None:
        if printability:
            print(obj + ' didn\'t exist :<')
        return False
    else:
        if printability:
            print(obj + ' exist!!!')
        return True


def wait(obj: str, confidence: float = 0.8, times: int = 0) -> Any:
    """Waiting for a given object appeared on the screen.
    """
    location = None
    print('Still waiting occurrence of ' + obj + '...')
    if times != 0:
        loop = 0
        while loop < times:
            location = find(obj, confidence, printability=False)
            loop += 1
            if loop == times and location is None:
                print('Didn\'t find ' + obj + ' :<')
                return None
    else:
        loop = True
        while loop:
            location = find(obj, confidence, printability=False)
            if location is not None:
                loop = False

    print('Finally found ' + obj + '!!! Phew...')
    return location


def wait_and_click(obj: str, confidence: float = 0.8, times: int = 0) -> None:
    """Waiting for a given object and click it.
    """
    location = wait(obj, confidence, times)
    if location is not None:
        x, y = pyautogui.center(location)
        click_xy(x, y, printability=False)
        print('Click ' + obj + ' successfully!')
        return
    print('Oops...times up... :<')


def multiple_click(click_list: list) -> None:
    """Click a sequence of buttons
    """
    for button in click_list:
        wait_and_click(button)
        pyautogui.moveTo(50, 50)
        time.sleep(0.2)


def translate_name_to_pic(names: set[str]) -> set:
    """Return a set which is translated by
    the name of each champion, in a given set, to their path in picture/champ.
    """
    front = f'picture/champ/'
    back = f'.png'
    output = set()
    for name in names:
        output.add(front + name + back)
    return output


##########################
# Bot functions
##########################
find_match = 'picture/find_match.png'
accept = 'picture/accept.png'
begin_indicator = 'picture/begin_indicator.png'
ok = 'picture/ok.png'
setting = 'picture/setting.png'
surr_1 = 'picture/surrender_1.png'
surr_2 = 'picture/surrender_2.png'
exit_now = 'picture/exit_now.png'
play_again = 'picture/play_again.png'
my_self = 'picture/my_self.png'
test = 'picture/test.png'
# TEN_MINUTES = 605


def join_game() -> None:
    """ Click find match and accept until enter the game.
    """
    wait_and_click(find_match)
    wait_and_click(accept)
    print('Waiting the occurrence of picture/begin_indicator.png...')
    while not exist(begin_indicator, printability=False):
        if exist(accept, printability=False):
            click(accept)


def run_and_surr(games_interval: int, surr_time: int) -> None:
    """ Start game and surrender immediately after ten minutes.
    """
    while True:
        join_game()
        # Version 2
        # while not exist(my_self):
        #     if exist(accept):
        #         click(accept)
        # wait(begin_indicator)
        print('waiting ten minutes...')
        time.sleep(surr_time)
        # Use right click to click setting button
        # for ensure the cursor in the TFT window.
        click(setting, butt='right')
        pydirectinput.press('esc')
        multiple_click([surr_1, surr_2])
        time.sleep(games_interval)
        while exist(ok):
            click(ok)
            time.sleep(1)
        wait_and_click(play_again)
        print('')
        time.sleep(0.5)


def run_and_surr_party(games_interval: int, surr_time: int) -> None:
    """ Start game and surrender immediately after ten minutes.
    """
    while True:
        wait_and_click(accept)
        print('Waiting the occurrence of picture/begin_indicator.png...')
        while not exist(begin_indicator, printability=False):
            if exist(accept, printability=False):
                click(accept)
        print('waiting ten minutes...')
        time.sleep(surr_time)
        # Use right click to click setting button
        # for ensure the cursor in the TFT window.
        click(setting, butt='right')
        pydirectinput.press('esc')
        multiple_click([surr_1, surr_2])
        time.sleep(games_interval)
        while exist(ok):
            click(ok)
            time.sleep(1)
        wait_and_click(play_again)
        print('')
        time.sleep(0.5)


def auto_pick(build_list: set[str], games_interval: int) -> None:
    """Pick card in given set automatically.
    """
    champ_path_set = translate_name_to_pic(build_list)
    while True:
        is_end = False
        exit_clicked = False
        join_game()
        print('Starting pick champions in your build list...')
        while not is_end:
            for champ in champ_path_set:
                while exist(champ):
                    wait_and_click(champ, times=2)
            if exist(exit_now, printability=False):
                wait_and_click(exit_now)
                # exit_clicked = True
                time.sleep(games_interval)
                while exist(ok):
                    click(ok)
                    time.sleep(1)
                wait_and_click(play_again)
                is_end = True
            elif exist(ok, printability=False):
                while exist(ok):
                    click(ok)
                    time.sleep(1)
                wait_and_click(play_again)
                is_end = True
            elif exist(play_again, printability=False):
                wait_and_click(play_again)
                is_end = True

            # 此方法因不明原因不可用
            # if not is_end:
            #     while exist(ok):
            #         click(ok)
            #         time.sleep(1)
            #     if exit_clicked:
            #         wait_and_click(play_again)
            #         is_end = True
        print('')
        time.sleep(0.5)

import pyautogui
import time


class Ava():
    """Wrapper for Test Runs Creation"""
    def action(self, pos_x, pos_y, delay):
        pyautogui.moveTo(pos_x, pos_y) #Add Buton
        time.sleep(delay)
        pyautogui.click()

    
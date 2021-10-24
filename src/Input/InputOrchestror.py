import time
import pyautogui


class InputOrchestrator:
    
    def __init__(self, time: time, pyautogui: pyautogui):
        self._time = time
        self._pyautogui = pyautogui
        self._screen_size = self._pyautogui.size()

    def press_arrow_left(self, duration=0):
        self._press('left', duration)
        
    def press_arrow_right(self, duration=0):
        self._press('right', duration)
        
    def press_arrow_up(self, duration=0):
        self._press('up', duration)
        
    def press_arrow_down(self, duration=0):
        self._press('down', duration)
        
    def click_on_center(self, duration=0):
        self._click(0.5, 0.5, duration)
        
    def click_near_the_right_corner(self, duration=0):
        self._click(0.9, 0.1, duration)
        
    def _press(self, key, duration):
        self._pyautogui.keyDown(key)
        self._time.sleep(duration)
        self._pyautogui.keyUp(key)
        
    def _click(self, relative_x, relative_y, duration):
        self._pyautogui.moveTo(self._screen_size[0] * relative_x, self._screen_size[1] * relative_y, duration)
        self._pyautogui.click()
    
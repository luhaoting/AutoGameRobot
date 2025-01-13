import pyautogui
import time

class VirtualJoystick:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def move_to_center(self):
        pyautogui.moveTo(self.center_x, self.center_y, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')

    def move_joystick(self, x_offset, y_offset):
        pyautogui.moveTo(self.center_x, self.center_y, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.move(x_offset, y_offset, duration=1)
        pyautogui.mouseUp(button='left')

    def move_up(self):
        self.move_joystick(0, -100)

    def move_down(self):
        self.move_joystick(0, 100)

    def move_left(self):
        self.move_joystick(-100, 0)

    def move_right(self):
        self.move_joystick(100, 0)

    def move_up_right(self):
        self.move_joystick(100, -100)

    def move_up_left(self):
        self.move_joystick(-100, -100)

    def move_down_right(self):
        self.move_joystick(100, 100)

    def move_down_left(self):
        self.move_joystick(-100, 100)

def main():
    joystick = VirtualJoystick(center_x=500, center_y=500)
    joystick.move_to_center()
    time.sleep(2)

    joystick.move_right()
    time.sleep(2)

    joystick.move_up()
    time.sleep(2)

    joystick.move_to_center()

if __name__ == "__main__":
    main()

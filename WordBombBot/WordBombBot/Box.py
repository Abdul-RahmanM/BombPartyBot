import pyautogui
import keyboard


class Box:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = [0, 0]

    def get_box(self):
        for i in range(1, 3):
            if i == 1:
                print(f"Press [{i}] "
                      "when cursor is on the upper-left corner of the text box")
            else:
                print(f"Press [{i}] "
                      "when cursor is on the bottom-right corner of the text box")
            while not keyboard.is_pressed(str(i)):
                self.coords[i - 1] = pyautogui.position() # Returns pos as [(x,y), (x,y)]

        return (self.coords[0].x, self.coords[0].y,
                self.coords[1].x, self.coords[1].y)
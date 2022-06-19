import pyautogui
from PIL import ImageGrab
import keyboard

positions = [[663, 305, 664, 306], [663, 475, 664, 476], [663, 630, 664, 631], [663, 780, 664, 781], [663, 950, 664, 951],
            [1375, 305, 1376, 306], [1375, 475, 1376, 476], [1375, 630, 1376, 631], [1375, 780, 1376, 781], [1375, 950, 1376, 951]]

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
    for pos in positions:
        px = ImageGrab.grab(bbox=(pos)).load()
        color = px[0,0]
        if(color == (238, 141, 72)):
            print("click on ", pos, "with color ", color)
            pyautogui.click(pos[0], pos[1])
        
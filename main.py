import pyautogui
from PIL import ImageGrab
import keyboard

colors = {"improvements" : (238, 141, 72), "buyX" : (224, 139, 78), "managers label": (),"managers upgrades": (143, 188, 211)}

improvements_positions = [[663, 305], [663, 475], [663, 630], [663, 780], [663, 950],
            [1375, 305], [1375, 475], [1375, 630], [1375, 780], [1375, 950]]
business_positions = [[460, 260], [460, 430],[460, 580],[460, 740],[460, 900],
            [1150, 260], [1150, 430],[1150, 580],[1150, 740],[1150, 900]]
buyX_position = [1844, 41]
managers_label_position = [62, 623]
managers_position = [830, 650]
x_position = [1825, 100]

def buyImprovements():
    for improvemntPos in improvements_positions:
        color = px[improvemntPos[0], improvemntPos[1]]
        print("pos: ", improvemntPos, "color: ", color)
        if color != colors["improvements"]:
            continue
        print("click on ", improvemntPos[0], improvemntPos[1], "with color ", color)
        pyautogui.click(improvemntPos[0], improvemntPos[1], duration=0.1)

def clickBusiness():
    color = px[buyX_position[0], buyX_position[1]]
    if color == colors["buyX"]:
        for busionessPos in business_positions:
            pyautogui.click(busionessPos[0], busionessPos[1])

def managers():
    color = px[managers_label_position[0], managers_label_position[1]]
    if color == colors["managers label"]:
        pyautogui.click(managers_label_position[0], managers_label_position[1], duration=0.1)
        color = px[managers_position[0], managers_position[1]]
        if color == colors["managers upgrades"]:
            pyautogui.click(managers_position[0], managers_position[1], duration=0.1)

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
    px = ImageGrab.grab().load()
    buyImprovements()
    clickBusiness()
    managers()
    #pos = pyautogui.position()
    #print(pyautogui.position())
    #px = ImageGrab.grab().load()
    #print(px[pos.x, pos.y])

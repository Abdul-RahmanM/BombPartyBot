import pyautogui
import keyboard
import pytesseract
from pytesseract import image_to_string
from PIL import Image,ImageGrab
import cv2
from Box import Box

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Get dimensions
box = Box()
x1, y1, x2, y2 = box.get_box()

# ss of word
def screenShot():
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
    #img = cv2.imread('text.png')
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #_, th1 = cv2.threshold(img, 218, 255, cv2.THRESH_BINARY)
    return img

# Get the letters
def getLetters(th1):
    text = image_to_string(th1, lang="eng").replace("\n", "")
    if text == "":
        text = image_to_string(th1, lang="eng").replace("\n", "")
        return text
    else:
        return text

used_words = []

def main():
    answers = []
    text = getLetters(screenShot())
    print(text)
    with open('dict.txt') as f:
        contents = [line.replace("\n", "") for line in f.readlines()]
    for word in contents:
        if text in word:
            answers.append(word)
    max_len = -1
    for word in answers:
        if len(word) > max_len:
            if word not in used_words:
                max_len = len(word)
                longest_word = word
                used_words.append(longest_word)
        else:
            continue
    try:
        keyboard.write(longest_word)
    except UnboundLocalError:
        print("Error finding the word/could not read letters... TRY AGAIN")
    answers = []

# Get ss of the word

while True:
    if keyboard.is_pressed("["):
        main()
    if keyboard.is_pressed("esc"):
        quit()
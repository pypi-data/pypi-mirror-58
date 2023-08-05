"""
##################################################################################
ComCaveSnipper
This tool is doing your pin query for you.
@Author ginnie3112x  Version 1.0, 2020
ginnie3112x@gmail.com
##################################################################################
"""
import ctypes
import msvcrt
import mss.tools
from PIL import Image
from mss import mss
import pyautogui
import pytesseract
import _ctypes as ct

import time
from threading import Thread

# Please check the path to tessaract, which you need to install, see README.md
# initializes OCR/
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
title = 'Anwesenheitskontrolle'
# for testing
#title = 'Fotos'


# gets the screenshot from given pin display
def get_screenshots(box):
    with mss() as sct:
        # print(sct.monitors)
        pinbox = resize_box(box, 0, 0, 88, 250)

        # Get a screenshot of the box
        sct_img = sct.grab(pinbox)
        print(sct_img)

        # Create an Image
        img = Image.new("RGB", sct_img.size)

        # Best solution: create a list(tuple(R, G, B), ...) for putdata()
        pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
        img.putdata(list(pixels))

        # Save it!
        img.save('screenshot.png')

    return img


# "scans" the pin from screenshot
def get_pin(frame):
    try:
        pinlist = pytesseract.image_to_string(frame)
        return pinlist
    except ValueError:
        print('Can not read pin.')
        return -1


# gets the position of the window with title 'Anwesenheitskontrolle', if there is none returns Value -1
def get_pos_window():
    try:
        win = pyautogui.getWindowsWithTitle(title)
        return win[0].box
    except Exception:
        return -1


#defines the section of the window that is relevant for the pin
def resize_box(box_original, leftmargin, topmargin, rightmargin, lowermargin):
    pinbox = box_original[0] + leftmargin, box_original[1] + rightmargin, box_original[0] + box_original[2] + topmargin, \
             box_original[1] + box_original[3] - lowermargin
    return pinbox


#clicks on the number buttons, locating them with help of the function locateOnScreen(imagepath)
def click_mouse(imagepath):
    point = None
    try:
        point = pyautogui.locateCenterOnScreen(imagepath)
        if point is not None:
            num = imagepath.split('.')[0]
            pyautogui.click(point)
            print('Click on', num, 'Point:', point)
        else:
            print('No point found')

    except pyautogui.PyAutoGUIException:
        print('Could not locate image with number')



# checks the resolution of the screen because there are some issues with different images
def check_resolution():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    res = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    print('Screen resolution', res)
    return res

# switches the resolution for building the image path, you can add new resolution.
# in this case add some new snippets of the buttons, named number_resolutionkey.PNG without spaces
def switch_resolution(res_w):
    switcher = {
        1920: 'hd',
        1366: 'hdr',
        720: 'sd',
        640: 'vga'
    }
    return switcher.get(res_w[0])

# finally inserts the given PIN and clicks the send button
def insert_pin(bx):
    # Outputs the size of the boxed window
    print('The Size of the window:', bx)

    # gets the screenshot
    get_screenshots(bx)

    # loads the image to read the given pin
    imageLoad = Image.open('screenshot.png')
    pin = get_pin(imageLoad)

    #filter the pinlist for digits
    testpin = list(filter(lambda x: x.isdigit(), pin))
    if len(testpin) != 0:
        print('Your pin is', pin[0:4])

    resolution = check_resolution()
    res = switch_resolution(resolution)

    if res is None:
        res = ""

    # if the read character is a number/ digit
    for i in pin:
        if i.isdigit():

            # builds the path
            imagepath = i + res + '.PNG'
            print('Path to images', imagepath)

            # tries to click the right number button
            try:
                click_mouse(imagepath)
            except Exception:
                print('ERROR! Something went wrong.\nCould not click.')
    try:

        if len(pin) == 4:
            # Path of the sending button
            imagepath = 'send.PNG'
            click_mouse(imagepath)
            print('And.....')
            print('Ready!')
        else:
            imagepath = 'loschenhd.PNG'
            for i in range(len(pin)):
                click_mouse(imagepath)
    except Exception:
        print('Could not send nor delete')



# run the Thread
def run():
    bx = None
    print('Tool is running!')
    print('Take care of your mouse. If a query is open it will go to pin number block')
    # Continuously checks whether the window is open
    while True:
        if get_pos_window() == -1:
            pass
        else:
            # Waits until the window is load
            time.sleep(5)

            try:
                # the position of the window
                bx = get_pos_window()

            except Exception:
                print('ERROR! Window is closed! Tool is still running')

            try:
                # if is load, goes on with inserting pin
                insert_pin(bx)

            except Exception:
                print('ERROR! Pin could not be inserted! Tool is still running')


if __name__ == '__main__':
    print('Welcome to ComCaveSnipper!')
    print('Check this out. This tool is doing your pin query for you. ')
    answer = input('Wanna try it? Press [Y/N] and Enter!\n')
    print('Press any key to exit the app.')
    while True:
        if answer == 'Y' or answer == 'y':
            print('Tool is starting ... ')
            print('Waiting for query ... ')
            # Makes a Thread and start the run method
            t = Thread(target=run)
            t.start()
            break
        elif answer == 'N' or answer == 'n':
            exit(-1)

    while True:
        if msvcrt.kbhit():
            print('Quit.')
            exit(-1)

from PIL import ImageGrab
from PIL import ImageOps
from PIL import Image

import pyautogui
import time
import numpy


class Coordinates():
    replay_button = (480, 500)
    dinosaur_coordinates = (188, 504)
    # x coordinates of tree = 300
    # y shortree = 528 smallest part


def restart_game():
    pyautogui.click(Coordinates.replay_button)


def press_space():
    pyautogui.keyDown('space')
    time.sleep(0.009)
    print('Jump')
    pyautogui.keyUp('space')


def image_grab():
    data_color = set()
    box = (Coordinates.dinosaur_coordinates[0] + 112 - 17, Coordinates.dinosaur_coordinates[1] - 10,
           Coordinates.dinosaur_coordinates[0] + 112 + 40, Coordinates.dinosaur_coordinates[1] + 40)

    new_box = (284, 540, 287, 545)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    # get_colors = Image.Image.getcolors(image)
    get_colors = Image.Image.getcolors(gray_image)
    image_array = numpy.array(get_colors)

    print(numpy.sum(image_array))

    return numpy.sum(image_array)


def main():
    restart_game()
    while True:
        if image_grab() != 3097:
            press_space()
            time.sleep(0.05)


if __name__ == "__main__":
    # restart_game()
    main()

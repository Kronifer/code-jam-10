import random
import typing
from string import ascii_lowercase

from PIL import Image


def generate_alphabet(key: str) -> dict:
    """Generates the A-channel offset of each character in the alphabet using a pre-set key."""
    random.seed(key)
    alphabet = {i: 0 for i in ascii_lowercase}
    alphabet[" "] = 0
    for i in alphabet.keys():
        value = random.randint(1, 28)
        if value in alphabet.values():
            while True:
                value = random.randint(1, 28)
                if value not in alphabet.values():
                    break
        alphabet[i] = value
    return alphabet


def write_message(image: Image.Image, message: str, key: str) -> typing.Tuple[Image.Image, bool]:
    """
    Writes the given message to the source image given using the generated A-channel offsets.

    Also supplies a boolean to clarify if the message was successfully written to the image.
    """
    alphabet = generate_alphabet(key)
    if image.mode != "RGBA":
        image = image.convert("RGBA")
    if image.size[0] * image.size[1] < len(message):
        return image, False  # Too large to encode message, so return original image and throw error to client
    xc = []
    yc = []
    coords = []
    for i in range(len(message)):
        xc.append(random.randint(0, image.size[0]))
        yc.append(random.randint(0, image.size[1]))
    xc.sort()
    yc.sort()
    for i in range(len(message)):
        coords.append((xc[i], yc[i]))
    for i in range(len(message)):
        pixel = list(image.getpixel(coords[i]))
        pixel[-1] -= alphabet[message[i]]
        image.putpixel(coords[i], tuple(pixel))
    return image, True


def read_message(image: Image.Image, key: str) -> str:
    """Reads a message from an image encoded with write_message."""
    alphabet = generate_alphabet(key)
    message = ""
    for i in image.getdata():
        if i[-1] != 255:
            message += list(alphabet.keys())[list(alphabet.values()).index(255 - i[-1])]
    return message

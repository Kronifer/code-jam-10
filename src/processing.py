import random
import typing

from PIL import Image

ASCII_VALUES = list(range(97, 123)) + [32, 33, 44, 46]  # "a"-"z", " ", "!", ",", "."


def generate_alphabet(key: str) -> dict:
    """Generates the A-channel offset of each character in the alphabet using a pre-set key."""
    random.seed(key)
    alphabet = {}
    for i in ASCII_VALUES:
        value = random.randint(1, len(ASCII_VALUES) + 1)
        while value in alphabet.values():
            value = random.randint(1, len(ASCII_VALUES) + 1)
        alphabet[chr(i)] = value
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
        print("Your message is too long.")
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
    for i, letter in enumerate(message):
        if not (ord(letter) in ASCII_VALUES):
            print("Oops. The message contains an invalid character.")
            return image, False
        pixel = list(image.getpixel(coords[i]))
        pixel[-1] -= alphabet[letter]
        image.putpixel(coords[i], tuple(pixel))
    return image, True


def read_message(image: Image.Image, key: str) -> str:
    """Reads a message from an image encoded with write_message."""
    try:
        alphabet = generate_alphabet(key)
        message = ""
        for i in image.getdata():
            if i[-1] != 255:
                message += list(alphabet.keys())[list(alphabet.values()).index(255 - i[-1])]
        return message
    except ValueError as ve:
        return f"ValueError: {ve}. You have entered an invalid key."

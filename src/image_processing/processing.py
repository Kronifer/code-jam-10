import random
from string import ascii_lowercase

from PIL import Image


def generate_alphabet(key: str) -> dict:
    """Generates the A-channel offset of each character in the alphabet using a pre-set key."""
    random.seed(key)
    alphabet = {i: 0 for i in ascii_lowercase}
    alphabet[" "] = 0
    for i in alphabet.keys():
        alphabet[i] = random.randint(0, 30)
    return alphabet


def write_message(image: Image.Image, message: str, alphabet: dict) -> Image.Image:
    """Writes the given message to the source image given using the generated A-channel offsets."""
    pass  # TODO: Implement

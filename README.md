# Steganography Center
The Wheels of Cheese submission for [Python Discord's Summer Code Jam 2023](https://www.pythondiscord.com/events/code-jams/10/). You can view a live demo of the project [here](https://kronifer.is-a.dev/)!

https://github.com/Kronifer/code-jam-10/assets/44979306/b8f102e6-a1cf-4047-83f5-da9d433f4d19

## Steganography Methods
### RGB
Generates unique colors that correspond to characters using a user-supplied key, and places those colours in the image based on the characters in the message that the user provided.
Example image: ![image](https://github.com/Kronifer/code-jam-10/assets/44979306/0f0f8af4-e3e1-4797-98c5-06c8371828eb)
- Key: stegocenter
- Message: RGB Encoded Message
### Alpha Channel
Generates unique alpha channel offsets that correspond to characters using a user-supplied key, and applies those to random pixels in a user-supplied image to encode a secret message. **NOTE**: Images with non-opaque transparency will not work for this!
Example image: ![image](https://github.com/Kronifer/code-jam-10/assets/44979306/e907e267-1852-45cc-b840-efd04fb45459)
- Key: steganocenter
- Message: Transparency Encoded Message

## Known Issues
- Using A-Channel encoding will very rarely throw an Internal Server Error. This is due to an oversight in selecting pixels for encoding messages and will occur extremely occasionally. If this happens, try very slightly changing your key. We apologize for not fixing this before the deadline but as the issue suggests it didn't come up in testing until after the coding portion had ended.

## Setup
```sh
git clone https://github.com/kronifer/code-jam-10
cd code-jam-10
poetry install
```

## Running the Project
Windows
```sh
poetry run waitress-serve --host "127.0.0.1" src.website:app
```
Linux
```sh
poetry run gunicorn src.website:app
```

## Contributors
[Kronifer](https://github.com/kronifer) - Team Leader

[Today100](https://github.com/Today100) - Frontend

[ilcheese2](https://github.com/ilcheese2) - Backend

[Chooky](https://github.com/JoelKirkby) - Backend

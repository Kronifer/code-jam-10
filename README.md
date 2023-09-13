# Steganography Center
The Wheels of Cheese submission for [Python Discord's Summer Code Jam 2023](https://www.pythondiscord.com/events/code-jams/10/).
![image](https://github.com/Kronifer/code-jam-10/assets/44979306/d4d084b4-df06-402b-9643-bac8c2697081) (put video of project here soon)

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

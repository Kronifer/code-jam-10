# Steganography Center
The Wheels of Cheese submission for [Python Discord's Summer Code Jam 2023](https://www.pythondiscord.com/events/code-jams/10/).
https://github-production-user-asset-6210df.s3.amazonaws.com/44979306/267836697-88b86151-e1ef-497e-973e-abc824de1120.mp4
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

# Code Jam 10

## Dev Setup

```sh
$ pip install poetry # Installs poetry to your system if it is not already
$ poetry install # Installs the project in a virtual environment
$ poetry run pre-commit install # Installs pre-commit, which will prevent you from committing should your code not pass linting
```

## Programming
Make sure your commit message follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
```sh
$ poetry shell # Opens the virtual environment in your shell, allowing you to access the installed dependencies
# Make whatever changes
$ git add .
$ poetry run task format # Formats your code using black and sorts your import using isort. DO THIS BEFORE COMMITTING!
$ git commit -m "message" # Commits your code to git. Make sure you format or your commit will fail!
$ git push # Pushes to your current remote branch
```

Contributors, please let me know if any instructions are unclear!

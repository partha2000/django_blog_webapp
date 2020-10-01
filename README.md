# django_blog_webapp
A blog webapp to get started with django

## Setting up the environment
_Always make sure you have python 3 and are using virtualenv to install and manage your packages_
1. `pip3 install virtualenv`	-> Install the virtualenv library
2. `virtualenv .venv`		-> Create a virtual environment
3. `source .venv/bin/activate`	-> Get inside the virtual environment
4. `pip install --upgrade pip`	-> get upgraded to pip3
5. Thereafter install all the packages as per the reqirements.txt
6. If you add any new packages then export a new `requirements.txt` file with this
`pip3 freeze > requirements.txt`

__NOTE :__ If you are using vscode then you will have to activate the virtual environment
 interpreter. Follow the steps given below:
* enter `code .` in the terminal and then a new VS opens. Ctrl+Shift+P -> Select Interpreter select the environment that starts with `./env` or `.\env` run Ctrl+Shift+` to activate it

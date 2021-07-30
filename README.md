## 🐍 Python-Flask Webapp with persistent database

- Ninth example project from [Udemy course](https://www.udemy.com/course/the-python-mega-course/)
- Uses Flask and SQLAlchemy to create a webapp with a persistent database, as well as MIMEText and smtplib to handle email responses to user submissions


## 📓 Comments

- Flask is a really good framework, it is extremely easy to use, but provides a high level of control
- Using a virtualenv makes sense as a way to localise library installations and manage versions between different projects, but also seems limited in that you have to set the source to the virtualenv in CLI every time you open the editor, unsure if there is a way to permanently change this yet, or most likely you would deploy the app to an environment that has librarys installed


## 💻 Running the app

- Clone this repo to your local machine, and then make sure you have access to the libraries in the requirements.txt file, you can either directly install using ``` pip install (libraryname) ``` or you can use a virtualenv, by running ``` python -m venv (env name) ```, and then using the virtualenv to install the libraries local to the project repo
  - Navigate to the project directory and use ``` virtual/scripts/pip install (library name) ```
  - This is a localised install and will not conflict with other installs/ let you set a version
  - Then you need to use ``` source virtual/Scripts/activate ``` to tell python to use this virtualenv as the source
 - Navigate to the directory, and then use ``` python app.py  ``` to run the script, your terminal will confirm the server is running and give you a localhost port to alt-click
- The browser will launch, enter your email and height to receive an email response






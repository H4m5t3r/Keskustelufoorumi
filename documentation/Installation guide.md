# Installation guide
To download and run the application on Linux, please follow the steps below.

## Downloading the project
To download this project, click on the green "Clone or download"-button that can be found on the right side of the screen on the project's front page. Choose "Clone with HTTPS" and click on "Download ZIP". The ZIP folder can now be found in your Downloads folder on your computer.

## Unpacking and setting up the project
Extract the project from the ZIP folder. Now use the terminal to navigate to the extracted folder. You should now be in the folder "Keskustelufoorumi-master". Use the commands below to install a virtual environment and the required dependencies to be able to run the project. If you do not have Python installed, please download it from the [Python downloads page](https://www.python.org/downloads/).

**Create a virtual environment**
```
$ python3 -m venv venv
```
After you have created a virtual environment you can start it with the following command:
```
$ source venv/bin/activate
```
The virtual environment needs to be activated to run the application. It will be indicated by the text `(venv)` in the terminal like in this example:
```
$ (venv) ~/Keskustelufoorumi$
```
Always remember to activate the virtual environment before running the application. Otherwise it will not start.

**Update `pip`, which is used to get the required dependencies**
```
$ pip install --upgrade pip
```

**Install the project's dependencies**

The following commands will install required dependencies that the program needs for certain operations. This program uses Flask. Please note that all of these commands need to be run in the project folder.
```
$ install Flask
```
```
$ pip install flask-sqlalchemy
```
```
$ pip install flask-bcrypt
```
```
$ pip install flask-login
```
```
$ pip install flask-wtf
```

## Run the project
After all dependencies have been installed you should be able to run the application with the following command:
```
$ python run.py
```
If you open a web browser and go to `http://localhost:5000/` you you should see the starting page with a greeting message.

## Setting up the app
Once the app is running you can log in with the administrator account's login details. This account is created automatically as well as a default message category called "No category". You can find the administrator account's login details on the project's [front page](https://github.com/H4m5t3r/Keskustelufoorumi). Note that you should change the password after logging in if you plan to use the app with other people since anyone with the password can access the administrator account. Once you have signed in this can be done by clicking on "Change password" in the upper right corner.

## Using the app
If you completed the steps listed above you should now have set up the application successfully and can start using it. For more information, please refer to the [user manual](https://github.com/H4m5t3r/Keskustelufoorumi/blob/master/documentation/User%20manual.md).

## Setting up the app in Heroku

To set up the app on the remote service Heroku you first need to install Gunicorn with the following command:
```
$ pip install gunicorn
```
Before you continue, create an account in Heroku and make sure you have the Heroku tools [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

Log in to Heroku and create a new app by clicking on "New" in the upper right corner and choose "Create new app". Choose a name for the app, choose your region and click on "Create app". After this, choose the app and click on "Deploy". Scroll down to "Deploy using Heroku Git. There you will find instructions on how to upload the app to Heroku. The steps will also be listed here.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```
$ heroku login
```


### Create a new Git repository
Initialize a git repository:
```
$ git init
$ heroku git:remote -a *name*
```
`*name*` should be replaced with the name you chose for your app.

Then add the project to the repository and push it.
```
$ git add .
$ git commit -am "initial commit"
$ git push heroku master
```
Wait for Heroku to finish. After that you should find the application on this website:

https://git.heroku.com/-name-.git

where `-name-` should be replaced with the name you chose. The address should also be displayed in the terminal.

Add the Heroku app to the local application
```
heroku config:set HEROKU=1
```
and create a Heroku database
```
heroku addons:add heroku-postgresql:hobby-dev
```
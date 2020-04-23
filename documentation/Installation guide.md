# Installation guide
To download and run the application on Linux, please follow the steps below.

## Downloading the project
To download this project, click on the green "Clone or download"-button that can be found on the right side of the screen on the project's front page. Choose "Clone with HTTPS" and click on "Download ZIP". The ZIP folder can now be found in your Downloads folder on your computer.

## Unpacking and setting up the project
Extract the project from the ZIP folder. Now use the terminal to navigate to the extracted folder. You should now be in the folder "Keskustelufoorumi-master". Use the commands below to install a virtual environment and the required dependencies to be able to run the project. If you do not have Python installed, please download it from the [Python downloads page](https://www.python.org/downloads/).

**Create a virtual environment**
```
python3 -m venv venv
```
After you have created a virtual environment you can start it with the following command:
```
source venv/bin/activate
```
The virtual environment needs to be activated to run the application. It will be indicated by the text `(venv)` in the terminal like in this example:
```
(venv) ~/Keskustelufoorumi$
```
Always remember to activate the virtual environment if it it not activated before running the application.

**Update `pip`, which is used to get the required dependencies**
```
pip install --upgrade pip
```

**Install the project's dependencies**
The following commands will install required dependencies that the program needs for certain operations. This program uses Flask.
```
pip install Flask
```
```
pip install flask-sqlalchemy
```
```
pip install flask-bcrypt
```
```
pip install flask-login
```
```
pip install flask-wtf
```

## Run the project
After all dependencies have been installed you should be able to run the application with the following command:
```
python run.py
```
If you open a web browser and go to `http://localhost:5000/` you you should see the starting page with a greeting message.

## Setting up the app
Once the app is running you have to set up the administrator account and create the default message category "No category".

**IMPORTANT: The administrator account is defined as the account with the ID 1, which means that the first account that is created automatically becomes the administrator. You can set the name and username to whatever you want but make sure that you do not create any other accounts before this account has been created. The same goes for the default category "No category".**

To create the administrator account, click on the "Create an account" link in the upper right corner on the chat forum. Fill in the account details and click on "Create account".

After creating the admin account you can sign in using the details you just created the administrator account with. To create the default message category, click on "Add a category" on the top bar. Write "No category" in the text field and click on "Add a new category". This "category" will not appear in the list below the category form so to make sure it was added, click on "Add a message" on the top bar. If the default category was successfully created it should appear as an alternative in the category field.

## Using the app
If you completed the steps listed above you should now have set up the application successfully and can start using it. For more information, please refer to the [user manual](https://github.com/H4m5t3r/Keskustelufoorumi/blob/master/documentation/User%20manual.md).
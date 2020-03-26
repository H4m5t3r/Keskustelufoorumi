# Chat forum
In this project I will create a chat forum where the user can sign in and send messages.

### Planned features:
Users will be able to
* [ ] create, edit and delete an account
* [x] sign in
* [x] add messages
* [ ] create and edit subjects
* [ ] filter messages by subjects
* [ ] add answers to other messages
* [ ] delete their own messages
* [ ] like or dislike other users' messages

### Part 1
The subject for the project has been chosen and a GitHub repository has been created. A database diagram was also added.

### Part 2
At the moment the user can add messages to the database and list all messages. I added a like button which I probably will make changes to later. A better way of implementing it could be to store how many people have liked a certain message as an integer instead of just having a boolean variable. I just wanted to make sure that the data in the database could be changed. Examples of user cases have been added to the file named "User stories".

### Part 3
Changes:
* The user can now create an account and sign in with their user details.
* Validators have been added to the forms that are used for writing a message and creating a new account. These validators check that none of the text fields are empty.
* Writing a message now also requires the user to be signed in.

Planned features:
* A button for removing a message is planned, but has not been completed yet. This feature has been temporarily removed because it made the application malfunction.
* An option to edit a message
* An anministrator account may be added in during the coming weeks. This account would be able to delete a message even if it has not been created with it.

#### Useful links:
[User stories](https://github.com/H4m5t3r/Keskustelufoorumi/blob/master/documentation/User%20stories.md)

[Database diagram](https://github.com/H4m5t3r/Keskustelufoorumi/blob/master/documentation/Database%20diagram.png)

[Heroku app](https://tsoha-k2020-keskustelufoorumi.herokuapp.com/)

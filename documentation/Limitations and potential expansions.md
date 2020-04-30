## Limitations and potential expansions

For some reason reason the view_likes function that lets users see who has liked a message does not work in Heroku. It works locally but when it is used in Heroku the user gets an error message. The page looks like this when it works:

![view_likes](https://github.com/H4m5t3r/Keskustelufoorumi/blob/master/documentation/view_likes%20demo.png)

Features that could be added to improve the user experience:

* Deleting accounts
* Deleting categories
* More validators to make sure users use good passwords
* Adding more error messages
* Making users able to change their name
* Giving the administrator information about rows in the tables (when they were created, when they were modified or deleted etc.)
* Adding more roles

Deleting accounts could be done easily by just deleting all messages and other information related to the account but it would be better to implement a feature that changes the name to "Deleted account" and makes the account go into a sleep state so that no one can access it. This way the posted messages would still remain on the chat forum.

Right now forms give error messages but there are no flash messages that for example tell the user they were successfully logged in. This feature was never implemented beacuse of lack of time.

## As a user I can participate in discussions on the chat forum page.

### **As a user without an account I have limited access to the chat forum's features**

As a user I can list all the posted messages.
```
SELECT * FROM Message;
```

As a user I can filter messages by their category.
```
SELECT * FROM Message WHERE Message.category_id = :category_id
```

As a user I can open messages and read them.
```
SELECT * FROM Message WHERE Message.id = :message_id;
```

As a user I can see who has written the message.
```
SELECT Account.name FROM Account WHERE Account.id = :writer_id;
```

As a user I can see what category has been chosen for a message.
```
SELECT Category.name FROM Category WHERE Category.id = :category_id;
```

As a user I can read the answers to a message.
```
SELECT * FROM Answer WHERE Answer.message_id = :message_id;
```

As a user I can see how many likes a message has.
```
SELECT COUNT(*) FROM Like WHERE Like.message_id = :message_id;
```

As a user I can see who has liked a message.
```
SELECT Account.name from Account WHERE Account.id IN (SELECT Like.account_id WHERE Like.message_id = :message_id)
```

As a user I can create an account to be able to post messages on the chat forum.
```
INSERT INTO Account (name, username, password) VALUES (:name, :username, :hashed_password)
```

### **As a user with an account I have access to more features**

As a signed in user I can change my password.
```
UPDATE Account SET password = :new_password WHERE Account.id = :current_user.id
```

As a signed in user I can write a new message so that other users can read it.
```
INSERT INTO message (date_created, date_modified, name, messagetext, account_id, category_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, :title, :messagetext, :current_user.id, :category_id)
```

As a signed in user I can choose a category from the ones available for the messages I write.
```
SELECT Category.name FROM Category;
```

As a signed in user I can edit my own messages.
```
UPDATE message SET date_modified=CURRENT_TIMESTAMP, messagetext=:new_messageText, category_id=:new_category_id WHERE message.id = :message_id;
```

As a signed in user I can delete my own answers.
```
DELETE FROM Message WHERE Message.id = :message_to_delete
```

As a signed in user I can increase the number of likes a message has by one by liking it.

```
INSERT INTO "like" (account_id, message_id) VALUES (:current_user.id, :message_id);
```

As a signed in user I can remove my like from a message if I have liked it.
```
DELETE FROM Like WHERE Like.account_id = :current_user.id AND Like.message_id = :message_id;
```

As a signed in user I can add answers to messages.
```
INSERT INTO Answer (date_created, date_modified, answertext, account_id, message_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, :answertext, :current_user.id, :message_id)
```

As a signed in user I can edit my own answers.
```
UPDATE Answer SET date_modified=CURRENT_TIMESTAMP, answertext=:newAnswerText WHERE Answer.id = :answer_id
```

As a signed in user I can delete my own answers.
```
DELETE FROM Answer WHERE Answer.id = :answer_to_delete
```

As a signed in user I can create new message categories.
```
INSERT INTO category (date_created, date_modified, name, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, :category_name, :current_user.id)
```

### **As an administrator I have privileges**

As an administrator I can delete messages even if I am not the one who posted them.
```
DELETE FROM Message WHERE Message.id = :message_to_delete
```

As an administrator I can delete answers even if I am not the one who posted them.
```
DELETE FROM Answer WHERE Answer.id = :answer_to_delete
```

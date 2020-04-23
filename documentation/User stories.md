## Available features

**As a user I can participate in discussions on the chat forum page.**

**As a user without an account I have limited access to the chat forum's features**

As a user I can list all the posted messages.
```
message = Message.query.all(), account = User.query.all()
```

As a user I can open messages and read them.
```
message = Message.query.filter_by(id=message_id).first(), 
account = User.query.filter_by(id=writer_id).first(), 
category = Category.query.filter_by(id=category_id).first(), 
answers = Answer.query.filter_by(message_id=message_id),
answerwriters = User.query.all()
```

As a user I can create an account to be able to post messages on the chat forum.
```
form = SignUpForm()
```
```
t = User(form.name.data, form.username.data, hashed_password)
db.session().add(t)
db.session().commit()
```

**As a user with an account I have access to more features**

As a signed in user I can write a new message so that other users can read it.
```
form = MessageForm()
```
```
form = MessageForm(request.form)
t = Message(form.name.data, form.messagetext.data)
t.account_id = current_user.id
t.category_id = request.form['category_id']

db.session().add(t)
db.session().commit()
```

As a signed in user I can add a category to the messages I write.
```
query_factory = lambda: models.Category.query.all()
```

As a signed in user I can edit my own messages.
```

```

As a signed in user I can increase the number of likes a message has by one by liking it or remove my like from it if I have already liked it.

```

```

As a signed in user I can add answers to messages.
```

```

As a signed in user I can delete my own messages.
```

```

As a signed in user I can create new message categories.
```

```


**As an administrator I have privileges**

As an administrator I can delete messages even if I am not the one who posted them.
```

```

## Planned features

As a user I can filter messages by their category.

As a signed in user I can change my password.

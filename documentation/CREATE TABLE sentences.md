The account table:
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (username)
)
```

The category table:
```
CREATE TABLE category (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
```

The message table:
```
CREATE TABLE message (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	messagetext VARCHAR(144) NOT NULL, 
	liked BOOLEAN NOT NULL, 
	likes INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (liked IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
)
```

The answer table:
```
CREATE TABLE answer (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	answertext VARCHAR(144) NOT NULL, 
	liked BOOLEAN NOT NULL, 
	likes INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	message_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (liked IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(message_id) REFERENCES message (id)
)
```

The likes table:
```
CREATE TABLE "like" (
	id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	message_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(message_id) REFERENCES message (id)
)
```
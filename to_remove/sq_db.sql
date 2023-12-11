PRAGMA foreign_key=on;

CREATE TABLE IF NOT EXISTS users(
id integer PRIMARY KEY AUTOINCREMENT,
email text NOT NULL,
firstName text NOT NULL,
lastName text NOT NULL,
gender text NOT NULL,
birthday text NOT NULL,
address text NOT NULL,
username text NOT NULL,
password text NOT NULL,
phoneNumber text NOT NULL
);

CREATE TABLE IF NOT EXISTS usersProfile(
userId integer,
avatar BLOB DEFAULT NULL,
description text NOT NULL,
englishLevel text NOT NULL,
groups text NOT NULL,
FOREIGN KEY (userId) REFERENCES users(id)
);

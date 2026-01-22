CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
matric_no TEXT NOT NULL,
password TEXT NOT NULL,
role TEXT NOT NULL
);


CREATE TABLE exeats (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
reason TEXT,
departure_date TEXT,
return_date TEXT,
status TEXT,
created_at TEXT
);
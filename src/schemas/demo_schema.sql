DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    review_score INTEGER NOT NULL, 
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS result;

CREATE TABLE result (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    formula STRING CHECK (formula in ('ack', 'fact', 'fibo')),
    x1 INTEGER,
    x2 INTEGER,
    y INTEGER
);
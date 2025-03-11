CREATE TABLE IF NOT EXISTS user (
    id              INTEGER PRIMARY KEY AUTOINCREMENT ,
    username        TEXT NOT NULL UNIQUE,
    email           TEXT,
    hashed_password TEXT NOT NULL,
    salt            TEXT NOT NULL,
    creation_date   TEXT,
    is_admin        INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE IF NOT EXISTS poll (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    public_id       TEXT NOT NULL UNIQUE,
    hashed_password TEXT,
    creation_date   TEXT,
    open_date       TEXT,
    expiration_date TEXT,
    type            INTEGER
);
CREATE TABLE IF NOT EXISTS code (
    election_id     TEXT NOT NULL,
    hashed_code     TEXT NOT NULL,
    FOREIGN KEY (election_id)
        REFERENCES election (id)
)
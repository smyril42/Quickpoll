CREATE TABLE IF NOT EXISTS user (
    id              TEXT PRIMARY KEY,
    username        TEXT PRIMARY KEY,
    hashed_password TEXT NOT NULL,
    email           TEXT,
    creation_date   TEXT
);
CREATE TABLE IF NOT EXISTS election (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    public_id       TEXT PRIMARY KEY,
    hashed_password TEXT,
    creation_date   TEXT,
    expiration_date TEXT,
    type            INTEGER
);
CREATE TABLE IF NOT EXISTS code (
    election_id     TEXT NOT NULL,
    hashed_code     TEXT NOT NULL,
    FOREIGN KEY (election_id)
        REFERENCES election (id)
)
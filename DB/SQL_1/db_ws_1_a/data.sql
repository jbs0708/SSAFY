PRAGMA table_info('songs');
SELECT * FROM songs;

CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    album TEXT,
    genre TEXT,
    duration INTEGER
);


INSERT INTO
    songs (title, artist, album, genre, duration)
VALUES
    ('title1', 'artist1', 'Album1', 'Genre1', 200),
    ('title2', 'artist2', 'Album2', 'Genre2', 400),
    ('title3', 'artist3', 'Album3', 'Genre3', 600),
    ('title4', 'artist4', 'Album4', 'Genre4', 500),
    ('title5', 'artist5', 'Album5', 'Genre5', 300);


UPDATE
    songs
SET
    title = 'update Title'
WHERE
    id = 1;
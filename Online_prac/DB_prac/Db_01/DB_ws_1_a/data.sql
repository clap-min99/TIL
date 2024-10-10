CREATE TABLE songs(
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  album TEXT NOT NULL,
  genre TEXT NOT NULL,
  duration INTEGER NOT NULL
)

INSERT INTO songs(title, artist, album, genre, duration)
VALUES
('Song1', 'Artist 1', 'Album 1', 'Pop', '200'),
('Song2', 'Artist 2', 'Album 2', 'Rock', '300'),
('Song3', 'Artist 3', 'Album 3', 'Hip Hop', '250'),
('Song4', 'Artist 4', 'Album 4', 'Electronic', '180'),
('Song5', 'Artist 5', 'Album 5', 'R&B', '320');

UPDATE songs
SET title = 'update Title'
WHERE id = 1;
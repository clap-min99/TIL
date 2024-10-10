-- Active: 1728548050919@@127.0.0.1@3306

SELECT
  genre, COUNT(*) as count
FROM
  songs
GROUP BY
  genre;

SELECT
  genre, COUNT(*) AS count, AVG(duration) AS average_duration
FROM
  songs
GROUP BY
  genre;
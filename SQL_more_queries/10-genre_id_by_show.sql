-- Task 10: List every show title and its genre_id, for shows having at leat one genre
SELECT
    tv_shows.title,
    tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
    ON tv_shows.id = tv_shows_genres.tv_show_id
ORDER BY
    tv_shows.title ASC,
    tv_shows_genres.genre_id ASC;

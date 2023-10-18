-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
    tv_genres.name AS genre,
    COUNT(tv_shows.title) AS number_of_shows
FROM
    tv_genres
    LEFT JOIN tv_shows ON tv_genres.id = tv_show_genres.show_id
ORDER BY number_of_shows
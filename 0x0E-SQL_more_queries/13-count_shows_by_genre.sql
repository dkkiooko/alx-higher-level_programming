-- list all genres from hbtn_0d_tvshows and displays number of shows linked to each other
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres 0N tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;


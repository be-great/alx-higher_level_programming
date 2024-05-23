-- lists all shows contained in database
SELECT tv_shows.title - tv_show_genres.genre_id from tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title asc, tv_show_genres.genre_id asc;

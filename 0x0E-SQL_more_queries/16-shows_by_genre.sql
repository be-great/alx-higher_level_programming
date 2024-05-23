-- script that lists all shows, and all genres linked to that show.
SELECT title, name FROM tv_shows
left join tv_show_genres on tv_shows.id = tv_show_genres.show_id
left join tv_genres on tv_show_genres.genre_id = tv_genres.id ORDER BY title ASC, name ASC;

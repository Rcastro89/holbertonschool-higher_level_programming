-- dumps
SELECT * FROM tv_genres;
SELECT * FROM tv_show_genres;
SELECT * FROM tv_shows;
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

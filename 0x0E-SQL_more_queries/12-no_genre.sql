-- left is NULL join
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

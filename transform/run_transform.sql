DROP TABLE IF EXISTS analytics.song_popularity CASCADE;

CREATE TABLE analytics.song_popularity AS
SELECT
    artist,
    song,
    genre,
    COUNT(*) AS play_count,
    AVG(duration_sec) AS avg_duration
FROM music_events
GROUP BY artist, song, genre;
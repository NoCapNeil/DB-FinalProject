import csv
from cs50 import SQL
open("mydatabase.db","w").close()
database = SQL("sqlite:///mydatabase.db")

database.execute("CREATE TABLE my_songs(song_id INT PRIMARY KEY, song_name TEXT, song_year INT)")
database.execute("CREATE TABLE Artist(Artist_id INT PRIMARY KEY, Artist_name TEXT, feature INT, singles INT)")
database.execute("CREATE TABLE Album(song_id, Artist_id, FOREIGN KEY(song_id) REFERENCES my_songs(song_id) FOREIGN KEY(Artist_id) REFERENCES Artist(Artist_id))")

with open("music_data.csv","r")as file:
    reader = DictReader(file)

    for rows in reader:
        songs = row["song_name"]
        albums = row["singles"]

        database.execute("INSERT INTO my_songs(song_name) VALUES (?)",songs)
        database.execute("INSERT INTO Artist(Artist_name) VALUES (?)", albums)
        database.execute("INSERT INTO album(song_name, Artist_name) VALUES ((SELECT song_name FROM my_songs WHERE song_year = ?), (SELECT Artist_name FROM Artist WHERE feature = ?))", songs, albums )
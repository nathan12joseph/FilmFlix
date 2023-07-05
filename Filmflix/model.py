import sqlite3 as sql


class filmflix_db:

    def __init__(self):
        self.connection = sql.connect("filmflix.db")
        self.cursor = self.connection.cursor()

    def insert_film(self, *args):
        with self.connection:
            self.cursor.execute(
                f"""INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
                VALUES ('{args[0][0]}', '{args[0][1]}', '{args[0][2]}', '{args[0][3]}', '{args[0][4]}');""")

    def update_film(self, *args):
        with self.connection:
            self.cursor.execute(f"""UPDATE tblfilms SET title = '{args[0][0]}', yearReleased = '{args[0][1]}',
                                rating = '{args[0][2]}', duration = '{args[0][3]}', genre = '{args[0][4]}'
                                WHERE filmID = {args[0][5]}""")

    def delete_film(self, filmID):
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM tblfilms WHERE filmID = {filmID}")

    def get_by_filmID(self, filmID):
        self.cursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {filmID}")
        results = self.cursor.fetchone()
        return results

    def search_by(self, parameter, user_input):
        if parameter == 'genre':
            self.cursor.execute(
                f"SELECT * FROM tblfilms WHERE genre= '{user_input}'")
        elif parameter == 'yearReleased':
            self.cursor.execute(
                f"SELECT * FROM tblfilms WHERE yearReleased= '{user_input}'")
        elif parameter == 'rating':
            self.cursor.execute(
                f"SELECT * FROM tblfilms WHERE rating= '{user_input}'")

        results = self.cursor.fetchall()
        return results

    def get_all_films(self):
        self.cursor.execute(f"SELECT * FROM tblfilms")
        results = self.cursor.fetchall()
        return results

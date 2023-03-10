import config
import mysql.connector


class Scoreboard:

    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def get_score(self):
        return self.scoreboard


def insert_username_into_player_table(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password=config.mysql_pass)

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Players (Score)
                                VALUES (%s)"""

        cursor.execute(mysql_insert_query, (name,))
        connection.commit()
        print("Player score inserted successfully into Players table!")

    except mysql.connector.Error as error:
        print("Failed to insert score into Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")

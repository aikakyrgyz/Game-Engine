import config
import mysql.connector


class Player:

    def __init__(self, username):
        self.username = username

    def get_player(self):
        return self.username


def insert_username_into_player_table(username):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password=config.mysql_pass)

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Players (Username)
                                VALUES (%s)"""

        cursor.execute(mysql_insert_query, (username,))
        connection.commit()
        print("Player username inserted successfully into Players table!")

    except mysql.connector.Error as error:
        print("Failed to insert username into Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


username = 'Descole'
insert_username_into_player_table(username)


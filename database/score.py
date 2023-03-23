import mysql.connector


class Scoreboard:

    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def get_score(self):
        return self.scoreboard


def insert_dm_score(dmscore):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Players (Dmscore)
                                VALUES (%s)"""

        cursor.execute(mysql_insert_query, (dmscore,))
        connection.commit()
        print("Dr. Mario score inserted successfully into Players table!")

    except mysql.connector.Error as error:
        print("Failed to insert score into Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def insert_puyo_score(puyoscore):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Players (Puyoscore)
                                VALUES (%s)"""

        cursor.execute(mysql_insert_query, (puyoscore,))
        connection.commit()
        print("Puyo Puyo score inserted successfully into Players table!")

    except mysql.connector.Error as error:
        print("Failed to insert score into Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def return_dm_score(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT Dmscore FROM Players 
                                WHERE Username = %s""", (name,))

        result = cursor.fetchone()
        return result

    except mysql.connector.Error as error:
        print("Failed to Dr. Mario score.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def return_puyo_score(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT Puyoscore FROM Players 
                                        WHERE Username = %s""", (name,))

        result = cursor.fetchone()
        return result

    except mysql.connector.Error as error:
        print("Failed to fetch Puyo Puyo score.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def return_combined_score(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT(Dmscore + Puyoscore) as Totalscore FROM Players 
                                        WHERE Username = %s""", (name,))

        result = cursor.fetchone()
        return result

    except mysql.connector.Error as error:
        print("Failed to fetch combined score.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def return_top_five():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT Username, Dmscore, Puyoscore, (Dmscore + Puyoscore) as Totalscore FROM Players 
                                ORDER by Totalscore DESC LIMIT 5;""")

        result = cursor.fetchall()
        return result

    except mysql.connector.Error as error:
        print("Failed to fetch top five scores.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def compare_dm_score(player1, player2):
    score1 = return_dm_score(player1)
    score2 = return_dm_score(player2)


def compare_puyo_score(player1, player2):
    score1 = return_puyo_score(player1)
    score2 = return_puyo_score(player2)

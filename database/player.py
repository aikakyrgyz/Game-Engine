import mysql.connector


def insert_username_into_player_table(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Players (Username)
                                VALUES (%s)""", (name,))

        connection.commit()
        print("Player username inserted successfully into Players table!")

    except mysql.connector.Error as error:
        print("Failed to insert username into Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def check_if_player_exists(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Players 
                                WHERE Username = %s""", (name,))

        result = cursor.fetchone()
        if result is not None:
            print("Player confirmed.")
            return True
        else:
            print("Player does not exist in database. Please try again.")
            return False

    except mysql.connector.Error as error:
        print("Failed to find username in Players table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def change_username(old, new):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        mysql_query = """UPDATE players SET Username =%s WHERE Username =%s"""

        cursor.execute(mysql_query, (new, old))
        connection.commit()
        print(f"{old} has been changed to {new}!")

    except mysql.connector.Error as error:
        print("Failed to update username.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


def display_player_score(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='players',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        cursor.execute("""SELECT Dmscore, Puyoscore, (Dmscore + Puyoscore) as Totalscore FROM Players 
                                WHERE Username = %s""", (name,))

        results = cursor.fetchall()
        return results

    except mysql.connector.Error as error:
        print("Failed to fetch player scores.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")

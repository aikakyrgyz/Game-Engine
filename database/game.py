import mysql.connector


def insert_game_into_game_table(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='games',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Games (Gamename)
                                VALUES (%s)"""

        cursor.execute(mysql_insert_query, (name,))
        connection.commit()
        print("Game inserted successfully into Games table!")

    except mysql.connector.Error as error:
        print("Failed to insert game into Games table.\n{}".format(error) + '.')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")


# needs fixing
def return_game_list():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='games',
                                             user='root',
                                             password='wit122')

        cursor = connection.cursor()
        mysql_id_query = """SELECT Gamename FROM games"""

        cursor.execute(mysql_id_query)
        results = cursor.fetchall()
        list1 = []
        list2 = []
        results = list(results)

        x = 0
        for game in results:
            game = (game[0])
            list1.append(game)
            list2.append(x)
            x += 1

        game_list = list(zip(list1, list2))
        return game_list

    except mysql.connector.Error as error:
        print("Failed to fetch game list.\n{}".format(error) + ".")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection has been closed.")

from database import player


def register_player(username):
    if username != "" and len(username) <= 15:
        # comment out the function below if you do not have SQL set-up
        player.insert_username_into_player_table(username)
        # if exists in the database, add game to player profile
        print(f"Player profile updated - {username}")

        # else register player, add to database
        print(f"Player registered - {username}")
    else:
        print(f"Error, username is empty or too long!")

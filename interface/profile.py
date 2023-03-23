from database import player, score


def display_score(username):
    results = player.display_player_score(username)
    dmscore, puyoscore, combined = results[0]
    text = f"Dr. Mario: {dmscore} | Puyopuyo: {puyoscore}"
    text2 = f"Total Score: {combined}"
    return text, text2

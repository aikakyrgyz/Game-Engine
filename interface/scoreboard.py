from database import score


def display_top_five():
    results = score.return_top_five()
    one1, one2, one3, one4 = results[0]
    two1, two2, two3, two4 = results[1]
    three1, three2, three3, three4 = results[2]
    four1, four2, four3, four4 = results[3]
    five1, five2, five3, five4 = results[4]
    one = f"1: {one1} | Dr. Mario: {one2} | Puyopuyo: {one3} | Total Score: {one4}"
    two = f"2: {two1} | Dr. Mario: {two2} | Puyopuyo: {two3} | Total Score: {two4}"
    three = f"3: {three1} | Dr. Mario: {three2} | Puyopuyo: {three3} | Total Score: {three4}"
    four = f"4: {four1} | Dr. Mario: {four2} | Puyopuyo: {four3} | Total Score: {four4}"
    five = f"5: {five1} | Dr. Mario: {five2} | Puyopuyo: {five3} | Total Score: {five4}"
    return one, two, three, four, five
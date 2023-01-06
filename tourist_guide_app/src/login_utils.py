import sqlite3


def check(username, password):
    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    c.execute("SELECT PASSWORD, ID FROM TOURIST WHERE NAME=?", (username,))
    p = c.fetchall()

    if p:
        if password == p[0][0]:
            valid = 1
            tourist_id = p[0][1]
        else:
            valid = 0
            tourist_id = -1
    else:
        valid = 0
        tourist_id = -1

    conn.commit()
    conn.close()

    return valid, tourist_id

import sqlite3


def delete(d, parent_table, table):
    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    if d == '':
        message = "Id must be filled in"
    elif not d.isdigit():
        message = "Id must be an integer"
    else:
        c.execute("SELECT * FROM {table} WHERE ID=?".format(table=table), (d,))
        results = c.fetchall()

        if results:
            c.execute("DELETE FROM {table} WHERE ID=?".format(table=table), (d,))
            if parent_table != '':
                c.execute("DELETE FROM {table} WHERE ID=?".format(table=parent_table), (d,))

            message = 'Deleted!'
        else:
            message = 'There is not such id'

    conn.commit()
    conn.close()

    return message

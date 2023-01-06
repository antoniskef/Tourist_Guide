import sqlite3


def which_table(rb, acc, fad, act, ser, tra):
    table = ''
    table2 = ''
    if rb == 1:
        table = 'ACCOMMODATION'
        if acc != 'All':
            table2 = acc.upper()
    elif rb == 2:
        table = 'FOOD_AND_DRINK'
        if fad != 'All':
            table2 = fad.upper()
    elif rb == 3:
        table = 'ACTIVITY'
        if act != 'All':
            table2 = act.upper()
    elif rb == 4:
        table = 'SERVICES'
        if ser != 'All':
            table2 = ser.upper()
    elif rb == 5:
        table = 'TRANSPORTATION'
        if tra != 'All':
            table2 = tra.upper()
    elif rb == 6:
        table = 'BEACH'
    elif rb == 7:
        table = 'SIGHTSEEING'

    return rb, table, table2


def search(text, rb, acc, fad, act, ser, tra):
    conn = sqlite3.connect('../database/tourist_guide.db')

    #  create cursor that allows us to execute some SQL commands
    c = conn.cursor()

    loc_columns = ['LOCATION', 'ORIENTATION']

    rb, table, table2 = which_table(rb, acc, fad, act, ser, tra)
    results = []
    columns = []
    if rb > 0:
        text = '%' + text + '%'

        if table2 == "":
            c.execute("SELECT * FROM {table} NATURAL JOIN LOCATION WHERE {table}.NAME LIKE ?".format(table=table), (text,))
            results = c.fetchall()
            c.execute("PRAGMA table_info({table});".format(table=table))
            columns_list = c.fetchall()
            for i in range(len(columns_list)):
                columns.append(columns_list[i][1])
            for i in range(len(loc_columns)):
                columns.append(loc_columns[i])
        else:
            c.execute("SELECT * FROM ({table} NATURAL JOIN LOCATION) NATURAL JOIN {table2} WHERE NAME LIKE ?".format(table=table, table2=table2), (text,))
            results = c.fetchall()
            c.execute("PRAGMA table_info({table});".format(table=table))
            columns_list = c.fetchall()
            for i in range(len(columns_list)):
                columns.append(columns_list[i][1])
            for i in range(len(loc_columns)):
                columns.append(loc_columns[i])
            c.execute("PRAGMA table_info({table2});".format(table2=table2))
            columns_list = c.fetchall()[1:]
            for i in range(len(columns_list)):
                columns.append(columns_list[i][1])

        # commit and close
        conn.commit()
        conn.close()

    return results, columns





import sqlite3


def insert(k, parent_columns, child_columns, parent_table, table):

    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    if k[0] == '' or k[1] == '':
        message = "Id and name must be filled in"
    else:
        try:
            if parent_table != '':
                t1 = create_tuple(len(parent_columns))
                t2 = create_tuple(len(child_columns))

                c1 = tuple(k[:len(parent_columns)])
                c2 = tuple([k[0]] + k[len(parent_columns):])
                c.execute("INSERT INTO {table} VALUES ".format(table=parent_table)+t1, c1)
                c.execute("INSERT INTO {table} VALUES ".format(table=table) + t2, c2)
            else:
                t = create_tuple(len(child_columns))
                c.execute("INSERT INTO {table} VALUES ".format(table=table) + t, k)

            message = "Insetred!"
        except sqlite3.IntegrityError as e:
            if e.args[0] == "datatype mismatch":
                message = "Id must be an integer."
            elif e.args[0].split(":")[0] == "UNIQUE constraint failed":
                message = "Id must be unique."

    conn.commit()
    conn.close()

    return message


def create_tuple(n):
    s = "(?)"
    for i in range(n-1):
        s = s[:-1]
        s = s+", ?)"

    return s


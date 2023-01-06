import sqlite3


def parent_table(table):
    accommodation = ["Hotel", "Apartments", "Camping"]
    food_and_drink = ["Restaurant", "Cafe", "Club", "Bar"]
    activities = ["Cinema", "Festival_concert", "Water_sports"]
    services = ["Police_station", "Doctor", "Hospital", "Rental_cars", "Ship_ticket_agency"]
    transportation = ["Taxi", "Bus"]

    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    columns_list = []
    parent = ''

    if table in accommodation:
        c.execute("PRAGMA table_info({table});".format(table='ACCOMMODATION'))
        columns_list = c.fetchall()
        parent = 'ACCOMMODATION'
    elif table in food_and_drink:
        c.execute("PRAGMA table_info({table});".format(table='FOOD_AND_DRINK'))
        columns_list = c.fetchall()
        parent = 'FOOD_AND_DRINK'
    elif table in activities:
        c.execute("PRAGMA table_info({table});".format(table='ACTIVITY'))
        columns_list = c.fetchall()
        parent = 'ACTIVITY'
    elif table in services:
        c.execute("PRAGMA table_info({table});".format(table='SERVICES'))
        columns_list = c.fetchall()
        parent = 'SERVICES'
    elif table in transportation:
        c.execute("PRAGMA table_info({table});".format(table='TRANSPORTATION'))
        columns_list = c.fetchall()
        parent = 'TRANSPORTATION'
    elif table == "Beach":
        columns_list = []
        parent = ''
    elif table == "Sightseeing":
        columns_list = []
        parent = ''

    col = []

    for i in range(len(columns_list)):
        col.append(columns_list[i][1])

    conn.commit()
    conn.close()

    return col, parent


def columns(table):

    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    c.execute("PRAGMA table_info({table});".format(table=table.upper()))
    columns_list = c.fetchall()

    col = []
    for i in range(len(columns_list)):
        col.append(columns_list[i][1])

    col_parent, parent = parent_table(table)

    col_parent.append(col)

    conn.commit()
    conn.close()

    return col_parent, parent

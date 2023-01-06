import sqlite3
import pandas as pd


def insert():
    df_accommodation = pd.read_excel("../excel_files/ACCOMMODATION/ACCOMMODATION.xlsx")
    df_hotel = pd.read_excel("../excel_files/ACCOMMODATION/HOTEL.xlsx")
    df_apartments = pd.read_excel("../excel_files/ACCOMMODATION/APARTMENTS.xlsx")
    df_camping = pd.read_excel("../excel_files/ACCOMMODATION/CAMPING.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # ACCOMMODATION GENERAL
        for index, row in df_accommodation.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Price = row["PRICE"]
            Rating = row["RATING"]
            Address = row["ADDRESS"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO ACCOMMODATION VALUES (?, ?, ?, ?, ?, ?)", (Id, Name, Price, Rating, Address, Location_id))

        ## HOTELS
        for index, row in df_hotel.iterrows():
            Id = row["ID"]
            Breakfast = row["BREAKFAST"]
            Pool = row["POOL"]
            Spa = row["SPA"]
            c.execute("INSERT INTO HOTEL VALUES (?, ?, ?, ?)", (Id, Breakfast, Pool, Spa))

        ## APARTMENTS
        for index, row in df_apartments.iterrows():
            Id = row["ID"]
            Rooms = row["ROOMS"]
            c.execute("INSERT INTO APARTMENTS VALUES (?, ?)", (Id, Rooms))

        ## Camping
        for index, row in df_camping.iterrows():
            Id = row["ID"]
            Free = row["FREE"]
            c.execute("INSERT INTO CAMPING VALUES (?, ?)", (Id, Free))

        conn.commit()

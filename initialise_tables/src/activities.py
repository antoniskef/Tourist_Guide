import sqlite3
import pandas as pd


def insert():
    df_activity = pd.read_excel("../excel_files/ACTIVITY/ACTIVITY.xlsx")
    df_cinema = pd.read_excel("../excel_files/ACTIVITY/CINEMA.xlsx")
    df_fest_conc = pd.read_excel("../excel_files/ACTIVITY/FESTIVAL_CONCERT.xlsx")
    df_water_sports = pd.read_excel("../excel_files/ACTIVITY/WATER_SPORTS.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # ACTIVITY
        for index, row in df_activity.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Price = row["PRICE"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO ACTIVITY VALUES (?, ?, ?, ?)", (Id, Name, Price, Location_id))

        # CINEMA
        for index, row in df_cinema.iterrows():
            Id = row["ID"]
            Summer = row["SUMMER"]
            c.execute("INSERT INTO CINEMA VALUES (?, ?)", (Id, Summer))

        # FESTIVAL_CONCERT
        for index, row in df_fest_conc.iterrows():
            Id = row["ID"]
            Artist = row["ARTIST"]
            c.execute("INSERT INTO FESTIVAL_CONCERT VALUES (?, ?)", (Id, Artist))

        # WATER SPORTS
        for index, row in df_water_sports.iterrows():
            Id = row["ID"]
            Tube = row["TUBE"]
            Water_ski = row["WATER_SKI"]
            Surfing = row["SURFING"]
            Diving = row["DIVING"]
            Sailing = row["SAILING"]
            c.execute("INSERT INTO WATER_SPORTS VALUES (?, ?, ?, ?, ?, ?)", (Id, Tube, Water_ski, Surfing, Diving, Sailing))

        conn.commit()

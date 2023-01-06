import sqlite3
import pandas as pd


def insert():
    df_transportation = pd.read_excel("../excel_files/TRANSPORTATION/TRANSPORTATION.xlsx")
    df_taxi = pd.read_excel("../excel_files/TRANSPORTATION/TAXI.xlsx")
    df_bus = pd.read_excel("../excel_files/TRANSPORTATION/BUS.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # TRANSPORTATION
        for index, row in df_transportation.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO TRANSPORTATION VALUES (?, ?, ?)", (Id, Name, Location_id))

        # TAXI
        for index, row in df_taxi.iterrows():
            Id = row["ID"]
            Tel = row["TEL NUMBER"]
            c.execute("INSERT INTO TAXI VALUES (?, ?)", (Id, Tel))

        # BUS
        for index, row in df_bus.iterrows():
            Id = row["ID"]
            Inter = row["INTERMEDIATE STOPS"]
            Final = row["FINAL STOP"]
            Time = row["TIME OF DEPARTURE"]
            c.execute("INSERT INTO BUS VALUES (?, ?, ?, ?)", (Id, Inter, Final, Time))

        conn.commit()

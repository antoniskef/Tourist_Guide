import sqlite3
import pandas as pd


def insert():
    df_beach = pd.read_excel("../excel_files/BEACH/BEACH.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # BEACH
        for index, row in df_beach.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Organised = row["ORGANISED"]
            Type = row["TYPE"]
            Price = row["PRICE"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO BEACH VALUES (?, ?, ?, ?, ?, ?)", (Id, Name, Organised, Type, Price, Location_id))

        conn.commit()

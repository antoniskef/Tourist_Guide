import sqlite3
import pandas as pd


def insert():
    df_location = pd.read_excel("../excel_files/LOCATION/LOCATION.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # LOCATION
        for index, row in df_location.iterrows():
            Id = row["LOCATION_ID"]
            Name = row["LOCATION_NAME"]
            Orientation = row["ORIENTATION"]
            c.execute("INSERT INTO LOCATION VALUES (?, ?, ?)", (Id, Name, Orientation))

        conn.commit()

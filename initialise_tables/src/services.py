import sqlite3
import pandas as pd


def insert():
    df_services = pd.read_excel("../excel_files/SERVICES/SERVICES.xlsx")
    df_doctor = pd.read_excel("../excel_files/SERVICES/DOCTOR.xlsx")
    df_hospital = pd.read_excel("../excel_files/SERVICES/HOSPITAL.xlsx")
    df_police_station = pd.read_excel("../excel_files/SERVICES/POLICE STATION.xlsx")
    df_rental_cars = pd.read_excel("../excel_files/SERVICES/RENTAL CAR.xlsx")
    df_ship_ticket_agency = pd.read_excel("../excel_files/SERVICES/SHIP TICKET AGENCY.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # SERVICES
        for index, row in df_services.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Tel = row["TEL.NUMBER"]
            Address = row["ADDRESS"]
            Opening_hours = row["OPENING HOURS"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO SERVICES VALUES (?, ?, ?, ?, ?, ?)", (Id, Name, Tel, Address, Opening_hours, Location_id))

        # POLICE STATION
        for index, row in df_police_station.iterrows():
            Id = row["ID"]
            Fax = row["FAX"]
            c.execute("INSERT INTO POLICE_STATION VALUES (?, ?)", (Id, Fax))

        # DOCTOR
        for index, row in df_doctor.iterrows():
            Id = row["ID"]
            Speciality = row["SPECIALITY"]
            c.execute("INSERT INTO DOCTOR VALUES (?, ?)", (Id, Speciality))

        # HOSPITAL
        for index, row in df_hospital.iterrows():
            Id = row["ID"]
            Public = row["PUBLIC"]
            c.execute("INSERT INTO HOSPITAL VALUES (?, ?)", (Id, Public))

        # RENTAL_CARS
        for index, row in df_rental_cars.iterrows():
            Id = row["ID"]
            Rating = row["RATING"]
            Price = row["PRICE"]
            Num_cars = row["NUM CARS"]
            c.execute("INSERT INTO RENTAL_CARS VALUES (?, ?, ?, ?)", (Id, Rating, Price, Num_cars))

        # SHIP_TICKET_AGENCY
        for index, row in df_ship_ticket_agency.iterrows():
            Id = row["ID"]
            Price = row["PRICE"]
            c.execute("INSERT INTO SHIP_TICKET_AGENCY VALUES (?, ?)", (Id, Price))

        conn.commit()


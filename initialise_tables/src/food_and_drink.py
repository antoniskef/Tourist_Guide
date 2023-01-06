import sqlite3
import pandas as pd


def insert():
    df_food_and_drink = pd.read_excel("../excel_files/Food_and_Drink/Food_and_Drink.xlsx")
    df_restaurant = pd.read_excel("../excel_files/Food_and_Drink/Restaurant.xlsx")
    df_cafe = pd.read_excel("../excel_files/Food_and_Drink/Cafe.xlsx")
    df_bar = pd.read_excel("../excel_files/Food_and_Drink/Bar.xlsx")
    df_club = pd.read_excel("../excel_files/Food_and_Drink/Club.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # FOOD AND DRINK GENERAL
        for index, row in df_food_and_drink.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Price = row["PRICE"]
            Rating = row["RATING"]
            Address = row["ADDRESS"]
            Location = row["LOCATION_ID"]
            c.execute("INSERT INTO FOOD_AND_DRINK VALUES (?, ?, ?, ?, ?, ?)", (Id, Name, Rating, Price, Address, Location))

        ## RESTAURANTS
        for index, row in df_restaurant.iterrows():
            Id = row["ID"]
            Type_of_food = row["TYPE_OF_FOOD"]
            c.execute("INSERT INTO RESTAURANT VALUES (?, ?)", (Id, Type_of_food))

        ## CAFE
        for index, row in df_cafe.iterrows():
            Id = row["ID"]
            Board_games = row["GAMES"]
            c.execute("INSERT INTO CAFE VALUES (?, ?)", (Id, Board_games))

        ## CLUB
        for index, row in df_club.iterrows():
            Id = row["ID"]
            Type_of_music = row["TYPE_OF_MUSIC"]
            c.execute("INSERT INTO CLUB VALUES (?, ?)", (Id, Type_of_music))

        ## BAR
        for index, row in df_bar.iterrows():
            Id = row["ID"]
            Type_of_music = row["TYPE_OF_MUSIC"]
            c.execute("INSERT INTO BAR VALUES (?, ?)", (Id, Type_of_music))

        conn.commit()

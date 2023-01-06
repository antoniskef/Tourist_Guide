import create_tables
import location
import accommodation
import food_and_drink
import activities
import services
import transportation
import beach
import sightseeing


def initialise_tables():
    create_tables.create()
    location.insert()
    accommodation.insert()
    food_and_drink.insert()
    activities.insert()
    services.insert()
    transportation.insert()
    beach.insert()
    sightseeing.insert()


if __name__ == '__main__':
    initialise_tables()

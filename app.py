from fastapi import FastAPI
from pydantic import BaseModel
from sqlite3 import connect
from math import radians, sin, cos, sqrt, atan2

app = FastAPI()

class Coordinates(BaseModel):
    lat: float
    lng: float

addresses = [
    {'coordinates': (12.29,76.63),'distance': 100},
    {'coordinates': (13.03,77.59), 'distance': 50},
    {'coordinates': (12.95,77.70), 'distance': 200}
]



@app.get("/addresses/{lat}{long}")
def fetch_addresses(lat:int,long:int):
    # Connect to the database
    conn = connect("database.db")
    c = conn.cursor()
    
    # # Fetch all addresses from the database
    # c.execute("SELECT * FROM addresses")
    # addresses = c.fetchall()

    lat = 12.97
    lng = 77.59
    
    # Convert the given coordinates to radians
    lat1 = radians(lat)
    lng1 = radians(lng)
    
    # Initialize a list to store the addresses within the given distance
    result = []
    # addresses = [(12.29,76.63),(13.03,77.59)]
    
    # Calculate the distance between the given coordinates and each address in the database using the haversine formula
    for address in addresses:
    #     for i in address:
        lat2 = radians(address['coordinates'][0])
        lng2 = radians(address['coordinates'][1])
        dlng = lng2 - lng1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 6371 * c
        if distance <= distance:
            result.append(lat2)
            result.append(lng2)

        # Return the list of addresses within the given distance
        return result

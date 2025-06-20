# geo.py
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Securely fetch API key or raise error
try:
    API_KEY = os.environ["OPEN_KEY"]
except KeyError:
    raise RuntimeError("Missing required environment variable: OPEN_KEY. Make sure it is set in your .env file.")

def get_coordinates(address, city, state, postcode):
    full_address = f"{address}, {city}, {state}, {postcode}"
    try:
        response = requests.get(
            "https://api.opencagedata.com/geocode/v1/json",
            params={"q": full_address, "key": API_KEY}
        )
        response.raise_for_status()
        data = response.json()
        if data['results']:
            coords = data['results'][0]['geometry']
            return coords['lat'], coords['lng']
    except Exception as e:
        print(f"Error fetching coordinates for: {full_address} -> {e}")
        return None
    return None

def enhance_with_geo(row):
    res_coords = get_coordinates(row[3], row[4], row[5], row[6])
    post_coords = get_coordinates(row[10], row[11], row[12], row[13])
    if res_coords and post_coords:
        row[7], row[8] = res_coords
        row[14], row[15] = post_coords
        return row
    return None

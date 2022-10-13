from uber_rides.session import Session
from uber_rides.client import UberRidesClient

ACCESS_TOKEN = "[REDACTED]"
session = Session(oauth2credential=ACCESS_TOKEN)
client = UberRidesClient(session)

response = client.get_products(37.77, -122.41)


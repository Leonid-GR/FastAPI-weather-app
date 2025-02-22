import os

API_KEY = "672b1d6aa764591bfd003931f49ac435"
if not API_KEY:
    raise RuntimeError("No API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"
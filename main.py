from fastapi import FastAPI
from weather_report.geacoder import Geocoder
from weather_report.weather import WeatherHandler

app = FastAPI()


@app.get("/geocode")
def get_city_coordinates(city: str):
    return Geocoder.get_coordinates(city)


@app.get("/weather/current")
def get_current_weather(city: str):
    coordinates = Geocoder.get_coordinates(city)
    return WeatherHandler.get_current_weather(coordinates["lat"], coordinates["lon"])


@app.get("/weather/forecast")
def get_weather_forecast(city: str):
    coordinates = Geocoder.get_coordinates(city)
    return WeatherHandler.get_weather_forecast(coordinates["lat"], coordinates["lon"])

import httpx
from fastapi import HTTPException
from config import API_KEY, BASE_URL

class WeatherHandler:

    @staticmethod
    def get_current_weather(lat: float, lon: float):
        try:
            response = httpx.get(f"{BASE_URL}/weather", params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric",
                "lang": "ru"
            })
            response.raise_for_status()
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error fetching current weather")
        except Exception as e:
            raise HTTPException(status_code=500, detail="An error occurred while fetching current weather")

    @staticmethod
    def get_weather_forecast(lat: float, lon: float):
        try:
            response = httpx.get(f"{BASE_URL}/forecast", params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric",
                "lang": "ru"
            })
            response.raise_for_status()
            data = response.json()

            forecast = []
            for entry in data["list"]:
                forecast.append({
                    "datetime": entry["dt_txt"],
                    "temperature": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"],
                    "humidity": entry["main"]["humidity"],
                    "wind_speed": entry["wind"]["speed"]
                })

            return forecast
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error fetching weather forecast")
        except Exception as e:
            raise HTTPException(status_code=500, detail="An error occurred while fetching weather forecast")
import httpx
from fastapi import HTTPException
from config import API_KEY

class Geocoder:

    @staticmethod
    def get_coordinates(city: str):
        try:
            response = httpx.get("https://api.openweathermap.org/geo/1.0/direct", params={
                "q": city,
                "appid": API_KEY,
                "limit": 1
            })
            response.raise_for_status()
            data = response.json()
            if not data:
                raise HTTPException(status_code=404, detail="City not found")
            return {
                "lat": data[0]["lat"],
                "lon": data[0]["lon"]
            }
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error fetching coordinates")
        except Exception as e:
            raise HTTPException(status_code=500, detail="An error occurred while fetching coordinates")
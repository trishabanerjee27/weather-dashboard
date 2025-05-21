import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_weather(city):
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/"
        f"rest/services/timeline/{city}?unitGroup=us&key={API_KEY}&contentType=json"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


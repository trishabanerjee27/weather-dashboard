import streamlit as st
from weather.fetcher import fetch_weather
from weather.models import WeatherDay
from weather.storage import save_weather_to_csv
import pandas as pd

st.title("Weather Dashboard")
city = st.text_input("Enter a city", value="Seattle")

if st.button("Fetch Weather"):
    try:
        data = fetch_weather(city)
        daily = data["days"]
        weather_objs = [WeatherDay(day["datetime"], day["tempmax"], day["tempmin"], day["conditions"]) for day in daily]
        save_weather_to_csv(weather_objs, "weather_history.csv")

        df = pd.DataFrame([w.to_dict() for w in weather_objs])
        df["avg_temp"] = (df["tempmax"] + df["tempmin"]) / 2

        st.success(f"Showing 15-day forecast for {city} (in Fahrenheit)")
        st.dataframe(df)
        st.line_chart(df.set_index("date")["avg_temp"])
    except Exception as e:
        st.error(f"Error: {e}")
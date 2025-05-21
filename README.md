# weather-dashboard

# Weather Dashboard

A Streamlit application (python) that fetches live weather forecasts, stores historical data, and lets you analyze weather trends with charts and tables.

---

## Features

- Fetches live 15-day forecast from Visual Crossing Weather API
- Stores historical data in CSV format
- Built using OOP (`WeatherDay` class)
- Analyzes data using Pandas
- Visualizes trends with interactive Streamlit charts
- Keeps API keys secure with `.env`

---

## What's used?

- Python 3.10+
- Streamlit
- Pandas
- Requests
- python-dotenv

---

## Project Structure
```
weather-dashboard/
├── app.py # Streamlit app
├── weather/
│ ├── init.py
│ ├── fetcher.py # API logic (fetch_weather)
│ ├── models.py # WeatherDay class
│ ├── storage.py # CSV read/write
├── analysis.ipynb # Jupyter notebook for data EDA
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```


---

## Installation

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   cd weather-dashboard
   ```
2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```
3. **Set up .env file**
    ```
    API_KEY=whateverrr_visualcrossing_api_key
    ```
4. **run the APP!**
    ```
    streamlit run app.py
    ```
5. Open http://localhost:8501 in your browser


---

## Analysis
To run analysis separately, open:
```
analysis.ipynb
```
Here, you can:

- Compute average temps

- Plot trend lines

- Inspect data with Pandas

---

## API Reference
Weather data is sourced from the ([Visual Crossing Weather API](https://www.visualcrossing.com/weather-query-builder/)), which provides rich forecasts including temperature precipitation, wind, and condition summaries.

---
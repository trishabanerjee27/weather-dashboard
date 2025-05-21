import csv
import os

def save_weather_to_csv(weather_data_list, filepath):
    if not weather_data_list:
        return
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=weather_data_list[0].to_dict().keys())
        writer.writeheader()
        for entry in weather_data_list:
            writer.writerow(entry.to_dict())

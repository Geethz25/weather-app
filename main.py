"""
weather_fetcher.py -- Periodically fetches current weather data from the
Open-Meteo API and saves each reading to a timestamped text file.
"""
import requests
import os
from datetime import datetime


def fetch_weather(latitude: float = 6.98, longitude: float = 79.85) -> dict:
    """
    Fetch current weather data from the Open-Meteo API.

    Parameters: latitude (float), longitude (float)
    Returns: dict -- Parsed JSON API response.
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly": "precipitation",
    }
    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def display_weather(weather_data: dict) -> str:
    """Format weather data into a human-readable string."""
    current = weather_data.get("current_weather", {})
    temperature = current.get("temperature", "N/A")
    wind_speed = current.get("windspeed", "N/A")
    wind_dir = current.get("winddirection", "N/A")
    weather_code = current.get("weathercode", "N/A")
    timestamp = current.get("time", "N/A")

    hourly = weather_data.get("hourly", {})
    precipitation = hourly.get("precipitation", ["N/A"])[0]

    return (
        f"=== Weather Report ===\n"
        f"Timestamp      : {timestamp}\n"
        f"Temperature    : {temperature} C\n"
        f"Wind Speed     : {wind_speed} km/h\n"
        f"Wind Direction : {wind_dir}\n"
        f"Weather Code   : {weather_code}\n"
        f"Precipitation  : {precipitation} mm\n"
    )


def save_weather_report(report: str, output_dir: str = "weather_reports") -> str:
    """Save weather report to a timestamped text file."""
    os.makedirs(output_dir, exist_ok=True)
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as file_handle:
        file_handle.write(report)
    return file_path


def main() -> None:
    """Entry point: fetch, display, and save the weather report."""
    try:
        weather_data = fetch_weather()
        report = display_weather(weather_data)
        print(report)
        saved_path = save_weather_report(report)
        print(f"Report saved to: {saved_path}")
    except requests.exceptions.RequestException as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

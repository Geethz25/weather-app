"""
weather_fetcher.py -- Periodically fetches current weather data from the
Open-Meteo API and saves each reading to a timestamped text file.
"""
import requests
import os
from datetime import datetime

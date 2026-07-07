"""
scraper.py -- Scrapes weather data from the BBC Weather website
using Requests and BeautifulSoup.
"""
import requests
from bs4 import BeautifulSoup

BBC_WEATHER_URL = "https://www.bbc.com/weather/1248991"  # Colombo

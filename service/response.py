from DBs.lab3.repository.database import get_weather, get_cel_obj_asc
from datetime import datetime


def get_data(country, date):
    date = datetime.strptime(date, '%d.%m.%Y').date()
    weather_data = get_weather(country, date)
    cel_obj_asc_data = get_cel_obj_asc(country, date)

    return weather_data, cel_obj_asc_data

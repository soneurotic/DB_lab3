from DBs.lab3.settings import *
from DBs.lab3.domain.orm import WorldWeather, CelestialObjectsAscension
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from dotenv import load_dotenv

def create_session():
    load_dotenv()

    if DATABASE == 'postgresql':
        URL = 'POSTGRESQL_URL'
        if not URL:
            raise ValueError('Некоректно визначена змінна POSTGRES_URL')
    elif DATABASE == 'mysql':
        URL = 'MYSQL_URL'
        if not URL:
            raise ValueError('Некоректно визначена змінна MYSQL_URL')
    else:
        raise NameError(f'Перевірте коректність підключеної бази даних')

    engine = create_engine(URL)
    return Session(bind=engine)

session = create_session()

def get_weather(country, date):
    getInfo = (
        select(WorldWeather.country, WorldWeather.temperature_celsius, WorldWeather.wind_kph, WorldWeather.wind_direction, WorldWeather.last_updated, WorldWeather.touch_some_grass)
        .where((WorldWeather.country == country) & (func.date(WorldWeather.last_updated) == date))
    )
    return session.execute(getInfo).all()


def get_cel_obj_asc(country, date):
    getInfo = (
        select(CelestialObjectsAscension.sunrise, CelestialObjectsAscension.sunset, CelestialObjectsAscension.moonrise, CelestialObjectsAscension.moonset)
        .join(WorldWeather, CelestialObjectsAscension.id == WorldWeather.id)
        .where((WorldWeather.country == country) & (func.date(WorldWeather.last_updated) == date))
    )
    return session.execute(getInfo).all()
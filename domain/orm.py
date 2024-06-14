from sqlalchemy import ForeignKey, Column, String, Integer, Boolean, Enum, Float, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WorldWeather(Base):
    __tablename__ = 'world_weather'

    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    temperature_celsius = Column(Float, nullable=False)
    wind_kph = Column(Float, nullable=False)
    wind_direction = Column(Enum('ENE', 'SSW', 'WSW', 'NNW', 'W', 'E', 'S', 'N', 'NW', 'SW', 'SE', 'NE', 'ESE', 'NNE', 'SSE', 'WNW'), nullable=False)
    last_updated = Column(DateTime, nullable=False)
    touch_some_grass = Column(Boolean, nullable=False)

# Взяти в опрацювання всі колонки стосовно однієї категорії для подальшого
# оцінювання в залежності від кратності варіанта вашому номеру в списку:
# 1. вітру,
# 2. стану повітря,
# 3. осадів
# 4. сходу-заходу небесних тіл

# Варіант у списку групи - 20
# 20 % 4 = 0, відповідно обиратимемо всі колонки
# стосовно категорії сходу-заходу небесних тіл

class CelestialObjectsAscension(Base):
    __tablename__ = 'cel_obj_ascension'

    id = Column(Integer, ForeignKey('world_weather.id'), primary_key=True)
    sunrise = Column(String, nullable=False)
    sunset = Column(String, nullable=False)
    moonrise = Column(String, nullable=False)
    moonset = Column(String, nullable=False)
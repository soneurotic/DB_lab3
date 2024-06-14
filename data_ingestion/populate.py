import os
import pandas as pd


def populate_sql(path=''):
    if path != '':
        os.chdir(path)

    df = pd.read_csv('GlobalWeatherRepository.csv')
    df = df[['country', 'temperature_celsius', 'wind_kph', 'wind_direction', 'last_updated', 'sunrise', 'sunset', 'moonrise', 'moonset']]

    for column in ['sunrise', 'sunset', 'moonrise', 'moonset']:
        df[column] = df[column].map(lambda x: x[:-3])

    base_query = '''INSERT INTO world_weather (country, temperature_celsius, wind_kph, wind_direction, last_updated, sunrise, sunset, moonrise, moonset) VALUES '''

    with open('populate.sql', 'w', encoding='UTF-8') as file:
        for index, row in df.iterrows():
            query = base_query + str(tuple(row)) + ';\n'
            file.write(query)


if __name__ == '__main__':
    populate_sql()
from tabulate import tabulate


def display_output(world_weather, cel_obj_asc):
    print('\n' + '\033[1m' + 'Weather')
    print(tabulate(world_weather, ('Country', 'Temperature (Celsius)', 'Wind (kph)', 'Wind direction', 'Last updated', 'Touch some grass?'), tablefmt='pretty'))

    print('\n' + '\033[1m' + 'Celestial objects ascension')
    print(tabulate(cel_obj_asc, ('Sunrise', 'Sunset', 'Moonrise', 'Moonset'), tablefmt='pretty'))
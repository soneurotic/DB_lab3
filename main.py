from DBs.lab3.presentation_layer.user_input import get_user_input
from DBs.lab3.presentation_layer.output import display_output
from DBs.lab3.service.response import get_data


def main():
    country, date = get_user_input()
    world_weather, cel_obj_asc = get_data(country, date)
    display_output(world_weather, cel_obj_asc)


if __name__ == '__main__':
    main()
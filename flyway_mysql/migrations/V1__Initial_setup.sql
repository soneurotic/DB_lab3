CREATE TABLE world_weather(
    id                      serial PRIMARY KEY,
    country                 varchar(32) NOT NULL,
    temperature_celsius     real NOT NULL,
    wind_kph                real NOT NULL,
    wind_direction          varchar(3) NOT NULL,
    last_updated            timestamp NOT NULL,
    sunrise                 varchar(32) NOT NULL,
    sunset                  varchar(32) NOT NULL,
    moonrise                varchar(32) NOT NULL,
    moonset                 varchar(32) NOT NULL
);
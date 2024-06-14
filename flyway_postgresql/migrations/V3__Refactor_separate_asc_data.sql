CREATE TABLE cel_obj_ascension(
    id             serial PRIMARY KEY REFERENCES world_weather(id),
    sunrise        varchar(32) NOT NULL,
    sunset         varchar(32) NOT NULL,
    moonrise       varchar(32) NOT NULL,
    moonset        varchar(32) NOT NULL
);

INSERT INTO cel_obj_ascension SELECT id, sunrise, sunset, moonrise, moonset FROM world_weather;

ALTER TABLE world_weather DROP COLUMN sunrise,
                          DROP COLUMN sunset,
                          DROP COLUMN moonrise,
                          DROP COLUMN moonset;
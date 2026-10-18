CREATE TABLE macro_observations (
    series_id  TEXT    NOT NULL,
    obs_date   DATE    NOT NULL,
    value      NUMERIC NOT NULL,
    PRIMARY KEY (series_id, obs_date)
);
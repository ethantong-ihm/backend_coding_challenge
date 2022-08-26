CREATE TABLE IF NOT EXISTS song_data (
  artist_name varchar(200) NOT NULL,
  song_title varchar(200) NOT NULL,
  non_overnight_replays int NOT NULL,
  station_replays int NOT NULL,
  market_replays int NOT NULL,
  breakout_name varchar(50) NOT NULL,
  breakout_metric1 int NOT NULL,
  breakout_metric2 int NOT NULL,
  breakout_metric3 int NOT NULL,
  breakout_metric4 int NOT NULL,
  breakout_metric5 int NOT NULL,
  breakout_metric6 int NOT NULL,
  breakout_metric7 int NOT NULL,
  breakout_metric8 int NOT NULL,
  breakout_metric9 int NOT NULL,
  UNIQUE (artist_name, song_title, breakout_name, breakout_metric1, breakout_metric2, breakout_metric3, breakout_metric4)
);




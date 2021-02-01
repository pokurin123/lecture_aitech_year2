CREATE TABLE data_spot_impr (
spot_id SERIAL PRIMARY KEY,
spot_area TEXT,
spot_name TEXT,
spot_latitude TEXT,
spot_longitude TEXT,
spot_elevation TEXT,
spot_history_culture INTEGER,
spot_nature INTEGER,
spot_view INTEGER,
spot_opentime INTEGER,
spot_closetime INTEGER
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime
) VALUES (
'東京', '高尾山', '35.6254527', '139.7576692', '599',
0, 1, 1,
10, 16
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime
) VALUES (
'鳥取', '鳥取砂丘', '35.5417282', '134.2298797', '0',
0, 1, 1,
8, 17
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime
) VALUES (
'東京', '築地本願寺', '35.6676278', '139.7721169', '2',
1, 0, 1,
6, 16
);



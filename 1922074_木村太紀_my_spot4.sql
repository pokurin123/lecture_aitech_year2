CREATE TABLE my_spot4(
   ID              INTEGER  NOT NULL PRIMARY KEY 
  ,spot_name       VARCHAR(12) NOT NULL
  ,spot_location   VARCHAR(13) NOT NULL
  ,spot_latitude   NUMERIC(11,8) NOT NULL
  ,spot_longitude  NUMERIC(11,7) NOT NULL
  ,spot_type       VARCHAR(3) NOT NULL
  ,nearest_station VARCHAR(7) NOT NULL
  ,when_build      INTEGER  NOT NULL
  ,open            INTEGER  NOT NULL
  ,close           INTEGER  NOT NULL
  ,rating_5Lv      INTEGER  NOT NULL
  ,history         INTEGER  NOT NULL
  ,culture         INTEGER  NOT NULL
  ,nature          INTEGER  NOT NULL
  ,religion        INTEGER  NOT NULL
  ,amusement       INTEGER  NOT NULL
);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (1,'武蔵国分寺跡','国分寺',35.6917002,139.4732204,'寺社','国分寺',750,24,24,3,1,1,0,1,0);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (2,'都立武蔵国分寺公園','国分寺',35.4148,139.2821,'公園','西国分寺',2002,24,24,3,0,0,1,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (3,'お鷹の道・真姿の池湧水群','国分寺',35.6941728,139.4736651,'自然','国分寺',847,24,24,5,0,0,1,0,0);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (4,'武蔵国分寺','国分寺',35.41396,139.28158,'寺社','国分寺',1333,24,24,4,1,1,0,1,0);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (5,'都立小金井公園','小金井',35.4252,139.3108,'公園','小金井',1954,24,24,5,0,0,1,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (6,'江戸東京たてもの園','小金井',35.425996,139.304541,'博物館','小金井',1993,9,16,3,1,1,0,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (7,'けやき公園','国分寺',35.7105909,139.4745479,'公園','国分寺',1980,24,24,5,0,0,1,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (8,'昭和記念公園','立川',35.7030422,139.4104691,'公園','立川',1983,24,24,5,0,0,1,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (9,'玉川上水緑道','国分寺・小金井・小平・立川',35.7481267,139.3956418,'遊歩道','国分寺・小金井',1653,24,24,4,0,0,1,0,1);
INSERT INTO my_spot4(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement) VALUES (10,'谷保天満宮','国立',35.68020857,139.4436548,'寺社','国立',903,24,24,4,1,1,0,1,0);

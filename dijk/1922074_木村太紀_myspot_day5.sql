CREATE TABLE myspot_day5(
   ID              INTEGER  NOT NULL PRIMARY KEY 
  ,spot_name       VARCHAR(12) NOT NULL
  ,spot_location   VARCHAR(13) NOT NULL
  ,spot_latitude   NUMERIC(10,7) NOT NULL
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
  ,stay_time       INTEGER  NOT NULL
);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (1,'武蔵国分寺跡','国分寺',35.423802,139.2828026,'寺社','国分寺',750,24,24,3,1,1,0,1,0,10);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (2,'都立武蔵国分寺公園','国分寺',35.4151912,139.2818347,'公園','西国分寺',2002,24,24,3,0,0,1,0,1,30);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (3,'お鷹の道・真姿の池湧水群','国分寺',35.413903,139.2825565,'自然','国分寺',847,24,24,5,0,0,1,0,0,30);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (4,'武蔵国分寺','国分寺',35.4138058,139.2819694,'寺社','国分寺',1333,24,24,4,1,1,0,1,0,15);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (5,'都立小金井公園','小金井',35.4300291,139.3100976,'公園','小金井',1954,24,24,5,0,0,1,0,1,60);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (6,'江戸東京たてもの園','小金井',35.4256399,139.3045236,'博物館','小金井',1993,9,16,3,1,1,0,0,1,45);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (7,'けやき公園','国分寺',35.4239893,139.2828434,'公園','国分寺',1980,24,24,5,0,0,1,0,1,40);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (8,'昭和記念公園','立川',35.424197,139.2349866,'公園','立川',1983,24,24,5,0,0,1,0,1,70);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (9,'玉川上水緑道','国分寺・小金井・小平・立川',35.4347169,139.2544989,'遊歩道','国分寺・小金井',1653,24,24,4,0,0,1,0,1,30);
INSERT INTO myspot_day5(ID,spot_name,spot_location,spot_latitude,spot_longitude,spot_type,nearest_station,when_build,open,close,rating_5Lv,history,culture,nature,religion,amusement,stay_time) VALUES (10,'谷保天満宮','国立',35.4048379,139.2638867,'寺社','国立',903,24,24,4,1,1,0,1,0,20);

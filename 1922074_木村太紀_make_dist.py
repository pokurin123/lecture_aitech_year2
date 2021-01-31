from dataaccess import DataAccess
import itertools
import math

hoge = DataAccess()
count = 0
list_latitude = {}
list_longitude = {}
#赤道、極半径
red_rad = 6378.137
pol_rad = 6356.752
name = {}
name_ex = {}
#化成緯度、経度それぞれ辞書型に格納
for id_n in range(1,11):
    x = list(itertools.chain.from_iterable(hoge.get_spots(id_n)))
    #化成緯度のリスト
    list_latitude[count] = x[2]
    list_longitude[count] = x[3]
    name[count] = x[0]
    name_ex[count] = x[0]
    count += 1

def make_dist(point_A,point_B):    
    print(point_A + "から" + point_B + "までの距離")
    #適当なidを取得
    for i in name:
        if name[i] == point_A:
            id_A = i
        elif name[i] == point_B:
            id_B = i
    
    rad_lati_A = math.radians(list_latitude[id_A])
    rad_long_A = math.radians(list_longitude[id_A])
    rad_lati_B = math.radians(list_latitude[id_B])
    rad_long_B = math.radians(list_longitude[id_B])

    param_rati_A = math.atan(pol_rad/red_rad * math.tan(rad_lati_A))
    param_rati_B = math.atan(pol_rad/red_rad * math.tan(rad_lati_B))

    dist_sphere = math.acos(math.sin(param_rati_A) * math.sin(param_rati_B) + math.cos(param_rati_A) * math.cos(param_rati_B) * math.cos(rad_long_A - rad_long_B))

    corr_1 = (math.sin(dist_sphere)-dist_sphere) * (math.sin(param_rati_A)+math.sin(param_rati_B))**2 / math.cos(dist_sphere/2)**2
    corr_2 = (math.sin(dist_sphere)+dist_sphere) * (math.sin(param_rati_A)-math.sin(param_rati_B))**2 / math.cos(dist_sphere/2)**2
    f = (red_rad - pol_rad) / red_rad
    dist_corr = f/8 * (corr_1 - corr_2)

    final_dist = red_rad * (dist_sphere + dist_corr)
    time = final_dist/4 *60
    print(str(final_dist) + "km")

def set_point(point_A):
    for i in name:
        if name[i] == point_A:
            point_A_id = i
    del name_ex[point_A_id]
    for i in name_ex:
        point_B = name[i]
        make_dist(point_A,point_B)
        print("----------------------------------")

point_A = "武蔵国分寺"
set_point(point_A)
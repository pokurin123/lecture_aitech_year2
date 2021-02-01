from dataaccess import DataAccess
import numpy as np

da = DataAccess()
# spot_list = da.get_spots()
# for spot in spot_list:
#     print(x)
# print("----")
# spot_list = da.get_spots_by_area("長野")
# for spot in spot_list:
#     print(spot)
# print("----")
# spot_list = da.get_latlng_by_spot_name("白馬五竜スキー場")
# for spot in spot_list:
#     print(spot)
# print("----")

# spot_list = da.get_openclose_by_spot_name("白馬五竜スキー場")
# for spot in spot_list:
#     print(spot)
# print("----")
# # spot_list = da.get_spot_by_features(0, 1, 1, 1, 1)
# # for spot in spot_list:
# #     print(spot)
# # print("----")
# spot_list = da.get_spot_by_branch(22)
# for spot in spot_list:
#     print(spot)
# print("----")
# ##ここから追記
# spot_list = da.get_temperature("白馬五竜スキー場")
# for spot in spot_list:
#     print(spot)

# 意味的計算（内積）
spot_list = da.get_impression()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(3,4)
c = len(a)
b = np.zeros(c)
x = input("その場所に歴史がありますか？（あればはいでなければいいえ）")
if x == "はい":
    b[0] = 1
y = input("その場所に自然がありますか？（あればはいでなければいいえ）")
if y == "はい":
    b[1] = 1
z = input("その場所に景観がありますか？（あればはいでなければいいえ）")
if z == "はい":
    b[2] = 1
kekka = []
for item in a:
    kekka.append([item[0], np.sum(item[1:].astype(np.int) * b)])
kekka.sort(reverse=True)
print(kekka)

#空間的計算（ユークリッド）
name = input("調べたい場所を入力してください")
space = da.get_spots_by_space(name)
space = np.array(space)
spot_list = da.get_space()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(3,4)
kekka = []
for item in a:
    kekka.append([item[0], np.linalg.norm(item[1:].astype(np.float) - space.astype(np.float))])
print(kekka)

#時間的計算（内積）
name = input("調べたい場所を入力してください")
time = da.get_spots_by_time(name)
time = np.array(time)
spot_list = da.get_time()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(3,3)
kekka = []
for item in a:
    kekka.append([item[0], np.sum(item[1:].astype(np.float) * time.astype(np.float))])
print(kekka)






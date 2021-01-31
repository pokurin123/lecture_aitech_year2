import sys
from dijk_spot import send_dist
hogehoge = send_dist()
elgo = []
city_dic = {}
class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)]
            for row in range(vertex)]

    def printSolution(self, dist):
        print ("Vertex distance from source")
        for node in range(self.V):
            print (node, " ", dist[node])
            elgo.append(dist[node])
    def minDistance(self, dist, spots):
    # Initilaize minimum distance for next node
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and spots[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    
    def dijkstra(self,src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spots = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist,spots)
            spots[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and spots[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
#Main
#任意に入力でスタート地点を変更
#---------------------------------
#---------------------------------
start_point = "江戸東京たてもの園"
#---------------------------------
#---------------------------------

#行きたい場所を入力
#---------------------------------
#---------------------------------
wanna_go = ["けやき公園","都立武蔵国分寺公園","お鷹の道・真姿の池湧水群","昭和記念公園"]
#---------------------------------
#---------------------------------

#ダイクストラ入力用リスト
spot_dist = []
#---------------------------------
#距離とスポット名を持ってくる
get_form_return = hogehoge.dist_maker()
get_dist = get_form_return[0]
get_name = get_form_return[1]
#---------------------------------
#出力用辞書にて使うspotのidリスト
id_box = []
#---------------------------------
#スタート地点をspot_distに格納
point_count = 0
for i in get_name:
    if i == start_point:
        point_number = point_count
        spot_dist.append(get_dist[point_count])
        id_box.append(point_number)
    else:
        point_count += 1

#---------------------------------
#行きたい場所をspot_distに格納
for i in wanna_go:
    id_count = 0
    for num in get_name:
        if num == i:
            spot_dist.append(get_dist[id_count])
            id_box.append(id_count)
        else:
            id_count += 1

#---------------------------------
#出力用
print(" \n")
print("<開始地点>：" + start_point)
print(" \n")
print("<目的地群>")
for i in wanna_go:
    print("・" + i)
#---------------------------------
#ダイクストラに入力
print(" \n")
print("<使用するダイクストラ算出リスト>")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
g = Graph(len(spot_dist))
g.graph = spot_dist
#諸々のリストの頭がスタート地点なので0のままでOK
g.dijkstra(0);
#---------------------------------
#出力用にスポット名と距離を辞書で格納
elgo_count = 0
for i in id_box:
    city_dic[get_name[i]] = elgo[elgo_count]
    elgo_count += 1

#---------------------------------
#格納した辞書をソート
show_root = sorted(city_dic.items(), key=lambda x:x[1])

#出力
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("<最短ルートを表示>")
print("ルート案内開始")
print("↓")
for i in range(0,len(elgo)):
    show_root_name = show_root[i]
    print(show_root_name[0])
    print("↓")
    if i < len(elgo) - 1:
        print("-------------------------")
print("ルート案内終了")
print("\n")
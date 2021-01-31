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

get_form_return = hogehoge.dist_maker()
get_dist = get_form_return[0]
get_name = get_form_return[1]
#print(hogehoge.dist_maker[1])
g = Graph(len(get_dist))
g.graph = get_dist

#任意に入力でスタート地点を変更
#---------------------------------
#---------------------------------
start_point = "武蔵国分寺跡"
#---------------------------------
#---------------------------------
point_count = 0
for i in get_name:
    if i == start_point:
        point_number = point_count
    else:
        point_count += 1

g.dijkstra(point_number);
for i in range(0,len(elgo)):
    city_dic[get_name[i]] = elgo[i]

show_root = sorted(city_dic.items(), key=lambda x:x[1])

print("ルート案内開始")
print("↓")
for i in range(0,len(elgo)):
    show_root_name = show_root[i]
    print(show_root_name[0])
    print("↓")
    if i < len(elgo) - 1:
        print("-------------------------")
print("ルート案内終了")

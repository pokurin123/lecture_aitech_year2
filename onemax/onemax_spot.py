
from onemax_dataaccess import DataAccess
import itertools
class spots:
    def send_spot(self):
        hoge = DataAccess()
        name = {}
        x2 = []
        y2 = []
        count = 0

        #ロケーション名を辞書に格納
        for id_n in range(1,11):
            x = list(itertools.chain.from_iterable(hoge.get_spots3(id_n)))
            name[count] = x[0]
            count += 1

        x = list(itertools.chain.from_iterable(hoge.get_spots()))
        y = list(itertools.chain.from_iterable(hoge.get_spots2()))

        #緯度経度を整形
        for i in range(0,10):
            x2.append(x[i] / 100)
            y2.append(y[i] / 1000)
        #緯度経度をタプルでまとめて格納
        pepoi = []
        for i in range(0,len(x2)):
            m = (x2[i],y2[i])
            pepoi.append(m)
        
        return pepoi,name


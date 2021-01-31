from pre_dataaccess import DataAccess
import itertools

for id_n in list(range(1,10)):
    hoge = DataAccess()
    x = list(itertools.chain.from_iterable(hoge.get_spots(id_n)))
    x.insert(6,"amusement")
    x.insert(5,"religion")
    x.insert(4,"nature")
    x.insert(3,"culture")
    x.insert(2,"history")
    x.insert(1,"rating_5Lv")
    x.insert(0,"spot_type")

    print(x)
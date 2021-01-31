from dijk_var import Var
from dijk_db import DB
class DataAccess:
    def get_spots(self,id_n):
        query = "SELECT spot_name,spot_location,spot_latitude,spot_longitude,nearest_station FROM myspot_day5 WHERE ID =" + str(id_n)
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
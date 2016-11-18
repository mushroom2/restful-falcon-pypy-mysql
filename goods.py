import falcon
import mysql_data
import json
import datetime

mycon = mysql_data.MySQLData()
mycon.connect_to_db('localhost', 'mushroom', '123333', 'restfulshopdb')

def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()

class ThingsResource(object):


    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        res = mycon.get_data('SELECT * FROM goods')
        resp.body = json.dumps(res, default=my_date)




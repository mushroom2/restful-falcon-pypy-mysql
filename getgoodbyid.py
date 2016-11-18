import mysql_data
import json
import falcon
import datetime

mycon = mysql_data.MySQLData()
mycon.connect_to_db('localhost', 'mushroom', '123333', 'restfulshopdb')


def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()


class GetGoodById():

    def on_get(self, req, resp, goodid):
        res = mycon.get_data('SELECT good_name, date, in_shop, good_price FROM goods WHERE good_id = ' + goodid)
        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res, default=my_date)




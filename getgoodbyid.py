import mysql_data
import json
import falcon
import datetime


def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()


class GetGoodById():

    def __init__(self):
        self.mycon = mysql_data.MySQLData()

    def on_get(self, req, resp, goodid):
        self.mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample', 'sfera1488', 'falcontexample$restfulshopdb')
        res = self.mycon.get_data('SELECT good_name, date, in_shop, good_price FROM goods WHERE good_id = ' + goodid)
        if not res:
            raise falcon.HTTPError(falcon.HTTP_404, '404', 'Cant`t found this object')
        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res, default=my_date)
        self.mycon.disconnect_from_db()

    def on_delete(self, req, resp, goodid):
        self.mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample', 'sfera1488', 'falcontexample$restfulshopdb')
        self.mycon.delete_row(goodid)
        resp.set_header('Content-Type', 'text; charset=utf-8')
        resp.status = falcon.HTTP_202
        resp.body = ('%s id successfully deleted' % goodid)
        self.mycon.disconnect_from_db()






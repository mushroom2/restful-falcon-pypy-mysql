import mysql_data
import json
import falcon
import datetime


def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()


class GetGoodById():

    def on_get(self, req, resp, goodid):
        mycon = mysql_data.MySQLData()
        mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample',
                    'sfera1488', 'falcontexample$restfulshopdb')
        res = mycon.get_data('SELECT good_name, date, in_shop, good_price FROM goods WHERE good_id = ' + goodid)
        if not res:
            raise falcon.HTTPError(falcon.HTTP_404, '404', 'Cant`t found this object')
        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res, default=my_date)
        mycon.disconnect_from_db()




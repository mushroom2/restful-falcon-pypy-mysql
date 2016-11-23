import falcon
import mysql_data
import json
import datetime



def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()


class GoodsResource(object):

    def __init__(self):
        self.mycon = mysql_data.MySQLData()

    def on_get(self, req, resp):
        self.mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample', 'sfera1488', 'falcontexample$restfulshopdb')
        resp.status = falcon.HTTP_200  # This is the default status
        res = self.mycon.get_data('SELECT * FROM goods')
        resp.body = json.dumps(res, default=my_date)
        self.mycon.disconnect_from_db()

    def on_post(self, req, resp):
        self.mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample', 'sfera1488', 'falcontexample$restfulshopdb')
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)
        try:
            res = json.loads(raw_json, encoding='utf-8')
            self.mycon.post_data(("INSERT INTO goods (good_name, in_shop, good_price )"
                                 " VALUES (%s, %s, %s)"),
                                 (res['good_name'], res['in_shop'], res['good_price']))

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', 'Could not decode the request body.'
                                                                    ' The ''JSON was incorrect.')
        resp.status = falcon.HTTP_202
        resp.body = 'Successfully inserted'
        self.mycon.disconnect_from_db()

    def on_delete(self, req, resp):
        self.mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample', 'sfera1488', 'falcontexample$restfulshopdb')
        self.mycon.delete_collection()
        resp.status = falcon.HTTP_202
        resp.body = ('Table clean')
        self.mycon.disconnect_from_db()


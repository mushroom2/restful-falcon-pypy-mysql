import falcon
import mysql_data
import json
import datetime

mycon = mysql_data.MySQLData()
mycon.connect_to_db('falcontexample.mysql.pythonanywhere-services.com', 'falcontexample$restfulshopdb',
                    'sferalaser1488', 'restfulshopdb')

def my_date(dat):
    if isinstance(dat, datetime.datetime):
        return dat.__str__()

class GoodsResource(object):


    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        res = mycon.get_data('SELECT * FROM goods')
        resp.body = json.dumps(res, default=my_date)

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)
        try:
            res = json.loads(raw_json, encoding='utf-8')
            mycon.post_data(("INSERT INTO goods (good_name, in_shop, good_price )"
                             " VALUES (%s, %s, %s)"),
                            (res['good_name'], res['in_shop'], res['good_price']))

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', 'Could not decode the request body. The ''JSON was incorrect.')
        resp.status = falcon.HTTP_202
        resp.body = 'Successfully inserted'


__author__ = 'mushroom'

import falcon
import goods

app = falcon.API()

dbtest = goods.ThingsResource()

app.add_route('/goods', dbtest)
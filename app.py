__author__ = 'mushroom'

import falcon
import goods
import getgoodbyid

app = falcon.API()

goodsall = goods.ThingsResource()
goodsbyid = getgoodbyid.GetGoodById()


app.add_route('/goods', goodsall)
app.add_route('/goods/{goodid}', goodsbyid)
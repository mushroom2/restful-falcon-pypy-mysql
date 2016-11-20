__author__ = 'mushroom'

import falcon
import goods
import getgoodbyid
import index

app = falcon.API()

goodsall = goods.GoodsResource()
goodsbyid = getgoodbyid.GetGoodById()
startpage = index.IndexResource()

app.add_route('/', startpage)
app.add_route('/goods', goodsall)
app.add_route('/goods/{goodid}', goodsbyid)
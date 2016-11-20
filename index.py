import falcon

class IndexResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nHello world!\n'
                     '\n This is my firs falcon web api'
                     '\n This is sample of simple shop model'
                     '\n "/goods" - GET all goods'
                     '\n "goods/{id}" - GET good by ID'
                     )


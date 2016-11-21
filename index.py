import falcon

class IndexResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\n Hello, world!\n'
                     '\n This is my first falcon web api'
                     '\n This is the sample of a simple shop model'
                     '\n "/goods" - GET all products'
                     '\n You may add any product in the table by the POST method from "/goods"'
                     '\n you have to send json (for example) { "in_shop": 1/0 *product availability*, '
                     '"good_name": "your product name", "good_price": *your product price*}'
                     '\n "goods/{id}" - GET products by ID'
                     '\n '
                     )


import falcon
import statsd

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        c = statsd.StatsClient('localhost', 8125)
        c.incr('helloItsMe')
        resp.media = quote

api = falcon.API()
api.add_route('/hello', QuoteResource())
from python import flask, json
from flask import rumps

class AwesomeStatusBarApp(rums.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Brian")
        self.menu = ["Quering API..."]

        
        @rumps.timer(1)
        def sayhi(self, _):
            headers = {
                'Content-Type': 'aplication/json',
            }
            r = request.get("https://api.coinbase.coom/v2/exchanges-rates?currency=BTC")
            print(r.json()['data'] ['rates'] ['EUR'])
            self.tittle = r.json( ) ['data'] ['rates'] ['EUR']


    if __name__ == "__main__":
        AwesomeStatusBarApp().run()





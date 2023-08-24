from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=0da99b52a0c62d2c7e58ff65e8748bc1')
pprint(r.json)


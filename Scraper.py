from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id': '1'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'API KEY',
}

session = Session()
session.headers.update(headers)

while True:
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        output_file_day = open("output_2.txt", "a")
        print(data['status']['timestamp'][11:-5], data['data']['1']['quote']['USD']['price'], sep=', ', file=output_file_day)
        print(data['status']['timestamp'][11:-5], data['data']['1']['quote']['USD']['price'], sep=', ')
        output_file_day.close()
        time.sleep(120)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        time.sleep(30)

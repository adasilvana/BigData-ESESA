import datetime
import logging
import requests

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=FGJPN2ZCXI431EQO"
    r = requests.get(url)
    data = r.json()

    logging.info('Cotización: %s', data)
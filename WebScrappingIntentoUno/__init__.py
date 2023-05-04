import datetime
import logging
import requests

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    url = "https://www.librerialuces.com/es/libro/el-cuco-de-cristal_672991"
    r = requests.get(url)
    data = r.json()

    logging.info('Cotización: %s', data)

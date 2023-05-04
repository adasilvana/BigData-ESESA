import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info('Hola!', utc_timestamp)

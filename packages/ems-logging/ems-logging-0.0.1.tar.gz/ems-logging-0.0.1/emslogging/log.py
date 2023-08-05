import logging
import sys
import time


def default_logging_config():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )
    logging.Formatter.converter = time.gmtime

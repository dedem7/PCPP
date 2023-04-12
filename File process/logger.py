#LOGGING TEMPERATURE OF MOBILE PHONE

import logging
import random
import time


logger = logging.getLogger('temperature')
logging.basicConfig(level = logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log',mode='a')

FORMAT = "%(name)s:%(levelname)s:%(asctime)s:%(message)s"
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range(61):
    #time.sleep(60)
    temperature = random.randrange(20,41)

    if temperature < 30:
        logger.debug("DEBUG – {} C".format(str(temperature)))
    elif temperature>=30 and temperature<=35:
        logger.warning("WARNING – {} C".format(str(temperature)))
    else:
        logger.critical("CRITICAL – {} C".format(str(temperature)))

    

import logging
import sys

def getLogger(nombre=__name__):
    logger= logging.getLogger(nombre)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        consola = logging.StreamHandler()

        formato = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        consola.setFormatter(formato)
        logger.addHandler(consola)
    
    return logger
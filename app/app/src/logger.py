import logging

from app.core.DBHandler import DBHandler


def getLogger(nombre=__name__):

    logger = logging.getLogger(nombre)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        consola = logging.StreamHandler()

        #db = DBHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(usuario)s | %(clase)s | %(metodo)s | %(detalle)s | %(message)s"
        )

        consola.setFormatter(formatter)

        #db.setFormatter(formatter)

        logger.addHandler(consola)

        #logger.addHandler(db)

    return logger

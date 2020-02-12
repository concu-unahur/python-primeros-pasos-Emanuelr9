import threading
import time
import logging


def dormir():
    logging.info('Empenzado')
    time.sleep(1)
    logging.info('Finalizado')


    
class UnThread(threading.Thread):
    def __init__(self):
        super().__init__() 
        self.name = 'threadClase'

    def run(self):
        logging.info('Empezando')
        time.sleep(1)
        logging.info('Finalizado')
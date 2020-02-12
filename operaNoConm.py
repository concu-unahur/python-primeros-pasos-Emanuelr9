import threading
import time
import logging


from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num=10
#Escpeci de advertencia

semaforo = threading.Semaphore(1)

lock=threading.Lock()

def sumarUno():

    global num
    global lock
    
    try:
        num +=1
       
    finally:
       lock.release() #¿qué pasa si comento este release y descomento el pass


def multiplicarPorDos():

    global num
    global lock

    lock.acquire()
    
    try:
            num *=2          
    finally:

     lock.release()


t1 = threading.Thread(target=sumarUno, name='Sumar')
t2 = threading.Thread(target=multiplicarPorDos, name='Multiplicar')

lock.acquire()

t2.start()
t1.start()


t2.join()
logging.info(f'valor final {num}')

#print(num)
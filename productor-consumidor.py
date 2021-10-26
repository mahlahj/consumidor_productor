"""
Intendo de solución al problema de consumidor - productor usando semaforos
"""
import threading
import time
import logging
import random
import queue
import keyboard
import sys

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

TAMANO_BUFER = 20
q = queue.Queue(TAMANO_BUFER)

# Declaración de semáforos
mutex = threading.Semaphore()
empty = threading.Semaphore(TAMANO_BUFER)
full = threading.Semaphore(0)

class hiloProductor(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(hiloProductor,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,20)
                q.put(item)
                logging.debug('Colocando ' + str(item) + ' : ' + str(q.qsize()) + ' hamburguesas en la mesa.')
                time.sleep(random.random())
        return

class hiloConsumidor(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(hiloConsumidor,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Obteniendo ' + str(item) + ' : ' + str(q.qsize()) + ' hamburguesas de la mesa.')
                time.sleep(random.random())
        return

if __name__ == '__main__':
    
    p = hiloProductor(name='PRODUCTOR')
    c = hiloConsumidor(name='Consumidor')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)

    keyboard.wait("esc")
    sys.exit()
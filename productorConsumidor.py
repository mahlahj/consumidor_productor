import threading
import random
import time
import keyboard
 
# Variables de memoria compartida. 
BUFFER = 20
buffer = [-1 for i in range(BUFFER)]
en_indice = 0
fuera_indice = 0
 
# Declaración de semáforos.
mutex = threading.Semaphore()
vacio = threading.Semaphore(BUFFER)
lleno = threading.Semaphore(0)
 
# Hilo Productor.
class Productor(threading.Thread):
  def run(self):
     
    global BUFFER, buffer, en_indice, fuera_indice
    global mutex, vacio, lleno
     
    objetos_producidos = 0
    contador = 0
     
    while objetos_producidos < 20:
      dormir = random.uniform(1.2, 3.5)
      vacio.acquire()
      mutex.acquire()
      print("\nProductor se acerca a la mesa.\n")
       
      contador += 1
      buffer[en_indice] = contador
      en_indice = (en_indice + 1)%BUFFER
      print("\n\nProductor produjo hamburguesa: ", contador)
       
      mutex.release()
      lleno.release()
      print("\nProductor regresa a su puesto.\n")
       
      time.sleep(dormir)
      print("\n\nProductor se fue a dormir por ", dormir, "segundos.")
       
      objetos_producidos += 1
 
# Hilo Consumidor.
class Consumidor(threading.Thread):
  def run(self):
     
    global BUFFER, buffer, en_indice, fuera_indice, contador
    global mutex, vacio, lleno
     
    objeto_consumido = 0
     
    while objeto_consumido < 20:
      dormir = random.uniform(1.2, 3.5)
      lleno.acquire()
      mutex.acquire()
      print("\nConsumidor se acerca a la mesa.\n")
       
      objeto = buffer[fuera_indice]
      fuera_indice = (fuera_indice + 1)%BUFFER
      print("\n\nConsumidor consumió hamburguesa: ", objeto)
       
      mutex.release()
      vacio.release()
      print("\nConsumidor regresa a su silla.\n")      
       
      time.sleep(dormir)
      print("\n\nConsumidor se fue a dormir por ", dormir, "segundos,")
       
      objeto_consumido += 1
 
# Creación de Hilos.
productor = Productor()
consumidor = Consumidor()
 
# Inicialización de Hilos.
consumidor.start()
productor.start()
 
# Espera de terminación de hilos
productor.join()
consumidor.join()

keyboard.wait("esc")
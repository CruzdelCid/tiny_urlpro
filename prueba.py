from redis import Redis 
import time
from datetime import date
from datetime import datetime

print("PRUEBA PARA VERIFICAR SI ES UNA PÁGINA")
paginas = {'', 'urls',  'stats', 'admin', 'load', 'search'}



"""
print('stats' in paginas)
print('admin' in paginas)
print('load' in paginas)
print('search' in paginas)
print('pr' in paginas)
print('ueba' in paginas)


print("")
print("")
print("PRUEBA DEL TRY EXCEPT")
#https://www.w3schools.com/python/python_try_except.asp usemos try y except para evitarnos problemas
#https://riptutorial.com/es/flask/example/7981/rutas-basicas con esto ponemos convertidores del id en la URL
#Diccionario
dicci = {"1":"uno", "dos":"2"}
print(dicci['1'])
print(dicci['dos'])
try: 
    print(dicci['4'])
except:
    print("error")

"""

print("")
print("")
print("PRUEBA GETALL DE REDIS")
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
#redis_visitas = Redis('localhost', port=7000, charset="utf-8", decode_responses=True)

# print(redis.setnx(f"{key_2}_date", datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

def comprobar(key_1):
    return False

def crear(key_2, valor):
    print("")
    if (comprobar(key_2) == False):
        dicci = {} 
        print(redis.setnx(key_2, valor)) 
        #print(redis_visitas.setnx(key_2, 0))

        #f"{date.today()}
        dicci[key_2] = redis.get(key_2)
        #dicci[f"{key_2}_visitas"] = redis_visitas.get(key_2)
        print(dicci)
    else:
        print("El key ya existe")
    

key = "qwerty"
val = "www.google.com"


crear(key, val)
"""
crear("url", val)

crear("stats", val)

crear("Daniel", "www.facebook.com/daniel")

crear(key, val)



redis.delete('*')
redis.delete(f"{key}_visitas")
redis.delete(f"{key}_date")
"""

print("ALV")
lista = redis.keys('*')
#lista_visitas = redis_visitas.key('*')
print(lista)
#print(lista_visitas)

for m in lista: 
    redis.delete(m)

#for m in lista_visitas: 
#    redis_visitas.delete(m)

print(redis.keys('*'))
print(redis.keys('*'))









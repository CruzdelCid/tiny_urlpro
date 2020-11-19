from redis import Redis 
import time
from datetime import date
from datetime import datetime

print("PRUEBA PARA VERIFICAR SI ES UNA PÁGINA")
paginas = {'', 'stats', 'admin', 'load', 'search'}

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



print("")
print("")
print("PRUEBA GETALL DE REDIS")
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
#edis_visitas = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
#redis_date = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)

def comprobar(key_1):
    val = False
    if (key_1 in paginas):
        val = True
    return val 

def crear(key_2, valor):
    if (comprobar(key_2) == False): 
        redis.set(key_2, valor)
        redis.set(f"{key_2}_visitas", 0)
        redis.set(f"{key_2}_date", 0)
        print(key_2)
        print(redis.get(key_2))
        print(redis.get(f"{key_2}_visitas"))
        print(redis.get(f"{key_2}_date"))
    else:
        print("El key ya existe")
    

key = "qwerty"
val = "www.google.com"

print(date.today())
print(datetime.now())
print(type(date.today()))

crear(key, val)

crear("url", val)

crear("stats", val)

crear(key, val)








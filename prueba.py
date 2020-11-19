from redis import Redis 
import time
from datetime import date
from datetime import datetime
import random





#https://www.w3schools.com/python/python_try_except.asp usemos try y except para evitarnos problemas
#https://riptutorial.com/es/flask/example/7981/rutas-basicas con esto ponemos convertidores del id en la URL
#Diccionario


redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)

# print(redis.setnx(f"{key_2}_date", datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

pages = {'urls', 'stats', 'admin', 'load', 'search'}

def generador(valor): 
    word = valor.replace(".", "")
    word = word.replace("/", "")
    new_key = ""
    num = "1234567890"
    while word and len(new_key) < 7:
        position = random.randrange(len(word))
        new_key += word[position]
        new_key += num[random.randrange(len(num))]
        word = word[:position] + word[(position + 1):]
    return new_key 

def comprobar(key): 
    estado = False
    keys = redis.keys('*')
    if (key in pages): 
        estado = True 
    elif key in keys:
        estado = True
    return estado


diccionario = {'url':'www.google.com', 'visitas': 0, 'date': ''}

def crear(key, valor):
    key = key.replace(" ", "")
    if (key == ""):
        key = generador(valor)

    if (comprobar(key) == False):
        dicci = {}
        dicci['url'] = valor
        dicci['visitas'] = 0
        dicci['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        print(redis.hmset(key, dicci)) 
        print(key)
        print(redis.hgetall(key)) 
        return dicci
    else:
        print(f"El key: {key} ya existe.")
    

key_p = "qwerty"
val_p = "www.google.com"


crear(key_p, val_p)
crear("Marcoshdp", "www.google.com")
crear("", "//www.page.com")
crear("", "www.youtube.com/")
crear("Daniel", "www.youtube.com/")


print("")
lista = redis.keys('*')
print(lista)
for m in lista: 
    redis.delete(m)

print(redis.keys('*'))


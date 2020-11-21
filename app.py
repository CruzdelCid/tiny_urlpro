from flask import Flask, request, render_template, url_for, redirect
from redis import Redis 
from datetime import date
from datetime import datetime
import random

pages = ('', 'urls',  'stats', 'admin', 'load', 'search')
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)



#Generacion del key donde se guardara la url normal en el redis
def generador(valor): 
    word = valor.replace(".", "")
    word = word.replace("/", "")
    word = word.replace(":", "")
    new_key = ""
    num = "1234567890"

    while word and len(new_key) < 7:
        position = random.randrange(len(word))
        new_key += word[position]
        new_key += num[random.randrange(len(num))]
        word = word[:position] + word[(position + 1):]
    return new_key 


#Comprobacion de que el key generado sea unico y no coincida con nuestros urls internos
def comprobar(key): 
    estado = False
    keys = redis.keys('*')

    if (key in pages): 
        estado = True 
    elif key in keys:
        estado = True
    return estado


#Ejemplo inciial
diccionario = {'url':'www.google.com', 'visitas': 0, 'date': '20-11-2020'}

#Funcion que borra todos los elementos en el redis
def reset(): 
    lista = redis.keys('*')
    print(lista)
    for m in lista: 
        redis.delete(m)
    print(redis.keys('*'))

def lista(): 
    lista = redis.keys('*')
    print(lista)
    for m in lista: 
        print(redis.hgetall(m)) 
    

#Creacion de elementso en el redis, ya con las verificaciones respectivas
def crear(key, valor):
    key = key.replace(" ", "")
    if (valor == ""):
        return {}
    else:
        if (key == "" and valor != ""):
            key = generador(valor)

        if (comprobar(key) == False and valor != ""):
            dicci = {}
            dicci['key'] = key 
            dicci['url'] = valor
            dicci['visitas'] = 0
            dicci['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            print(redis.hmset(key, dicci)) 
            print(key)
            print(redis.hgetall(key)) 
            return dicci
        else:
            print(f"El key: {key} ya existe.")
            return {}
        
#lista()
#reset()
#crear("hola", "https://www.youtube.com/?hl=es-419")
#crear("FFF", "https://www.ufm.edu/Portal")
#crear("", "https://motionarray.com/browse")


#New tiny
#methods = ["GET", "SET"]
@app.route('/', methods=['GET', 'POST'])
def index():
    urlLarga = request.args.get("URL", "")
    keyOp = request.args.get("key", "")
    result = crear(keyOp, urlLarga)
    #result = {'key':'qwerty', 'url':"www.google.com", 'visitas': 1000, 'date':'20-11-2020'}
    return render_template("index.html", result=result)


@app.route("/stats")
def stats():
    return "stats"

#administración del equipo
@app.route("/admin")
def admin():
    return "admin"


@app.route("/load")
def load():
    return "load"

#Buscar url
@app.route("/search")
def search():
    return "search"

#Imprime las URLs
@app.route("/urls")
def urls():
    key_borrar = request.args.get("keyb", "")
    if key_borrar:
        redis.delete(key_borrar)
    urls = {}
    ke = redis.keys("*")
    if (ke): 
        for key in ke: 
            urls[key] = redis.hgetall(key)
    print(urls)
    return render_template("urls.html", urls = urls)

#Maneja el error 404 propio de la app
@app.route("/error")
def error():
    return render_template("navbar.html")
    
#Entrar a un Tiny_URL 
@app.route("/<string_v>")
def prueba(string_v=None):
    print(string_v)
    url = redis.hget(string_v, 'url')
    print(type(url))
    if (url == None):
        return redirect("/error")
    else:
        vist = int(redis.hget(string_v, 'visitas')) + 1
        print(vist)
        print(type(vist))
        redis.hset(string_v, 'visitas', vist)
        print(url)
        print(type(url))
        return redirect(url)


if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)

from flask import Flask, request, render_template, url_for, redirect
from redis import Redis 
from datetime import date
from datetime import datetime
import random

pages = {'', 'urls',  'stats', 'admin', 'load', 'search'} 
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)



#Generacion del key donde se guardara la url normal en el redis
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


#Comprobacion de que el key generado sea unico y no coincida con nuestros urls internos
def comprobar(key): 
    estado = False
    keys = redis.keys('*')

    if (key in pages): 
        estado = True 
    elif key in keys:
        estado = True
    return estado


#Ejemplo
diccionario = {'url':'www.google.com', 'visitas': 0, 'date': ''}

#Creacion de elementso en el redis, ya con las verificaciones respectivas
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

crear("hola", "https://www.youtube.com/?hl=es-419")
crear("FFF", "https://www.ufm.edu/Portal")
crear("", "https://motionarray.com/browse")


#New tiny
#methods = ["GET", "SET"]
@app.route('/', methods=['GET', 'POST'])
def index():
    urlLarga = request.args.get("URL", "")
    keyOp = request.args.get("Key", "")
    result = crear(keyOp, urlLarga)
    return render_template("index.html", key=keyOp, result=result)

#https://tin.com/admin
#URL list


@app.route("/stats")
def stats():
    pass

#administración del equipo
@app.route("/admin")
def admin():
    pass


@app.route("/load")
def load():
    pass

#Buscar url
@app.route("/search")
def search():
    pass

#Imprime las URLs
@app.route("/urls", methods = ["DELETE"] )
def urls():
    return "prueba de otras rutas"

#Maneja el error 404 propio de la app
@app.route("/error")
def error():
    return render_template("index.html")
    
#Entrar a un Tiny_URL 
@app.route("/<string_v>")
def prueba(string_v=None):
    url = redis.hget(string_v, 'url')
    if (url == None):
        return redirect("/error")
    else:
        print(url)
        print(type(url))
        return redirect(url)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)

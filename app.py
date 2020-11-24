from flask import Flask, request, render_template, url_for, redirect
import redis 
from datetime import date
from datetime import datetime
import random
import os

pages = ('', 'urls',  'stats', 'admin', 'load', 'search', 'eliminar')
REDIS_HOST = os.getenv("REDIS_HOST", None)
redis = redis.Redis(host=REDIS_HOST, port=6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


#Generacion del key donde se guardara la url normal en el redis
def generador(valor): 
    word = valor.replace(".", "")
    word = word.replace("/", "")
    word = word.replace(":", "")
    word = word.replace("=", "")
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


#Ejemplo incial
diccionario = {'url':'www.google.com', 'visitas': 0, 'date': '20-11-2020'}


#Funcion que borra todos los elementos en el redis
def reset(): 
    lista = redis.keys('*')
    for m in lista: 
        redis.delete(m)

def lista(): 
    lista = redis.keys('*')
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

            redis.hmset(key, dicci)
            return dicci
        else:
            print(f"El key: {key} ya existe.")
            return {}
        

@app.route("/eliminar")
def eliminar():
    lista = redis.keys('*')
    for m in lista: 
        redis.delete(m)

    return redirect("/urls")
    

#methods = ["GET", "SET"]
@app.route('/', methods=['GET', 'POST'])
def index():
    urlLarga = request.args.get("URL", "")
    keyOp = request.args.get("key", "")
    result = crear(keyOp, urlLarga)
    return render_template("index.html", result=result)


#cantidad de visitas
@app.route("/stats")
def stats():
    urls = {}
    ke = redis.keys("*")
    if (ke): 
        for key in ke: 
            urls[key] = redis.hgetall(key)
    return render_template("visits.html", urls = urls)


#administración del equipo
@app.route("/admin", methods=['GET', 'POST'])
def admin():
    Usua = request.args.get("Usuario", "")
    Contra = request.args.get("Clave", "")
    validacion = ""

    if(Usua == "Marcos" and Contra == "CS052"):
        validacion = "VERDAD"

    return render_template("admin.html", validacion=validacion)


#Buscar url
@app.route("/search", methods=['GET', 'POST'])
def search():
    Busc = request.args.get("key", "")
    urls = {}
    ke = redis.keys("*")
    if (ke): 
        for key in ke: 
            if (key == Busc):
                urls[key] = redis.hgetall(key)
    return render_template("search.html", urls = urls)


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
    return render_template("urls.html", urls = urls)


#Maneja el error 404 propio de la app
@app.route("/error")
def error():
    return render_template("error.html")


#Entrar a un Tiny_URL 
@app.route("/<string_v>")
def prueba(string_v=None):
    url = redis.hget(string_v, 'url')
    if (url == None):
        return redirect("/error")
    else:
        vist = int(redis.hget(string_v, 'visitas')) + 1
        redis.hset(string_v, 'visitas', vist)
        print(url)
        return redirect(url)


if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)

from flask import Flask, request, render_template, url_for
from redis import Redis 

pages = {'', 'urls',  'stats', 'admin', 'load', 'search'} 
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


#Investigar codificador
def comprobar(key): 
    val = False
    if (key in pages):
        val = True
    return val


#New tiny
#methods = ["GET", "SET"]
@app.route("/", methods = ["GET", "SET"])
def tiny_url(): 
    if (request.method == "GET"):
        pass 
    #comprobar
    #crear un tiny
    return "HELLO WORLD"

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

#Buscar
@app.route("/search")
def search():
    pass

@app.route("/pais")
def pais():
    return "Guatemala"


@app.route("/urls", methods = ["DELETE"] )
def urls():
    return "prueba de otras rutas"
    
#Entrar a un Tiny_URL 
@app.route("/<string_v>")
def prueba(string_v=None):
    #Buscar 
    #Devolver URL y Código: 301 
    #Invetigar para que se retorne la página 
    return "Palabra: " + string_v

"""
    try:
        return "Palabra: " + string_v
    except: 
        return "HELLO WORLD!"
"""

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)

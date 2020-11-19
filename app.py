from flask import Flask, request, render_template
from redis import Redis 

pages = {'', 'stats', 'admin', 'load', 'search'}

<<<<<<< HEAD
=======
#Diccionario
dicci = {"1":"uno", "dos":"2"}
print(dicci['1'])
print(dicci['dos'])
try: 
    print(dicci['2'])
except:
    print("error")
>>>>>>> 400c38ed23a0e37964c5bc470755dbe940565aa6


"""
redis  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
redis_visitas = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)
redis_date = Redis('localhost', port=6379, charset="utf-8", decode_responses=True)



user = {"Nombre":"Cruz del Cid", "Carnet":"20200394", "edad":"17", "País":"Guatemala"}

conn.hmset("my_information", user)
conn.set("alv", "Hola mundo")

print(conn.hgetall("my_information", "Nombre"))
print(type(conn.hgetall("my_information")))

print(conn.hget("my_information", "Nombre"))
print(conn.get("alv"))
""" 




#Investigar codificador
#
def comprobar(key): 
    val = False
    if (key in pages):
        val = True
    return val

def new_tiny(key = None): 
    pass


app = Flask(__name__)


<<<<<<< HEAD
=======
@app.route("/urls")
def urls():
    pass

#Entrar a un Tiny_URL 
@app.route("/<string_v>")
def prueba(string_v=None):
    #Buscar 
    #Devolver URL y Código: 301 
    #Invetigar para que se retorne la página 
    return "Palabra: " + string_v


>>>>>>> 400c38ed23a0e37964c5bc470755dbe940565aa6
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

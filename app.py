from flask import Flask, request, render_template
from redis import Redis 


dicci = {"1":"uno", "dos":"2"}

print(dicci['1'])
print(dicci['dos'])

#https://www.w3schools.com/python/python_try_except.asp usemos try y except para evitarnos problemas
try: 
    print(dicci['4'])
except:
    print("error")


#https://riptutorial.com/es/flask/example/7981/rutas-basicas con esto ponemos convertidores del id en la URL






"""
conn  = Redis('localhost', port=6379, charset="utf-8", decode_responses=True )

user = {"Nombre":"Cruz del Cid", "Carnet":"20200394", "edad":"17", "País":"Guatemala"}

conn.hmset("my_information", user)
conn.set("alv", "Hola mundo")





print(conn.hgetall("my_information"))
print(type(conn.hgetall("my_information")))

print(conn.hget("my_information", "Nombre"))
print(conn.get("alv"))

"""
app = Flask(__name__)
@app.route("/")
@app.route("/<string_v>")
def prueba(string_v=None):
    if (string_v==None): 
        return "HELLO WORLD"
    else: 
        return "Palabra: " + string_v
"""
    try:
        return "Palabra: " + string_v
    except: 
        return "HELLO WORLD!"
"""
@app.route("/nombre")
def nombre():
    return "c"

@app.route("/carnet")
def carnet():
    return "20200394"

@app.route("/edad")
def edad():
    return "edad"

@app.route("/pais")
def pais():
    return "Guatemala"

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)

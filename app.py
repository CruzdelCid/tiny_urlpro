from flask import Flask, request, render_template
from redis import Redis 


dicci = {"1":"uno", "dos":"2"}

print(dicci['1'])
print(dicci['dos'])

#https://www.w3schools.com/python/python_try_except.asp
try: 
    print(dicci['4'])
except:
    print("error")


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
def hello_word():
    return "Hello Word"

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
    app.run(host = "peronal_url", port = 5000, debug = True)

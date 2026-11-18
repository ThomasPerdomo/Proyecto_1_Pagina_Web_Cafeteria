import json
from flask import Flask, jsonify, send_file, render_template

def cargar_datos():
    with open("data.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

app = Flask(__name__)

@app.route("/")
def inicio():
    datos = cargar_datos()
    # Le mandamos todo el JSON al HTML en una sola variable llamada "datos"
    return render_template("index.html", datos = datos)

@app.route("/menu")
def menu():
    datos = cargar_datos()
    return render_template("menu.html", datos = datos)

@app.route("/menu/calientes")
def calientes():
    datos = cargar_datos()
    return render_template("calientes.html", datos = datos)

@app.route("/menu/frios")
def frios():
    datos = cargar_datos()
    return render_template("frios.html", datos = datos)  

@app.route("/menu/panes")
def panes():
    datos = cargar_datos()
    return render_template("panes.html", datos = datos)  

@app.route("/menu/comida")
def comida():
    datos = cargar_datos()
    return render_template("comida.html", datos = datos)

@app.route("/menu/cafe_grano")
def cafe_grano():
    datos = cargar_datos()
    return render_template("cafe_grano.html", datos = datos)

@app.route("/sedes")
def sedes():
    datos = cargar_datos()
    return render_template("sedes.html", datos = datos)
    
if __name__ == "__main__":
    app.run(debug=True)


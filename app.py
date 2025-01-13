from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el menú principal
@app.route("/")
def index():
    return render_template("index.html")


# Ruta para el formulario 1
@app.route("/Ejercicio_1", methods=["GET", "POST"])
def Ejercicio_1():
    promedio, estado = None, None
    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

    return render_template("Ejercicio_1.html", promedio=promedio, estado=estado)


# Ruta para el formulario 2
@app.route("/Ejercicio_2", methods=["GET", "POST"])
def Ejercicio_2():
    nombre, longitud = None, None
    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        nombres = [nombre1, nombre2, nombre3]
        nombre = max(nombres, key=len)
        longitud = len(nombre)

    return render_template("Ejercicio_2.html", nombre=nombre, longitud=longitud)

if __name__ == "__main__":
    app.run(debug=True)


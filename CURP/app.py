from curp import generar_curp
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre').upper().replace('Ñ', 'N')    # Nombre
        ap = request.form.get('primerApellido').upper().replace('Ñ', 'N')       # Apellido paterno
        am = request.form.get('segundoApellido').upper().replace('Ñ', 'N')       # Apellido materno
        an = request.form.get('anonacimiento')       # Año de nacimiento
        mn = request.form.get('mesNacimiento')       # Mes de naciemiento
        dn = request.form.get('diaNacimiento')       # Dia de nacimiento
        entidad = request.form.get('estado')  # Entidad
        sexo = request.form.get('sexo')     # Sexo

        final = generar_curp(nombre, ap, am, an, mn, dn, entidad, sexo)

        return render_template('index.html', valor=final)

    return render_template('index.html', valor='')

if __name__ == "__main__":
    app.run(debug=True)
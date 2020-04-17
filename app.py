from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("Principal.html")

@app.route('/potencia/<base>/<exponente>')
def potencia(base,exponente):
    base=int(base)
    exponente=int(exponente)
    if exponente == 0:
        resultado=1
    elif exponente < 0:
        resultado=(1/base)**abs(exponente)
    elif exponente > 0:
        resultado=base**exponente
    else:
        abort(404)
    return render_template("Potencias.html",base=base,exponente=exponente,resultado=resultado)

app.run(debug=True)
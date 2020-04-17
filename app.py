from flask import Flask, render_template
from lxml import etree
libro=etree.parse("libros.xml")
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

@app.route('/cuenta/<palabra>/<letra>')
def cuenta(palabra,letra):
    if len(letra) != 1:
        abort(404)
    resultado=palabra.count(letra)
    return render_template("Cuenta.html",palabra=palabra,letra=letra,resultado=resultado)

@app.route('libro/<int:codigo>')
def libro(codigo):
    nombre=libro.xpath('/biblioteca/libro[codigo="%i"]/titulo/text()' % codigo)
    autor=libro.xpath('/biblioteca/libro[codigo="%i"]/titulo/text()' % codigo)
    return render_template("libro.html",nombre=nombre,autor=autor)
app.run(debug=True)
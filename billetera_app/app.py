from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

def obtener_cuenta(numero):
    return next((cuenta for cuenta in BD if cuenta.numero == numero), None)

# Inicializar la aplicación con un conjunto de cuentas y contactos
BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]

@app.route('/')
def examen():

    titulo = '<h1>Examen de Software I</h1>'
    alumno = '<h3>Sebastian Chu</h3>'
    metodo1 = '<p>/billetera/contactos?minumero=21345<p>'
    metodo2 = '<p>/billetera/pagar?minumero=21345&numerodestino=123&valor=100<p>'
    metodo3 = '<p>/billetera/pagar?minumero=123&numerodestino=456&valor=50<p>'
    metodo4 = '<p>/billetera/historial?minumero=123</p>'

    mensaje = f'{titulo}{alumno}{metodo1}{metodo2}{metodo3}{metodo4}'
    return mensaje

@app.route('/billetera/contactos', methods=['GET'])
def obtener_contactos():
    minumero = request.args.get('minumero')
    cuenta = obtener_cuenta(minumero)
    
    if cuenta:
        contactos_info = {numero: obtener_cuenta(numero).nombre for numero in cuenta.contactos}
        return jsonify(contactos_info)
    else:
        return jsonify({"error": "Cuenta no encontrada"}), 404

@app.route('/billetera/pagar', methods=['GET'])
def realizar_pago():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))

    cuenta_origen = obtener_cuenta(minumero)
    cuenta_destino = obtener_cuenta(numerodestino)

    if cuenta_origen and cuenta_destino:
        if cuenta_origen.saldo >= valor:
            # Realizar la transacción
            cuenta_origen.saldo -= valor
            cuenta_destino.saldo += valor

            # Registrar la operación
            fecha = datetime.now().strftime("%d/%m/%Y")
            operacion = f"Pago realizado de {valor} a {cuenta_destino.nombre} el {fecha}"
            cuenta_origen.operaciones.append(operacion)

            operacion = f"Pago recibido de {valor} de {cuenta_origen.nombre} el {fecha}"
            cuenta_destino.operaciones.append(operacion)

            return jsonify({"mensaje": f"Transaccion exitosa. Realizado en {fecha}"})
        else:
            return jsonify({"error": "Saldo insuficiente"}), 400
    else:
        return jsonify({"error": "Cuenta no encontrada"}), 404

@app.route('/billetera/historial', methods=['GET'])
def obtener_historial():
    minumero = request.args.get('minumero')
    cuenta = obtener_cuenta(minumero)
    if cuenta:
        saldo = f"Saldo de {cuenta.nombre}: {cuenta.saldo}"
        operaciones = " <br>".join([f"--> {op}" for op in cuenta.operaciones])
        historial = f"{saldo} <br>Operaciones de {cuenta.nombre} <br>{operaciones}"

        return historial
    else:
        return jsonify({"error": "Cuenta no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)

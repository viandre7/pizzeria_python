from app import app
from modelo.cliente import *
from datetime import datetime
from flask import Flask, request, render_template, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

@app.route("/buscarClientePorCorreo",methods=['POST','GET'])
def buscarClientePorCorreo():
    datos=None
    estado=False
    correo = request.form['txtCorreo']
    try:
        cliente = Cliente.query.filter(Cliente.cliCorreo==correo).first()
        if(cliente!=None):
            datos=(cliente.idCliente, cliente.cliNombre, cliente.cliCorreo,cliente.cliTelefono)
            estado=True
            mensaje="Datos del Cliente"
        else:
            mensaje="No existe cliente con ese correo"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})

@app.route('/agregarCliente', methods=['POTS'])
def agregarCliente():
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    telefono = request.form['txtTelefono']
    estado = False
    datos = None
    if(nombre and correo and telefono):
        try:
            cliente = Cliente(cliNombre=nombre, cliCorreo=correo, cliTelefono=telefono)
            db.session.add(cliente)
            db.session.commit()
            datos= cliente.idCliente
            estado=True
            mensaje= 'Cliente agregado exitosamente'
        except exc.SQLAlchemyError as ex:
            mensaje = str(ex)
    else:
        mensaje= 'Faltan datos'
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})

# @app.route("/buscarClientePorCorreo",methods=['POST','GET'])
# def buscarClientePorCorreo():
#     datos=None
#     estado=False
#     correo = request.form['txtCorreo']
#     try:
#         cliente = Cliente.query.filter(Cliente.cliCorreo==correo).first()
#         if(cliente!=None):
#             datos=(cliente.idCliente, cliente.cliNombre, cliente.cliCorreo,cliente.cliTelefono)
#             estado=True
#             mensaje="Datos del Cliente"
#         else:
#             mensaje="No existe cliente con ese correo"
#     except exc.SQLAlchemyError as ex:
#         mensaje = str(ex)
#     return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


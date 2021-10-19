from sqlalchemy.orm.session import Session
from app import app
from modelo.pedido import *
from modelo.cliente import *
from modelo.pizza import *
from datetime import datetime
from flask import Flask, request, render_template, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc,func

@app.route('/registrarPedido', methods=['POST','GET'])
def registrarPedido():
    datos=None
    estado = False
    idCliente = request.form['idCliente']
    idPizza = request.form['idPizza']
    direccion = request.form['txtDireccion']
    cantidad = int(request.form['txtCantidad'])

    if(idCliente and idPizza and direccion and cantidad):
        try:
            pedido = Pedido()
            pedido.pedPizza=idPizza
            pedido.pedCliente=idCliente
            pedido.pedCantidad=cantidad
            pedido.pedDireccion=direccion
            pedido.pedFechaHora= datetime.now()
            db.session.add(pedido)
            db.session.commit()
            datos=pedido.idPedido
            estado=True
            mensaje = 'Pedido Agregado Correctamente'
        except exc.SQLAlchemyError as ex:
            db.session.rollback()
            mensaje = str(ex)
    else:
        mensaje='Faltan datos'
    return jsonify({'estado':estado, 'datos':datos, 'mensaje':mensaje})


# Listar Pedidos
@app.route('/listarPedidos', methods=['POST'])
def listarPedidos():
    estado = False
    datos = None
    try:
        pedidos = Pedido.query.all()
        if(pedidos !=None):
            lista=[]
            for p in pedidos:
                fechaPedido = p.pedFechaHora
                nuevaFechaPedido = fechaPedido.strftime("%Y-%m-%d") 
                pedido=(p.idPedido, p.pedCantidad, nuevaFechaPedido, p.cliente.cliNombre, p.pizza.pizNombre, p.pedEstado)
                lista.append(pedido)
            datos=lista
            print(lista)
            estado=True
            mensaje='Lista de pedidos'
        else:
            mensaje='No hay pedidos en el momento'
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


# Actualizar Pedidos
@app.route('/actualizarPedidos', methods=['POST'])
def actualizarPedidos():
    estado=False
    datos=None
    idPedido = request.form['actualizaPed']
    print(idPedido)
    if(idPedido):
        try:
            pedido = Pedido.query.get(idPedido)
            pedido.pedEstado='Atendido'
            db.session.add(pedido)
            db.session.commit()
            estado=True
            mensaje='Se ha actualizado el pedido'
        except exc.SQLAlchemyError as ex:
            db.session.rollback()
            mensaje = str(ex)
    else:
        mensaje='Faltan Datos'
    return jsonify({'estado':estado, 'datos':datos, 'mensaje':mensaje})


@app.route('/crearPedido', methods=['GET'])
def crearPedido():
    idPizza = request.args.get("idPizza")
    nombrePizza = request.args.get("nombrePizza")
    if(idPizza and nombrePizza):    
        datos= (idPizza, nombrePizza)
        return render_template("frmPedido.html",datos=datos)


@app.route('/gestionarPedidos')
def gestionarPedidos():
    if('user' in session):
        return render_template('user/gestionarPedidos.html')
    else:
        mensaje='Debe primero iniciar sesion'
        return render_template('frmIniciarSesion.html', mensaje=mensaje)
    

@app.route('/reportesGraficos')
def reportesGraficos():
    return render_template('user/generarGrafica.html')

@app.route('/datosGrafica1', methods=['POST'])
def datosGrafica1():
    try:
        datos=None
        estado=False
        pizzas= Pedido.query(Pizza.pizNombre, func.sum(Pedido.pedCantidad).label('pedCantidad')).\
        group_by(Pizza.idPizza).all()
        lista=[]
        estado=True
        for p in pizzas:
            print(p)
            pedido=(p.pizNombre, p.pizCantidad)
            lista.append(pedido)
            datos=pizzas
            mensaje='Lista de datos'  
        print(lista)  
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})

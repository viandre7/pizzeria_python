import os
from app import app
from modelo.pizza import *
from flask import Flask, request, render_template, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.utils import secure_filename

# Agregar Pizza
@app.route('/agregarPizza', methods=['POST'])
def agregar():
    estado = False
    datos = None
    try:
        nombre = request.form['txtNombre']
        ingredientes = request.form['txtIngredientes']
        valor = request.form['txtValor']
        if (nombre and ingredientes and valor):
            pizza = Pizza(pizNombre=nombre, pizIngredientes= ingredientes, pizValor=valor)
            db.session.add(pizza)
            db.session.commit()
            # Subir la foto de la pizza
            f = request.files['fileFoto']
            filename = secure_filename(f.filename)
            extension = filename.rsplit('.',1)[1].lower()
            nuevoNombre = str(pizza.idPizza) + '.' + extension
            #Guardamos el archivo en el directorio 'Archivos jpg'
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],nuevoNombre))
            datos = pizza.idPizza
            estado=True
            mensaje = "Pizza agregada con éxito"
        else:
            mensaje = "Faltan datos"
    except exc.SQLAlchemyError as ex:
        db.session.rollback()
        mensaje = str(ex)
    return jsonify({'estado':estado, 'datos':datos, 'mensaje':mensaje})

# Listar Pizzas
@app.route('/listarPizzas', methods=['POST'])
def listar():
    estado = False
    datos = None
    mensaje = ""
    try:
        pizzas = Pizza.query.all()
        listaPizzas=[]
        for p in pizzas:
            tuplaPizza = (p.idPizza, p.pizNombre,p.pizIngredientes,p.pizValor)
            listaPizzas.append(tuplaPizza)
            estado=True
            datos=listaPizzas
            mensaje='Listado de pizzas'
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})

@app.route('/gestionarPizzas')
def gestionarPizzas():
    if("user" in session):
        return render_template('user/frmGestionarPizza.html')
    else:
        mensaje = 'Debe primero iniciar sesion'
        return render_template('frmIniciarSesion.html', mensaje = mensaje)
        

@app.route('/pizzasPedido')
def listadoPizzas():
    return render_template('listadoPizzas.html')

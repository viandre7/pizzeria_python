import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Crear un objeto de tipo Flask
app = Flask(__name__)

app.secret_key = os.urandom(32) #Es necesario para poder crear variables de sesion

#Cadena de conexcion a la BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/pizzeria'
db = SQLAlchemy(app)

#configurar la carpeta donde se van a subir las fotos de las pizzas
app.config['UPLOAD_FOLDER']= './static/fotos'

#Lllamado a los controladores
from controlador.inicioController import *
from controlador.pizzaController import *
from controlador.pedidoController import *
from controlador.clienteController import *
from controlador.usuarioController import *

# Iniciar la aplicacion
if __name__ == "__main__":
    app.run(port=3000, debug=True) 
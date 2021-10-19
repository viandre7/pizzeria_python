from app import app
from flask import Flask, render_template, session

@app.route('/')
def inicio():
    return render_template('contenido.html')


@app.route('/quienesSomos')
def quienesSomos():
    return render_template('quienesSomos.html')

@app.route('/mostrarIniciarSesion')
def mostrarIniciarSesion():
    return render_template('frmIniciarSesion.html')
    
@app.route('/inicioUsuario')
def inicioUsuario():
    return render_template('user/contenido.html')


@app.route('/salir')
def salir():
    session.clear()
    mensaje='Ha cerrado la sesion'
    return render_template('frmIniciarSesion.html', mensaje=mensaje)
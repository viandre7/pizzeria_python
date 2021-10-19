from enum import unique
from app import db

class Pizza(db.Model):
    __tablename__ = 'pizzas' #Nombre de la tabla
    idPizza = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pizNombre = db.Column(db.String(100),unique=True, nullable=False)
    pizIngredientes = db.Column(db.String(1000), nullable=False)
    pizValor = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'{self.pizNombre}, {self.pizValor}'

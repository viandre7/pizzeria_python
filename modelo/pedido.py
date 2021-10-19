from datetime import datetime
from app import db

class Pedido(db.Model):
    __tablename__ = 'pedidos' #Nombre de la tabla
    idPedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pedCliente = db.Column(db.Integer, db.ForeignKey('clientes.idCliente'), nullable=False)
    pedPizza = db.Column(db.Integer, db.ForeignKey('pizzas.idPizza'), nullable=False)
    pedCantidad = db.Column(db.Integer, nullable=False)
    pedFechaHora = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    pedDireccion = db.Column(db.String(200), nullable=False)
    pedEstado = db.Column(db.String(20), default="Por Atender", nullable=False)
    # Necesarios para la relaicion
    pizza = db.relationship("Pizza",backref=db.backref('pizzas',lazy=True))
    cliente = db.relationship("Cliente",backref=db.backref('clientes',lazy=True))
 
    def __repr__(self):
        return f'''({self.pizza.pizNombre}, {self.cliente.cliNombre}, 
        {self.pedFechaHora}, {self.pedCantidad}, {self.pizza.pizValor})'''
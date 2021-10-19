from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes' #Nombre de la tabla
    idCliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliNombre = db.Column(db.String(50), nullable=False)
    cliCorreo = db.Column(db.String(50), unique=True, nullable=False)
    cliTelefono = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f'({self.idCliente},{self.cliNombre},{self.cliCorreo},{self.cliTelefono})'


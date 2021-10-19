from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios' #Nombre de la tabla
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuLogin = db.Column(db.String(45), unique=True, nullable=True)
    usuPassword = db.Column(db.String(60), unique=True, nullable=True)

    def __repr__(self):
        return f'{self.usuLogin}'


from app import db

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(8), index=True, unique=True)
    serialnum = db.Column(db.String(64), index=True, unique=True)
    customer = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return f'<Machine {self.serialnum}'
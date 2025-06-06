from __init__ import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=True)  # Entrada/salida
    uid = db.Column(db.Integer, unique=True, nullable=False)  # Único para evitar duplicados

    def __repr__(self):
        return f"<Attendance user_id={self.user_id} timestamp={self.timestamp} status={self.status} uid={self.uid}>"



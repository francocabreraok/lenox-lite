from __init__ import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=True)  # Entrada/Salida (0/1)
    uid = db.Column(db.Integer, nullable=True)     # ID único del evento (si está disponible)

    def __repr__(self):
        return f"<Attendance user_id={self.user_id} timestamp={self.timestamp} status={self.status} uid={self.uid}>"


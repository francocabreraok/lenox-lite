import sys
import os
from datetime import datetime

# Asegurar que el path apunte a /app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from zk import ZK, const
import __init__ as app_module
from models.attendance import Attendance

create_app = app_module.create_app
db = app_module.db

def fetch_attendance():
    zk = ZK('192.168.1.29', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=True)
    try:
        conn = zk.connect()
        conn.disable_device()
        attendances = conn.get_attendance()

        app = create_app()
        with app.app_context():
            nuevos = 0
            for att in attendances:
                # Evitar duplicados por uid
                if Attendance.query.filter_by(uid=att.uid).first():
                    continue

                record = Attendance(
                    user_id=att.user_id,
                    timestamp=att.timestamp,
                    status=att.status,
                    uid=att.uid
                )
                db.session.add(record)
                nuevos += 1

            db.session.commit()
            print(f"Asistencias importadas correctamente. Nuevas entradas: {nuevos}")

        conn.enable_device()
        conn.disconnect()

    except Exception as e:
        print("Error al conectar con ZK MB20:", e)

if __name__ == "__main__":
    fetch_attendance()

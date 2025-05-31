import os

class Config:
    SECRET_KEY = 'changeme-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin:admin123@db/asistencia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ZK MB20 settings
    ZK_DEVICE_IP = '192.168.1.71'
    ZK_DEVICE_PORT = 4370

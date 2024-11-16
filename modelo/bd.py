import psycopg2
from dotenv import load_dotenv
import os
from pass_bd import contra

class DataBaseMeta(type): #singleton

    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instances = instance
        return cls.__instances


class Database(metaclass=DataBaseMeta):
    
    def __init__(self):
        try:
            load_dotenv('.env')
            #self.conexion = psycopg2.connect(host='localhost', port=5434, database='8_escalones', user='postgres', password='pokemon')
            # Por ahora modificar los parameteros de acceso a la base de datos aqui:
            self.conexion = psycopg2.connect(
                host='localhost', 
                port=5432, 
                database='8_escalones', 
                user='postgres', 
                password=contra)
            print('Conexion exitosa')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def cursor(self):
        return self.conexion.cursor()

    


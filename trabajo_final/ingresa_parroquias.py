from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Parroquia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivos
#provincias = session.query(Provincia).all()
cantones = session.query(Canton).all()

with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    aux=[]
    aux2=[]
    
    id_p=0
    id_c=0
    for row in reader:
        aux=row
        for c in cantones:
            if aux[6]== c.nombre:
                id_c = c.id
        c = Parroquia(nombre=aux[6], cod_division_politica=aux[5],codigo_distrito=aux[7], canton=c,canton_id=id_c)
        session.add(c)

# confirmacion de transacciones
session.commit()
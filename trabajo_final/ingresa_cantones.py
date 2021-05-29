from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton

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
provincias = session.query(Provincia).all()

with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    next(reader)
    nomAux=""     
    id_p=0
    aux=[]
    for row in reader:
        if row[5] not in aux:
            aux.append(row[5])
            for p in provincias:
                if row[3] == p.nombre:
                    id_p = p.id
                    c = Canton(nombre=row[5], cod_division_politica=row[4], provincia= p, provincia_id=id_p)
                    session.add(c)
#confirmacion de transacciones
session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

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
 
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)
    aux=[]
    for row in reader:
        if row[3] not in aux:
            aux.append(row[3])
            p = Provincia(nombre=row[3], cod_division_politica=row[2])
            session.add(p)
# confirmacion de transacciones
session.commit()

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
    # Omitir la primera fila del csv 
    next(reader)
    # Lista vacia, donde guardaremos las provinciass que van pasando
    aux=[]

    # Recorrido del archivo csv, para extraer la información y llenar las tablas
    for row in reader:
        if row[3] not in aux:
            aux.append(row[3])# agrega las provincias
            p = Provincia(nombre=row[3], cod_division_politica=row[2]) # Creación del objeto de tipo Provincia
            session.add(p)  #Agregar el objeto Canton a la sesion
# confirmacion de transacciones
session.commit()

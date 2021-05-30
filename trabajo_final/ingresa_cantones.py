from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas
from genera_tablas import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivo
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    # Omitir la primera fila del csv
    next(reader)

    # Lista vacia, donde guardaremos los cantones que van pasando
    aux=[]

    # Recorrido del archivo csv, para extraer la información y llenar las tablas
    for row in reader:
        # COndicional que evalua si el canton ya existe en la lista que guarda a los cantones
        if row[5] not in aux:
            aux.append(row[5]) # agrega los cantones  la lista aux

            #Variable que guarda, la provincia que devuellve la consulta, para posteriormente
            # Obtener el id y asignarle a cantón.
            id_p= session.query(Provincia).filter_by(nombre = row[3]).first()  

            # Creación del objeto de tipo Canton
            c = Canton(nombre=row[5], cod_division_politica=row[4], provincia_id=id_p.id)

            #Agregar el objeto Canton a la sesion
            session.add(c)
#confirmacion de transacciones
session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import  Canton, Parroquia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivo
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    # Omitir la primera filadel csv
    next(reader)

    # Lista vacia, donde guardaremos las parroquias que van pasando
    aux=[]    

    # Recorrido del archivo csv, para extraer la información y llenar las tablas
    for row in reader:
          # COndicional que evalua si el canton ya existe en la lista que guarda a las parroquias     
        if row[7] not in aux:
            aux.append(row[7]) # agrega a la lista a las parroquias
            #Variable que guarda, EL canton que devuellve la consulta, para posteriormente
            # Obtener el id y asignarle a Parroquia.
            id_c= session.query(Canton).filter_by(nombre = row[5]).first()

            # Creación del objeto de tipo Parroquia
            p = Parroquia(nombre=row[7], cod_division_politica=row[6], codigo_distrito=row[8],canton_id=id_c.id)
           
            #Agregar el objeto Parroquia a la sesion
            session.add(p)

#confirmacion de transacciones            
session.commit()


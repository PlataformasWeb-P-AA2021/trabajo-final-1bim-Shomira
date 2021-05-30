
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import  Parroquia, Establecimiento
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
parroquias = session.query(Parroquia).all()
#Lectura del archivos
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    
    next(reader) # Omitir la primera fila del csv
    # Recorrido del archivo csv, para extraer la información y llenar las tablas

    for row in reader:
        # Transformar los tipos de datos String a int del csv para guardar en als tablas
        num_Es=int(row[14], base=0)
        num_Do=int(row[15], base=0)

        # Consulta que se realiza par obtener el id de la parroquia
        # a ala que pertenece el establecimiento
        id_p= session.query(Parroquia).filter_by(nombre = row[7]).first() 
        # Creación del objeto establecimiento
        e = Establecimiento(codigo_AMIE=row[0], nombre=row[1], sostenimiento=row[9],tipo_educacion=row[10],
        modalidad=row[11], jornada=row[12], acceso=row[13],num_estudiantes=num_Es,num_docentes=num_Do, parroquia_id=id_p.id)
        
        session.add(e)#Agregar el objeto Establecimiento a la sesion
#confirmacion de transacciones   
session.commit()



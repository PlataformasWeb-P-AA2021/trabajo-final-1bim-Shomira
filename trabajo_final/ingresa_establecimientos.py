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
cantones = session.query(Canton).all()
#Lectura del archivos
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    
    next(reader)
    aux=[]    
    id_p=0
    for row in reader:
        for c in cantones:      
            if row[5] == c.nombre:
                id_p = c.id
            if row[7] not in aux:
                aux.append(row[7])
                p = Parroquia(nombre=row[7], cod_division_politica=row[6], codigo_distrito=row[8],canton=c,canton_id=id_p)
                session.add(p)
session.commit()


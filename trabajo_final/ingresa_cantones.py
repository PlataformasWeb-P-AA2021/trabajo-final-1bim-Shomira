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
print(provincias[1])
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    aux=[]
    for row in reader:
        #print(row)
        aux=row
        id_p=0
        for p in provincias:
            if aux[5] == p.nombre:
                id_p = p.id
            p=p
        c = Canton(nombre=aux[5], cod_division_politica=aux[4],codigo_distrito=aux[8], provincia= p, provincia_id=id_p)
        session.add(c)

# confirmacion de transacciones
session.commit()

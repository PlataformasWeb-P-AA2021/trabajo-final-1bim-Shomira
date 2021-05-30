from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import colorama
from sqlalchemy import and_, or_
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta 1
# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
print("\033[0;m"+"Establecimientos de la provincia de Loja"+'\033[0;m') 

parroquia_Jn = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == 'Nocturna').all()
for p in parroquia_Jn:
    print(p)
    print("---------------------------------------------------------------------------------------------")
print(len(parroquia_Jn))

#  Consulta 2
# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
print("\033[0;m"+"Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459"+'\033[0;m') 

establecimientos_Ne = session.query(Canton).join(Parroquia,Establecimiento)\
    .filter(or_(Establecimiento.num_estudiantes == 448, Establecimiento.num_estudiantes == 450,
    Establecimiento.num_estudiantes == 451, Establecimiento.num_estudiantes == 454,
    Establecimiento.num_estudiantes == 458, Establecimiento.num_estudiantes == 459 )).all()

for e in establecimientos_Ne:
    print(e)
    print("---------------------------------------------------------------------------------------------")
print(len(establecimientos_Ne))

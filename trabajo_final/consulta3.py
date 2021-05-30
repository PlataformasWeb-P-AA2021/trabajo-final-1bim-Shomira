from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and y or
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
# Los cantones que tiene establecimientos con 0 número de profesores
print("\033[0;m"+"Los cantones que tiene establecimientos con 0 número de profesores"+'\033[0;m') 

est_Dc = session.query(Establecimiento).filter(Establecimiento.num_docentes == 0).all()
for dc in est_Dc:
    print(dc)
    print("---------------------------------------------------------------------------------------------")
print(len(est_Dc))

# Consulta 2
# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
print("\033[0;m"+"Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21"+'\033[0;m') 

pa_Cat = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.num_estudiantes >= 21,
        Parroquia.nombre == "CATACOCHA")).all()

for pa in pa_Cat:
    print(pa)
    print("---------------------------------------------------------------------------------------------")
print(len(pa_Cat))

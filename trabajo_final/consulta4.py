from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and y or
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
# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
print("\033[0;m"+"Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores."+'\033[0;m') 

est_Nd_Oe = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_estudiantes).all()
for nd_Oe in est_Nd_Oe:
    print(nd_Oe)
    print("---------------------------------------------------------------------------------------------")
print(len(est_Nd_Oe))

# Consulta 1
# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
print("\033[0;m"+"Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores."+'\033[0;m') 

est_Nd_Od = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_docentes).all()
for nd_Od in est_Nd_Od:
    print(nd_Od)
    print("---------------------------------------------------------------------------------------------")
print(len(est_Nd_Oe))
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
# Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
print("\033[0;m"+"Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena 'Permanente' en tipo de educación."+'\033[0;m') 

est_Op_Te = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.num_docentes > 20,
                    Establecimiento.tipo_educacion.like("%Permanente%"))).order_by(Parroquia.nombre).all()
for op_te in est_Op_Te:
    print(op_te)
    print("---------------------------------------------------------------------------------------------")
print(len(est_Op_Te))


# Consulta 1
# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02
print("\033[0;m"+"Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02"+'\033[0;m') 

est_Op_Te = session.query(Establecimiento).join(Parroquia).filter(Parroquia.codigo_distrito == '11D02').order_by(Establecimiento.sostenimiento).all()
for op_te in est_Op_Te:
    print(op_te)
    print("---------------------------------------------------------------------------------------------")
print(len(est_Op_Te))

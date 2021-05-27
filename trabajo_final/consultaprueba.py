from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimientos

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
canton = session.query(Canton).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Clubs")
for s in canton:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de 
# la entidad Jugador
establecimiento = session.query(Establecimiento).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python

print("Jugadores")
for s in establecimiento:
    print("%s" % (s))
    print("---------")




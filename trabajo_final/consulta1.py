from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa las clases de archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


print('Consulta 1')
# Todos los establecimientos de la provincia de Loja.
print("\033[1;33m"+"Establecimientos de la provincia de Loja"+'\033[0;m') 
div="\033[1;33m"+"-------------------------------------------------------------------------"+'\033[0;m'

# Consulta que devuelve  los establecimientos de la provincia de Loja.
establecimientos_L = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Provincia.nombre == 'LOJA').all()
for e in establecimientos_L:
    print(e)
    print(div)
print(len(establecimientos_L))

print('Consulta 2')
# Todos los establecimientos del Canton de Loja.
print("\033[;36m"+"Establecimientos del Cantón Loja "+'\033[;36m') 
# Separador
div="\033[;36m"+"-------------------------------------------------------------------------"+'\033[;36m'
establecimientos_Cl = session.query(Establecimiento).join(Parroquia, Canton).filter(Canton.nombre == 'LOJA').all()
for e in establecimientos_Cl:
    print(e)
    print(div)
print(len(establecimientos_Cl))
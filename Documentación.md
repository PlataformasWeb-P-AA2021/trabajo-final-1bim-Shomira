<!--
***
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02">
    <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo">
  </a>

  <h3 align="center">Ejemplo de uso de SqlAlchemy</h3>

  <p align="center">
Es un repositorio se permite ejemplificar el proceso de creación y relación de entidades, ingreso y consulta de información a través de la SqlAlchemy. 
 <a href="https://www.sqlalchemy.org/">SqlAlchemy</a>
    <br />
  </p>
</p>



<!-- Contenidos -->
<details open="open">
  <summary><h2 style="display: inline-block">Índice</h2></summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
     </li>
    <li>
      <a href="#Inicio-del-proyecto">Inicio del proyecto</a>
      <ul>
        <li><a href="#prerrequisitos">Prerrequisitos</a></li>
       </ul>
    </li>
     <li>
      <a href="#sobre-el-proyecto">Usos</a>
    </li>
    <li>
      <a href="#sobre-el-proyecto">Licencia</a>
    </li>
    <li>
      <a href="#sobre-el-proyecto">Contacto</a>
    </li>
  </ol>
</details>



<!-- SOBRE EL PROYECTO -->
## Sobre el proyecto

El siguiente trabajo ejemplifica, ingreso y consulta de información a través de la SqlAlchemy.

En la carpeta llamada data, se encuentra el archivo Listado-Instituciones-Educativas.csv el cual
usaremos para extraer los datos y dividir en enttidades que posteriormente de las relacionara.

Descripción de datos:

Las entidades son:
* Provincias.


```python
# Creación de la tabla Provincia una provincia tiene muchos cantones

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),unique=True)#Código División Política Administrativa Provincia
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: %s | Código de División Política: %s \n "% (
                          self.nombre,
                          self.cod_division_politica)

```  
* Canton  
Un cantón pertence a un provincia.  

```python
# Creación de la tabla Canton, un canton tiene muchas parroquias
#Un cantón pertenece a una provincia
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    def __repr__(self):
        return "Canton: %s |  Código de División Política: %s | Id de provincia: %d\n"% (
                          self.nombre, 
                          self.provincia,
                          self.provincia_id)
```
* Parroquia  
Una parroquia pertence a un cantón.
```python
# Creación de la tabla parroquia, una parroquia tiene varios establecimientos
# una parroquia pertenece a un cantón
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100),unique=True)
    codigo_distrito = Column(String(50),nullable=False) #Código de Distrito
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Parroquia
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos= relationship("Establecimiento", back_populates="parroquias")
    def __repr__(self):
        return "Parroquia: %s |  Código de División Política: %s |  Código de Distrito: %s | Id Canton: %d\n"% (
                          self.nombre, 
                          self.cod_division_politica,
                          self.codigo_distrito,
                          self.canton_id)
```  
* Establecimiento  
Un establecimiento tiene características propias.
```python
# Creación de la tabla Establecimiento con sus atributos.
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo_AMIE = Column(String, primary_key=True)  
    nombre = Column(String(100), nullable=False) 
    sostenimiento = Column(String(50), nullable=False) 
    tipo_educacion = Column(String(100), nullable=False) 
    modalidad = Column(String(500), nullable=False) 
    jornada = Column(String(100), nullable=False) 
    acceso = Column(String(100), nullable=False) 
    num_estudiantes = Column(Integer) 
    num_docentes = Column(Integer) 
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquias = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: %s | Codigo Institución: %s | Sostenimiento: %s | Tipo Educación: %s| Modalidad: %s | Jornada: %s | Acceso: %s |  Numero Estudiante: %d | Numero Docentes: %d | Id Parroquia: %d" % (
                self.nombre,
                self.codigo_AMIE,
                self.sostenimiento,
                self.tipo_educacion,
                self.modalidad,
                self.jornada,
                self.acceso,
                self.num_estudiantes,
                self.num_docentes,
                self.parroquia_id)
```
Relaciones entre entidades:
- Una provincia tiene muchos cantones.  
- Un cantón tiene muchas parroquias y pertenece a una unica provincia.  
- Una parroquia tiene Establecimientos y pertenece a un unico cantón.

<!-- GETTING STARTED -->
## Inicio del proyecto

Para poder usar el presente proyecto, tomar en consideración lo siguiente:

### Prerrequisitos

* Instalar [Python](https://www.python.org/) 
* Instalar [SQLAlchemy](https://www.sqlalchemy.org/) 
``` python
  	pip install SQLAlchemy
```

<!-- USAGE EXAMPLES -->
## Usos

La carpeta trabajo_final tiene los siguiente archivos
* configuracion.py

```python
# este módulo será usado para posibles configuraciones
#
# cadena conector a la base de datos
#
# Sqlite
cadena_base_datos = 'sqlite:///baseEstablecimientos.db'  
```
* genera_tablas.py
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()


# Creación de la tabla Provincia una provincia tiene muchos cantones

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),unique=True)#Código División Política Administrativa Provincia
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: %s | Código de División Política: %s \n "% (
                          self.nombre,
                          self.cod_division_politica)
# Creación de la tabla Canton, un canton tiene muchas parroquias
 #Un cantón pertenece a una provincia
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    def __repr__(self):
        return "Canton: %s |  Código de División Política: %s | Id de provincia: %d\n"% (
                          self.nombre, 
                          self.provincia,
                          self.provincia_id)
# Creación de la tabla parroquia, una parroquia tiene varios establecimientos
# una parroquia pertenece a un cantón
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100),unique=True)
    codigo_distrito = Column(String(50),nullable=False) #Código de Distrito
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Parroquia
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos= relationship("Establecimiento", back_populates="parroquias")
    def __repr__(self):
        return "Parroquia: %s |  Código de División Política: %s |  Código de Distrito: %s | Id Canton: %d\n"% (
                          self.nombre, 
                          self.cod_division_politica,
                          self.codigo_distrito,
                          self.canton_id)

# Creación de la tabla Establecimiento con sus atributos.
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo_AMIE = Column(String, primary_key=True)  
    nombre = Column(String(100), nullable=False) 
    sostenimiento = Column(String(50), nullable=False) 
    tipo_educacion = Column(String(100), nullable=False) 
    modalidad = Column(String(500), nullable=False) 
    jornada = Column(String(100), nullable=False) 
    acceso = Column(String(100), nullable=False) 
    num_estudiantes = Column(Integer) 
    num_docentes = Column(Integer) 
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquias = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: %s | Codigo Institución: %s | Sostenimiento: %s | Tipo Educación: %s| Modalidad: %s | Jornada: %s | Acceso: %s |  Numero Estudiante: %d | Numero Docentes: %d | Id Parroquia: %d" % (
                self.nombre,
                self.codigo_AMIE,
                self.sostenimiento,
                self.tipo_educacion,
                self.modalidad,
                self.jornada,
                self.acceso,
                self.num_estudiantes,
                self.num_docentes,
                self.parroquia_id)

Base.metadata.create_all(engine)

```
* ingreso_provincias.py
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

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
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    # Omitir la primera fila del csv 
    next(reader)
    # Lista vacia, donde guardaremos las provinciass que van pasando
    aux=[]

    # Recorrido del archivo csv, para extraer la información y llenar las tablas
    for row in reader:
        if row[3] not in aux:
            aux.append(row[3])# agrega las provincias
            p = Provincia(nombre=row[3], cod_division_politica=row[2]) # Creación del objeto de tipo Provincia
            session.add(p)  #Agregar el objeto Canton a la sesion
# confirmacion de transacciones
session.commit()

```  
* ingreso_cantones.py
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas
from genera_tablas import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivo
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    # Omitir la primera fila del csv
    next(reader)

    # Lista vacia, donde guardaremos los cantones que van pasando
    aux=[]

    # Recorrido del archivo csv, para extraer la información y llenar las tablas
    for row in reader:
        # COndicional que evalua si el canton ya existe en la lista que guarda a los cantones
        if row[5] not in aux:
            aux.append(row[5]) # agrega los cantones  la lista aux

            #Variable que guarda, la provincia que devuellve la consulta, para posteriormente
            # Obtener el id y asignarle a cantón.
            id_p= session.query(Provincia).filter_by(nombre = row[3]).first()  

            # Creación del objeto de tipo Canton
            c = Canton(nombre=row[5], cod_division_politica=row[4], provincia_id=id_p.id)

            #Agregar el objeto Canton a la sesion
            session.add(c)
#confirmacion de transacciones
session.commit()

```  
* ingreso_parroquias.py
```python
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

```  
* ingreso_establecimientos.py
```python

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
```  

### Archivos de consultas a las tablas    

* consulta1.py
```python
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


# Consulta que devuelve  los establecimientos de la provincia de Loja.
establecimientos_L = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Provincia.nombre == 'LOJA').all()
for e in establecimientos_L:
    print(e)
    #Divisor
    print("\033[1;33m"+"-------------------------------------------------------------------------"+'\033[0;m')
print(len(establecimientos_L))

print('Consulta 2')
# Todos los establecimientos del Canton de Loja.
print("\033[;36m"+"Establecimientos del Cantón Loja "+'\033[;36m') 


establecimientos_Cl = session.query(Establecimiento).join(Parroquia, Canton).filter(Canton.nombre == 'LOJA').all()
for e in establecimientos_Cl:
    print(e)
    #Separador
    print("\033[;36m"+"-------------------------------------------------------------------------"+'\033[;36m')
#Imprime el numero de registros
print(len(establecimientos_Cl))
```
* consulta2.py
```python
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
# Uso de un Join para acceder al canton
establecimientos_Ne = session.query(Canton).join(Parroquia,Establecimiento)\
    .filter(or_(Establecimiento.num_estudiantes == 448, Establecimiento.num_estudiantes == 450,
    Establecimiento.num_estudiantes == 451, Establecimiento.num_estudiantes == 454,
    Establecimiento.num_estudiantes == 458, Establecimiento.num_estudiantes == 459 )).all()

for e in establecimientos_Ne:
    print(e)
    print("---------------------------------------------------------------------------------------------")
print(len(establecimientos_Ne))

```
* consulta3.py
```python
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

```
* consulta4.py

```python
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
```

El orden de ejecución de los archivos es el siguiente:

1. Generación de las entidades:
``` sh
python genera_tablas.py
```
Este proceso debe generar un archivo llamado baseEstablecimientos.db que contienes la base de datos en Sqlite. 

2. Ingreso de información a las entidades:  
 **Se debe ejecutar en el orden especificado, caso contrario se podrian generar erorres y no se cargarian los datos a la base.**
``` sh
python ingresa_provincias.py  
python ingresa_cantones.py  
python ingresa_parroquias.py  
python ingresa_establecimientos.py
```
3. Ejecutar consultas:
``` sh
python consulta1.py
python consulta2.py
python consulta3.py
python consulta4.py
```

<!-- LICENSE -->
## Licencia

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contacto

Shomira Rosales Alberca - [@snrosales](@Snrosales)


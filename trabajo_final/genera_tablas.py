from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),unique=True)#Código División Política Administrativa Provincia
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: %s Código de División Política: %s \n "% (
                          self.nombre,
                          self.cod_division_politica)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")############################################
    def __repr__(self):
        return "Canton: %s Código de División Política: %s Id de provincia: %d\n"% (
                          self.nombre, 
                          self.provincia,
                          self.provincia_id)

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
        return "Parroquia: %s Código de División Política: %s Código de Distrito: %s Id Canton: %d\n"% (
                          self.nombre, 
                          self.cod_division_politica,
                          self.codigo_distrito,
                          self.canton_id)

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
        return "Establecimiento: %s Codigo Institución: %s Sostenimiento: %s Tipo Educación: %s Modalidad: %s Jornada: %s Acceso: %s Numero Estudiante: %d Numero Docentes: %d" % (
                self.nombre,
                self.codigo_AMIE,
                self.sostenimiento,
                self.tipo_educacion,
                self.modalidad,
                self.jornada,
                self.acceso,
                self.num_estudiantes,
                self.num_docentes)

Base.metadata.create_all(engine)

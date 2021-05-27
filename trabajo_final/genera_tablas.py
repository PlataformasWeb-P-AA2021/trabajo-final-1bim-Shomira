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
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    canton = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: nombre=%s\n "% (
                          self.nombre)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="canton")
    parroquia = relationship("Parroquia", back_populates="canton")############################################
    def __repr__(self):
        return "Canton: nombre=%s\n provincia=%s\n"% (
                          self.nombre, 
                          self.provincia)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo_distrito = Column(String(50),nullable=False) #Código de Distrito
    cod_division_politica = Column(String(50),nullable=False)#Código División Política Administrativa  Parroquia
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquia")
    def __repr__(self):
        return "Parroquia: nombre=%s\n canton=%s\n"% (
                          self.nombre, 
                          self.canton)
'''
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_AMIE = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False) 
    
    sostenimiento = Column(String(50), nullable=False) 
    tipo_educacion = Column(String(100), nullable=False) 
    modalidad = Column(String(500), nullable=False) 
    jornada = Column(String(100), nullable=False) 
    acceso = Column(String(100), nullable=False) 
    num_estudiantes = Column(Integer) 
    num_docentes = Column(Integer) 
    canton_id = Column(Integer, ForeignKey('canton.id'))
    parroquias = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: %s" % (
                self.nombre)
'''
Base.metadata.create_all(engine)

"""
Definición de modelos y configuración de la base de datos utilizando SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE  # Asegúrate de que esta ruta sea correcta

Base = declarative_base()

# pylint: disable=too-few-public-methods


class User(Base):
    __tablename__ = "user"
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    name = Column(String(80))
    lastname = Column(String(80))
    email = Column(String(255), unique=True)
    password = Column(String(50))
    profile_picture = Column(String(255), nullable=True)
    type_user = Column(String(80))


class Post(Base):
    __tablename__ = "post"
    id_post = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer)
    description = Column(String(255))
    image = Column(String(255), nullable=True)


# Configurar la URL de la base de datos
DATABASE_URL = (
    f"mysql+pymysql://{DATABASE['user']}:"
    f"{DATABASE['password']}@{DATABASE['host']}/"
    f"{DATABASE['name']}"
)

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión local de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

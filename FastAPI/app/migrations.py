from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.settings import DATABASE  # type: ignore

Base = declarative_base()


class User(Base):
    """ Model representing an user. """
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    name = Column(String(80))
    lastname = Column(String(80))
    email = Column(String(255))
    password = Column(String(50))
    profile_picture = Column(String(255))
    type_user = Column(String(80))


class Post(Base):
    """ Model representing a post. """
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(50))
    id_user = Column(Integer)


# Configurar la base de datos
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

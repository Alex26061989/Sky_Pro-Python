# config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = "postgres"
DB_PASSWORD = "08Aprel2018Lera+" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"  

# Строка подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Фабрика сессий
SessionLocal = sessionmaker(bind=engine)

# Базовый класс для моделей
Base = declarative_base()
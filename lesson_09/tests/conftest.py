# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from config import Base
from models import Subject, User, Student, Teacher

@pytest.fixture(scope="function")
def db_session():
    """
    Фикстура создает тестовую БД в памяти
    Каждый тест работает с чистой БД
    """
    # Создаем БД в памяти 
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    
    # Создаем сессию
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()
    
    # Добавляем базовые данные (предметы)
    subjects = [
        Subject(subject_id=1, name="English"),
        Subject(subject_id=2, name="Mathematics"),
        Subject(subject_id=3, name="Physics"),
    ]
    session.add_all(subjects)
    session.commit()
    
    yield session  
    
    # Закрываем сессию после теста
    session.close()
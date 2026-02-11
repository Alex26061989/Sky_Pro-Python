# test_crud.py
import pytest
from sqlalchemy.exc import IntegrityError
from models import Subject, User, Student, Teacher

# ============= ТЕСТ 1: ДОБАВЛЕНИЕ =============
def test_create_subject(db_session):
    """Тест на добавление нового предмета"""
    
    # Создаём новый предмет
    new_subject = Subject(
        subject_id=16,  # Новый ID (максимум 15 в наших данных)
        name="Programming"
    )
    
    # Добавляем в БД
    db_session.add(new_subject)
    db_session.commit()
    
    # Проверяем, что добавилось
    created_subject = db_session.query(Subject).filter_by(subject_id=16).first()
    
    assert created_subject is not None, "Предмет не был создан!"
    assert created_subject.name == "Programming", "Название предмета не совпадает!"
    assert created_subject.subject_id == 16, "ID предмета не совпадает!"

# ============= ТЕСТ 2: ИЗМЕНЕНИЕ =============
def test_update_subject_name(db_session):
    """Тест на изменение названия предмета"""
    
    # Берём существующий предмет (English)
    subject = db_session.query(Subject).filter_by(subject_id=1).first()
    assert subject is not None, "Предмет не найден!"
    assert subject.name == "English", "Исходное название не совпадает!"
    
    # Изменяем название
    subject.name = "English Language"
    db_session.commit()
    
    # Проверяем, что изменилось
    updated_subject = db_session.query(Subject).filter_by(subject_id=1).first()
    assert updated_subject.name == "English Language", "Название не обновилось!"

# ============= ТЕСТ 3: УДАЛЕНИЕ =============
def test_delete_subject(db_session):
    """Тест на удаление предмета"""
    
    # Проверяем, что предмет существует
    subject = db_session.query(Subject).filter_by(subject_id=3).first()
    assert subject is not None, "Предмет Physics не найден!"
    assert subject.name == "Physics", "Не тот предмет!"
    
    # Удаляем предмет
    db_session.delete(subject)
    db_session.commit()
    
    # Проверяем, что удалился
    deleted_subject = db_session.query(Subject).filter_by(subject_id=3).first()
    assert deleted_subject is None, "Предмет не был удален!"

# ============= ДОПОЛНИТЕЛЬНЫЙ ТЕСТ: СО СТУДЕНТОМ =============
def test_create_student_with_user(db_session):
    """Тест на добавление студента и пользователя"""
    
    # Создаём пользователя
    new_user = User(
        user_id=99999,
        user_email="test.student@example.com",
        subject_id=1  # English
    )
    db_session.add(new_user)
    db_session.flush()  # Чтобы получить ID
    
    # Создаём студента
    new_student = Student(
        user_id=new_user.user_id,
        level="Beginner",
        study_type="personal",
        subject_id=1
    )
    db_session.add(new_student)
    db_session.commit()
    
    # Проверяем
    created_student = db_session.query(Student).filter_by(user_id=99999).first()
    assert created_student is not None
    assert created_student.level == "Beginner"
    assert created_student.user.user_email == "test.student@example.com"
    
    # Удаляем (чистим за собой)
    db_session.delete(created_student)
    db_session.delete(new_user)
    db_session.commit()
    
    # Проверяем, что удалили
    assert db_session.query(Student).filter_by(user_id=99999).first() is None
    assert db_session.query(User).filter_by(user_id=99999).first() is None
# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Subject(Base):
    __tablename__ = "subjects"
    
    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    users = relationship("User", back_populates="subject")
    students = relationship("Student", back_populates="subject")
    teachers = relationship("Teacher", back_populates="subject")

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(100), nullable=False, unique=True)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"))
    
    subject = relationship("Subject", back_populates="users")
    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)

class Student(Base):
    __tablename__ = "students"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    level = Column(String(20), nullable=False)
    study_type = Column(String(10), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=False)
    
    user = relationship("User", back_populates="student")
    subject = relationship("Subject", back_populates="students")
    groups = relationship("GroupStudent", back_populates="student")

class Teacher(Base):
    __tablename__ = "teachers"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    email = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=False)
    
    user = relationship("User", back_populates="teacher")
    subject = relationship("Subject", back_populates="teachers")

class GroupStudent(Base):
    __tablename__ = "group_student"
    
    student_id = Column(Integer, ForeignKey("students.user_id"), primary_key=True)
    group_id = Column(Integer, primary_key=True)
        
    student = relationship("Student", back_populates="groups")
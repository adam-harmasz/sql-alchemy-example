from sqlalchemy import Table, Column, Integer, ForeignKey, Sequence, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
student_course = Table(
    "student_course",
    Base.metadata,
    Column("courses_id", Integer, ForeignKey("courses.id")),
    Column("students_id", Integer, ForeignKey("students.id")),
)


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(Integer)

    courses = relationship(
        "Courses", secondary=student_course, back_populates="students"
    )

    def __repr__(self):
        return f"Student(id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name})"


class Levels(Base):
    __tablename__ = "levels"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), nullable=False)

    courses = relationship("Courses", back_populates="level")

    def __repr__(self):
        return f"Level(id: {self.id}, name: {self.name})"


class Languages(Base):
    __tablename__ = "languages"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), nullable=False)

    courses = relationship("Courses", back_populates="language")

    def __repr__(self):
        return f"Language(id: {self.id}, name: {self.name})"


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), nullable=False)

    courses = relationship("Courses", back_populates="category")

    def __repr__(self):
        return f"Category(id: {self.id}, name: {self.name})"


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    nr_of_lessons = Column(Integer, nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)

    language = relationship("Languages", back_populates="courses")
    category = relationship("Categories", back_populates="courses")
    level = relationship("Levels", back_populates="courses")
    students = relationship(
        "Students", secondary=student_course, back_populates="courses"
    )

    language_id = Column(Integer, ForeignKey("languages.id", ondelete="CASCADE"))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"Course(id: {self.id}, level: {self.level}, lang: {self.language}, students: {self.students})"

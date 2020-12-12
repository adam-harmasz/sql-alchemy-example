from speak_and_fly.data import (
    LEVELS_DATA,
    LANG_DATA,
    CATEGORIES_DATA,
    STUDENT_DATA,
    COURSE_DATA,
)
from speak_and_fly.config import session
from speak_and_fly.models import Levels, Languages, Categories, Students, Courses


def get_level_objects():
    return [Levels(**level) for level in LEVELS_DATA]


def create_levels():
    session.add_all(get_level_objects())
    session.commit()


def get_lang_objects():
    return [Languages(**lang) for lang in LANG_DATA]


def create_langs():
    session.add_all(get_lang_objects())
    session.commit()


def get_categories_objects():
    return [Categories(**category) for category in CATEGORIES_DATA]


def create_categories():
    session.add_all(get_categories_objects())
    session.commit()


def get_student_objects():
    return [Students(**level) for level in STUDENT_DATA]


def create_students():
    session.add_all(get_student_objects())
    session.commit()


def get_course_objects():
    return [Courses(**level) for level in COURSE_DATA]


def create_courses():
    session.add_all(get_course_objects())
    session.commit()


def create_basic_data():
    create_levels()
    create_langs()
    create_categories()
    create_students()
    create_courses()


def assign_student_to_course(course, student):
    course.students.append(student)
    session.commit()


def assign_multiple_students_to_course(course, students):
    """
    course: Courses instance
    students: sequence e.g. list of Students instances
    """
    for student in students:
        course.students.append(student)
    session.commit()


def assign_course_to_student(student, course):
    student.courses.append(course)
    session.commit()


def assign_multiple_course_to_student(student, courses):
    """
    student: instance of Students class
    courses: sequence e.g. list of course instances
    """
    for course in courses:
        student.courses.append(course)
    session.commit()

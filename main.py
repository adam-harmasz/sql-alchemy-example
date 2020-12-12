from speak_and_fly.models import Students, Courses
from speak_and_fly.utils.data_manipulation import (
    create_basic_data,
    assign_multiple_students_to_course,
)
from speak_and_fly.utils.utils import create_tables
from speak_and_fly.config import session

if __name__ == "__main__":

    create_tables()
    create_basic_data()

    students = session.query(Students).all()
    english = session.query(Courses).filter(Courses.id == 1).one()
    assign_multiple_students_to_course(course=english, students=students)
    print(session.query(Courses).filter(Courses.id == 1).one())

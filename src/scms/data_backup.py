from src.scms.instructor import Instructor
from src.scms.student import Student
from src.scms.course import Course
from src.scms.enrollment import Enrollment
from src.scms.file_handler import FileHandler

class DataBackup:
    def __init__(self, courses_file_path:str, enrollments_file_path:str, students_file_path:str, instructors_file_path:str):
        self.__courses_file_handler: FileHandler = FileHandler(courses_file_path)
        self.__enrollments_file_handler: FileHandler = FileHandler(enrollments_file_path)
        self.__students_file_handler: FileHandler = FileHandler(students_file_path)
        self.__instructors_file_handler: FileHandler = FileHandler(instructors_file_path)


    def add_to_courses(self, course:Course) -> None:
        new_entry = f"{course.course_id},{course.course_name},{course.course_description},{course.instructor_id}"
        self.__courses_file_handler.write(new_entry)

    def add_to_enrollments(self, enrollment:Enrollment) -> None:
        new_entry = f"{enrollment.course_id},{enrollment.student_id},{enrollment.grade},{enrollment.timestamp}"
        self.__enrollments_file_handler.write(new_entry)

    def add_to_students(self, student:Student) -> None:
        new_entry = f"{student.student_id},{student.full_name},{student.email},{student.password}"
        self.__students_file_handler.write(new_entry)

    def add_to_instructors(self, instructor:Instructor) -> None:
        new_entry = f"{instructor.instructor_id},{instructor.full_name},{instructor.email},{instructor.password}"
        self.__instructors_file_handler.write(new_entry)

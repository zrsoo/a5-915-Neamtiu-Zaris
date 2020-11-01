"""
You will be given one of the problems below to solve using feature-driven development
The program must provide a menu-driven console user interface.
Use classes to represent the following:
The domain entity (complex, expense, student, book)
A services class that implements the required functionalities
The ui class which implements the user interface
Have 10 programmatically generated entries in the application at start-up.
Unit tests and specifications for non-UI functions related to the first functionality.


3. Students:
Manage a list of students. Each student has an id (integer, unique), a name (string) and a group (positive integer).
Provide the following features:

1.)Add a student. Student data is read from the console.
2.)Display the list of students.
3.)Filter the list so that students in a given group (read from the console) are deleted from the list.
4.)Undo the last operation that modified program data. This step can be repeated.
"""


# Imports

from domain.validators import StudentValidator
from services.service import StudentService
from tests.tests import test_add_student
from ui.console import Console

#


if __name__ == '__main__':
    try:
        test_add_student()

        validator = StudentValidator()

        student_service = StudentService(validator)
        student_service.generate_students()

        console = Console(student_service)
        console.run_console()

    except Exception as ex:
        print("Error: ", ex)
        #traceback.print_exc()
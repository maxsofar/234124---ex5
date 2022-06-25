import json
import os


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    studentsList = []
    with open(input_json_path, 'r') as f:
        data = json.load(f)
        for (id, info) in data.items():
            for course in info['registered_courses']:
                if course == course_name:
                    studentsList.append(info['student_name'])
                    break
    return studentsList




def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """

    with open(input_json_path, 'r') as f:
        with open(output_file_path, 'w') as o:
            data = json.load(f)
            coursesList = {}
            for (id, info) in data.items():
                for course in info['registered_courses']:
                    if course in coursesList:
                        coursesList[course] += 1
                    else:
                        coursesList[course] = 1
            for (course, numberOfStudents) in sorted(coursesList.items()):
                o.write('"' + course + '" ' + str(numberOfStudents) + '\n')


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass


# print(names_of_registered_students("/Users/Max/PycharmProjects/ex5/students_database.json",
#                                    "Introduction to Systems Programming"))
enrollment_numbers("/Users/Max/PycharmProjects/ex5/students_database.json", "output.txt")

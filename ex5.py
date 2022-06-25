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
    students_list = []
    with open(input_json_path, 'r') as i:
        data = json.load(i)
        for (id, info) in data.items():
            for course in info['registered_courses']:
                if course == course_name:
                    students_list.append(info['student_name'])
                    break
    return students_list




def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """

    with open(input_json_path, 'r') as i:
        with open(output_file_path, 'w') as o:
            data = json.load(i)
            courses_list = {}
            for (id, info) in data.items():
                for course in info['registered_courses']:
                    if course in courses_list:
                        courses_list[course] += 1
                    else:
                        courses_list[course] = 1
            for (course, numberOfStudents) in sorted(courses_list.items()):
                o.write('"' + course + '" ' + str(numberOfStudents) + '\n')


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturers_list = {}
    for file in os.listdir(json_directory_path):
        file_path = os.path.join(json_directory_path, file)
        if os.path.isfile(file_path) and file_path.endswith('.json'):
            with open(file_path, 'r') as i:
                data = json.load(i)
                for (courseNum, info) in data.items():
                    for lecturer in info['lecturers']:
                        if lecturer in lecturers_list.keys():
                            if info['course_name'] not in lecturers_list[lecturer]:
                                lecturers_list[lecturer].append(info['course_name'])
                        else:
                            lecturers_list[lecturer] = [info['course_name']]
    for file in os.listdir(output_json_path):
        file_path = os.path.join(output_json_path, file)
        if os.path.isfile(file_path) and file_path.endswith('.json'):
            with open(file_path, 'w') as o:
                json.dump(lecturers_list, o, indent=4)


# print(names_of_registered_students("/Users/Max/PycharmProjects/ex5/students_database.json",
#                                 "Introduction to Systems Programming"))
#enrollment_numbers("/Users/Max/PycharmProjects/ex5/students_database.json", "output.txt")

#courses_for_lecturers("semesters_databases", "output")

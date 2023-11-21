import unittest
import copy
from src.Canvas import course_functions as cf
from src.Tests import test_consts as test_const


class TestGetAllPendingAssignments(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_one_pending_assignments(self):
        courses = test_const.COURSES_3
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = test_const.ASSIGNMENTS_2
        self.assertEqual(expected, actual)

    def test_empty_course_name(self):
        courses = copy.deepcopy(test_const.COURSES_3)
        courses['COURSE KEY 1']['course_name'] = None
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = test_const.ASSIGNMENTS_0

        self.assertEqual(expected, actual)

    def test_multiple_empty_course_name(self):
        courses = copy.deepcopy(test_const.COURSES_4)
        courses['COURSE KEY 1']['course_name'] = None
        courses['COURSE KEY 2']['course_name'] = None
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = test_const.ASSIGNMENTS_6

        self.assertEqual(expected, actual)

    def test_multiple_one_course_name_empty(self):
        courses = copy.deepcopy(test_const.COURSES_4)
        courses['COURSE KEY 1']['course_name'] = None
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = test_const.ASSIGNMENTS_7

        self.assertEqual(expected, actual)


class TestGetAssignment(unittest.TestCase):
    def test_null_assignments(self):
        assignments = {}
        assignment_id = 'Assignment ID 1'
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_assignment_id(self):
        assignments = test_const.ASSIGNMENTS_2
        assignment_id = None
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_assignment(self):
        assignments = test_const.ASSIGNMENTS_2
        assignment_id = 'Assignment ID 1'
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = test_const.ASSIGNMENT_1
        self.assertEqual(expected, actual)

    def test_get_assignment_multiple(self):
        assignments = test_const.ASSIGNMENTS_3
        assignment_id = 'Assignment ID 2'
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = test_const.ASSIGNMENT_2
        self.assertEqual(expected, actual)

    def test_null_assignment_value(self):
        assignments = test_const.ASSIGNMENTS_1
        assignment_id = 'Assignment ID'
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_subject_value(self):
        assignments = copy.deepcopy(test_const.ASSIGNMENTS_1)
        assignments['Course Name 1'] = {}
        assignment_id = 'Assignment ID'
        actual = cf.get_assignment(assignments=assignments, assignment_id=assignment_id)
        expected = None
        self.assertEqual(expected, actual)


class TestGetAllDueToday(unittest.TestCase):
    def test_null_assignments(self):
        assignments = {}
        actual = cf.get_all_due_today(assignments=assignments)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_one_due_today_false(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_get_one_due_today_true(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": True
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {
            '452465': {
                "name": "Assignment 1",
                "points": 50.0,
                "description": 'Assignment 1 description',
                "due": "November 04, 2023 03:59 PM",
                "due_today": True
            }
        }
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        assignments = {
            'Test Course': {}
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_true_one_course(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": True
                },
                '2': {
                    "name": "Assignment 2",
                    "points": 10.0,
                    "description": 'Assignment 2 description',
                    "due": "November 25, 2029 9:00 PM",
                    "due_today": True
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {
            '452465': {
                "name": "Assignment 1",
                "points": 50.0,
                "description": 'Assignment 1 description',
                "due": "November 04, 2023 03:59 PM",
                "due_today": True
            },
            '2': {
                "name": "Assignment 2",
                "points": 10.0,
                "description": 'Assignment 2 description',
                "due": "November 25, 2029 9:00 PM",
                "due_today": True
            }
        }
        self.assertEqual(expected, actual)

    def test_multiple_false_one_course(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": False
                },
                '2': {
                    "name": "Assignment 2",
                    "points": 10.0,
                    "description": 'Assignment 2 description',
                    "due": "November 25, 2029 9:00 PM",
                    "due_today": False
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_false_multiple_course(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": False
                }
            },
            'Test Course 2': {
                '2': {
                    "name": "Assignment 2",
                    "points": 10.0,
                    "description": 'Assignment 2 description',
                    "due": "November 25, 2029 9:00 PM",
                    "due_today": False
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_true_multiple_course(self):
        assignments = {
            'Test Course': {
                '452465': {
                    "name": "Assignment 1",
                    "points": 50.0,
                    "description": 'Assignment 1 description',
                    "due": "November 04, 2023 03:59 PM",
                    "due_today": True
                }
            },
            'Test Course 2': {
                '2': {
                    "name": "Assignment 2",
                    "points": 10.0,
                    "description": 'Assignment 2 description',
                    "due": "November 25, 2029 9:00 PM",
                    "due_today": True
                }
            }
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {
            '452465': {
                "name": "Assignment 1",
                "points": 50.0,
                "description": 'Assignment 1 description',
                "due": "November 04, 2023 03:59 PM",
                "due_today": True
            },
            '2': {
                "name": "Assignment 2",
                "points": 10.0,
                "description": 'Assignment 2 description',
                "due": "November 25, 2029 9:00 PM",
                "due_today": True
            }
        }
        self.assertEqual(expected, actual)


class TestGetAllCoursesNames(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        actual = cf.get_all_course_names(courses=courses)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_one_course(self):
        courses = {
            'test': {
                'course_name': 'Course 1'
            },
        }
        actual = cf.get_all_course_names(courses=courses)
        expected = ['Course 1']
        self.assertEqual(expected, actual)

    def test_empty_value(self):
        courses = {
            'test_course_code': {}
        }
        actual = cf.get_all_course_names(courses=courses)
        expected = []
        self.assertEqual(expected, actual)

    def test_multiple(self):
        courses = {
            'Test': {
                'course_name': 'Course 1'
            },
            'Test1': {
                'course_name': 'Course 2'
            },
            'Test 3': {
                'course_name': 'Course 3'
            }
        }
        actual = cf.get_all_course_names(courses=courses)
        expected = ['Course 1', 'Course 2', 'Course 3']
        self.assertEqual(expected, actual)


class TestGetAnnouncement(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'latest_announcement': 'Test Announcement'
            }
        }
        course_key = None
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_announcement(self):
        courses = {
            'Test Key': {
                'latest_announcement': 'Test Announcement'
            }
        }
        course_key = "Test Key"
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = 'Test Announcement'
        self.assertEqual(expected, actual)

    def test_empty_value(self):
        courses = {
            'Test Key': {}
        }
        course_key = "Test Key"
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_announcement_value(self):
        courses = {
            'Test Key': {
                'latest_announcement': None
            }
        }
        course_key = 'Test Key'
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)


class TestGetTeacher(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'teacher': 'Mr. Test'
            }
        }
        course_key = None
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_teacher(self):
        courses = {
            'Test Key': {
                'teacher': 'Mr. Test'
            }
        }
        course_key = "Test Key"
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = 'Mr. Test'
        self.assertEqual(expected, actual)

    def test_empty_value(self):
        courses = {
            'Test Key': {}
        }
        course_key = "Test Key"
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_teacher_value(self):
        courses = {
            'Test Key': {
                'teacher': None
            }
        }
        course_key = 'Test Key'
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)


class TestGetCourseCode(unittest.TestCase):
    def test_null(self):
        orig_course_code = None
        actual = cf.get_course_code(orig_course_code)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_course_code(self):
        orig_course_code = 'orig | Test Subject'
        actual = cf.get_course_code(orig_course_code)
        expected = 'ORIG'
        self.assertEqual(expected, actual)

    def test_get_course_code_2(self):
        orig_course_code = 'orig | Test Subject | HAHAH'
        actual = cf.get_course_code(orig_course_code)
        expected = 'ORIG'
        self.assertEqual(expected, actual)


class TestGetSection(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'original_name': 'Code | Section | Subject'
            }
        }
        course_key = None
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_section(self):
        courses = {
            'Test Key': {
                'original_name': 'Code | Section | Subject'
            }
        }
        course_key = 'Test Key'
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = 'Section'
        self.assertEqual(expected, actual)

    def test_get_section_with_space(self):
        courses = {
            'Test Key': {
                'original_name': 'Code | Section 2A | Subject'
            }
        }
        course_key = 'Test Key'
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = 'Section 2A'
        self.assertEqual(expected, actual)

    def test_empty_value(self):
        courses = {
            'Test Key': {}
        }
        course_key = 'Test Key'
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_name_value(self):
        courses = {
            'Test Key': {
                'original_name': None
            }
        }
        course_key = 'Test Key'
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

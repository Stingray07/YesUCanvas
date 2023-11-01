import unittest
from unittest.mock import patch
import course_functions as cf


class TestGetAllPendingAssignments(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_one_pending_announcements(self):
        courses = {
            'Test Key': {
                'course_name': 'Test Course Name',
                'pending_assignments': {
                    'Assignment ID': {
                        'name': 'Assignment 1',
                        'points': 50,
                        'description': 'Test description',
                        'due': 'October 17, 2023',
                        'due_today': False
                    }
                }
            },
        }
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = {
            'Test Course Name': {
                'Assignment ID': {
                    'name': 'Assignment 1',
                    'points': 50,
                    'description': 'Test description',
                    'due': 'October 17, 2023',
                    'due_today': False
                }
            }
        }
        self.assertEqual(expected, actual)

    def test_empty_course_name(self):
        courses = {
            'Test Key': {
                'course_name': None,
                'pending_assignments': {
                    'Assignment ID': {
                        'name': 'Assignment 1',
                        'points': 50,
                        'description': 'Test description',
                        'due': 'October 17, 2023',
                        'due_today': False
                    }
                }
            }
        }
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = {
            'Course Not Found': {
                'Assignment ID': {
                    'name': 'Assignment 1',
                    'points': 50,
                    'description': 'Test description',
                    'due': 'October 17, 2023',
                    'due_today': False
                }
            }
        }

        self.assertEqual(expected, actual)

    def test_multiple_empty_course_name(self):
        courses = {
            'Test Key': {
                'course_name': None,
                'pending_assignments': {
                    'Assignment ID': {
                        'name': 'Assignment 1',
                        'points': 50,
                        'description': 'Test description',
                        'due': 'October 17, 2023',
                        'due_today': False
                    }
                }
            },
            'Test Key 2': {
                'course_name': None,
                'pending_assignments': {
                    'Assignment ID 2': {
                        'name': 'Assignment 2',
                        'points': 50,
                        'description': ' Test description 2',
                        'due': 'November 10, 2025',
                        'due_today': False
                    }
                }
            }
        }
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = {
            'Course Not Found': {
                'Assignment ID': {
                    'name': 'Assignment 1',
                    'points': 50,
                    'description': 'Test description',
                    'due': 'October 17, 2023',
                    'due_today': False
                },
                'Assignment ID 2': {
                    'name': 'Assignment 2',
                    'points': 50,
                    'description': ' Test description 2',
                    'due': 'November 10, 2025',
                    'due_today': False
                }
            }
        }

        self.assertEqual(expected, actual)

    def test_multiple_one_course_name_empty(self):
        courses = {
            'Test Key': {
                'course_name': None,
                'pending_assignments': {
                    'Assignment ID': {
                        'name': 'Assignment 1',
                        'points': 50,
                        'description': 'Test description',
                        'due': 'October 17, 2023',
                        'due_today': False
                    }
                }
            },
            'Test Key 2': {
                'course_name': 'Course 2',
                'pending_assignments': {
                    'Assignment ID 2': {
                        'name': 'Assignment 2',
                        'points': 50,
                        'description': ' Test description 2',
                        'due': 'November 10, 2025',
                        'due_today': False
                    }
                }
            }
        }
        actual = cf.get_all_pending_assignments(courses=courses)
        expected = {
            'Course Not Found': {
                'Assignment ID': {
                    'name': 'Assignment 1',
                    'points': 50,
                    'description': 'Test description',
                    'due': 'October 17, 2023',
                    'due_today': False
                }
            },
            'Course 2': {
                'Assignment ID 2': {
                    'name': 'Assignment 2',
                    'points': 50,
                    'description': ' Test description 2',
                    'due': 'November 10, 2025',
                    'due_today': False
                }
            }
        }

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

import unittest
import course_functions as cf


class TestGetAllCoursesNames(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        func_result = cf.get_all_course_names(courses=courses)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_get_all_course(self):
        courses = {
            'test': {
                'course_name': 'Course 1'
            },
        }
        func_result = cf.get_all_course_names(courses=courses)
        test_result = ['Course 1']
        self.assertEqual(func_result, test_result)

    def test_empty_value(self):
        courses = {
            'test_course_code': {}
        }
        func_result = cf.get_all_course_names(courses=courses)
        test_result = []
        self.assertEqual(func_result, test_result)

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
        func_result = cf.get_all_course_names(courses=courses)
        test_result = ['Course 1', 'Course 2', 'Course 3']
        self.assertEqual(func_result, test_result)


class TestGetAnnouncement(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        func_result = cf.get_announcement(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'latest_announcement': 'Test Announcement'
            }
        }
        course_key = None
        func_result = cf.get_announcement(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_get_announcement(self):
        courses = {
            'Test Key': {
                'latest_announcement': 'Test Announcement'
            }
        }
        course_key = "Test Key"
        func_result = cf.get_announcement(courses=courses, course_key=course_key)
        test_result = 'Test Announcement'
        self.assertEqual(func_result, test_result)

    def test_empty_value(self):
        courses = {
            'Test Key': {}
        }
        course_key = "Test Key"
        func_result = cf.get_announcement(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_empty_announcement_value(self):
        courses = {
            'Test Key': {
                'latest_announcement': None
            }
        }
        course_key = 'Test Key'
        func_result = cf.get_announcement(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)


class TestGetTeacher(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        func_result = cf.get_teacher(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'teacher': 'Mr. Test'
            }
        }
        course_key = None
        func_result = cf.get_teacher(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_get_teacher(self):
        courses = {
            'Test Key': {
                'teacher': 'Mr. Test'
            }
        }
        course_key = "Test Key"
        func_result = cf.get_teacher(courses=courses, course_key=course_key)
        test_result = 'Mr. Test'
        self.assertEqual(func_result, test_result)

    def test_empty_value(self):
        courses = {
            'Test Key': {}
        }
        course_key = "Test Key"
        func_result = cf.get_teacher(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_empty_teacher_value(self):
        courses = {
            'Test Key': {
                'teacher': None
            }
        }
        course_key = 'Test Key'
        func_result = cf.get_teacher(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)


class TestGetCourseCode(unittest.TestCase):
    def test_null(self):
        orig_course_code = None
        func_result = cf.get_course_code(orig_course_code)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_get_course_code(self):
        orig_course_code = 'orig | Test Subject'
        func_result = cf.get_course_code(orig_course_code)
        test_result = 'ORIG'
        self.assertEqual(func_result, test_result)


class TestGetSection(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        course_key = 'Test Key'
        func_result = cf.get_section(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_null_course_key(self):
        courses = {
            'Test': {
                'original_name': 'Code | Section | Subject'
            }
        }
        course_key = None
        func_result = cf.get_section(courses=courses, course_key=course_key)
        test_result = None
        self.assertEqual(func_result, test_result)

    def test_get_section(self):
        courses = {
            'Test Key': {
                'original_name': 'Code | Section | Subject'
            }
        }
        course_key = 'Test Key'
        func_result = cf.get_section(courses=courses, course_key=course_key)
        test_result = 'Section'
        self.assertEqual(func_result, test_result)

if __name__ == '__main__':
    unittest.main()

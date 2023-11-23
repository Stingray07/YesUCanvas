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
        assignments = copy.deepcopy(test_const.ASSIGNMENTS_2)
        assignments['Course Name 1']['Assignment ID 1']['due_today'] = False
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_get_one_due_today_true(self):
        assignments = test_const.ASSIGNMENTS_2
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {'Assignment ID 1': test_const.ASSIGNMENT_1}
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        assignments = {
            'Course Name 1': {}
        }
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_true_one_course(self):
        assignments = test_const.ASSIGNMENTS_4
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {'Assignment ID 1': test_const.ASSIGNMENT_1,
                    'Assignment ID 2': test_const.ASSIGNMENT_2}
        self.assertEqual(expected, actual)

    def test_multiple_false_one_course(self):
        assignments = copy.deepcopy(test_const.ASSIGNMENTS_4)
        assignments['Course Name 1']['Assignment ID 1']['due_today'] = False
        assignments['Course Name 1']['Assignment ID 2']['due_today'] = False
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_false_multiple_course(self):
        assignments = copy.deepcopy(test_const.ASSIGNMENTS_3)
        assignments['Course Name 1']['Assignment ID 1']['due_today'] = False
        assignments['Course Name 2']['Assignment ID 2']['due_today'] = False
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {}
        self.assertEqual(expected, actual)

    def test_multiple_true_multiple_course(self):
        assignments = test_const.ASSIGNMENTS_3
        actual = cf.get_all_due_today(assignments=assignments)
        expected = {'Assignment ID 1': test_const.ASSIGNMENT_1,
                    'Assignment ID 2': test_const.ASSIGNMENT_2}
        self.assertEqual(expected, actual)


class TestGetAllCoursesNames(unittest.TestCase):
    def test_null_courses(self):
        courses = {}
        actual = cf.get_all_course_names(courses=courses)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_one_course(self):
        courses = test_const.COURSES_3
        actual = cf.get_all_course_names(courses=courses)
        expected = ['Course Name 1']
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        courses = test_const.COURSES_1
        actual = cf.get_all_course_names(courses=courses)
        expected = []
        self.assertEqual(expected, actual)

    def test_multiple(self):
        courses = test_const.COURSES_4
        actual = cf.get_all_course_names(courses=courses)
        expected = ['Course Name 1', 'Course Name 2']
        self.assertEqual(expected, actual)


class TestGetAnnouncement(unittest.TestCase):
    course_key = 'COURSE KEY 1'

    def test_null_courses(self):
        courses = {}
        actual = cf.get_announcement(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = test_const.COURSES_3
        course_key = None
        actual = cf.get_announcement(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_announcement(self):
        courses = test_const.COURSES_3
        actual = cf.get_announcement(courses=courses, course_key=self.course_key)
        expected = 'Latest Announcement 1'
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        courses = test_const.COURSES_0
        actual = cf.get_announcement(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_announcement_value(self):
        courses = test_const.COURSES_1
        actual = cf.get_announcement(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)


class TestGetTeacher(unittest.TestCase):
    course_key = 'COURSE KEY 1'

    def test_null_courses(self):
        courses = {}
        actual = cf.get_teacher(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = test_const.COURSES_3
        course_key = None
        actual = cf.get_teacher(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_teacher(self):
        courses = test_const.COURSES_3
        actual = cf.get_teacher(courses=courses, course_key=self.course_key)
        expected = 'Teacher 1'
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        courses = test_const.COURSES_0
        actual = cf.get_teacher(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_teacher_value(self):
        courses = test_const.COURSES_1
        actual = cf.get_teacher(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)


class TestGetCourseCode(unittest.TestCase):
    def test_null(self):
        orig_course_code = None
        actual = cf.get_course_code(orig_course_code)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_course_code(self):
        orig_course_code = 'COURSE CODE | COURSE SECTION'
        actual = cf.get_course_code(orig_course_code)
        expected = 'COURSE CODE'
        self.assertEqual(expected, actual)

    def test_get_course_code_2(self):
        orig_course_code = 'COURSE CODE | COURSE SECTION | COURSE NAME'
        actual = cf.get_course_code(orig_course_code)
        expected = 'COURSE CODE'
        self.assertEqual(expected, actual)


class TestGetSection(unittest.TestCase):
    course_key = 'COURSE KEY 1'

    def test_null_courses(self):
        courses = {}
        actual = cf.get_section(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = test_const.COURSES_3
        course_key = None
        actual = cf.get_section(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_section(self):
        courses = test_const.COURSES_3
        actual = cf.get_section(courses=courses, course_key=self.course_key)
        expected = 'Section 1'
        self.assertEqual(expected, actual)

    def test_get_section_with_space(self):
        courses = test_const.COURSES_3
        actual = cf.get_section(courses=courses, course_key=self.course_key)
        expected = 'Section 1'
        self.assertEqual(expected, actual)

    def test_empty_value(self):
        courses = test_const.COURSES_0
        actual = cf.get_section(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_empty_name_value(self):
        courses = test_const.COURSES_1
        actual = cf.get_section(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)


class TestGetModules(unittest.TestCase):
    course_key = 'COURSE KEY 1'

    def test_null_courses(self):
        courses = {}
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=self.course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_null_course_key(self):
        courses = test_const.COURSES_3
        course_key = None
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=course_key)
        expected = None
        self.assertEqual(expected, actual)

    def test_get_modules_(self):
        courses = test_const.COURSES_3
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=self.course_key)
        expected = test_const.MODULES_1
        self.assertEqual(expected, actual)

    def test_get_multiple_modules(self):
        courses = test_const.COURSES_5
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=self.course_key)
        expected = test_const.MODULES_2
        self.assertEqual(expected, actual)

    def test_empty_modules_value(self):
        courses = test_const.COURSES_1
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=self.course_key)
        expected = {}
        self.assertEqual(expected, actual)

    def test_empty_course_value(self):
        courses = test_const.COURSES_0
        actual = cf.get_all_modules_from_course_key(courses=courses, course_key=self.course_key)
        expected = {}
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

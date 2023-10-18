def get_all_pending_assignments(courses):
    assignments = {}
    for course_key, course_value in courses.items():
        assignments[course_value['course_name']] = course_value['pending_assignments']

    return assignments


def get_course_code(orig_course_code):
    separator_index = orig_course_code.index("|")
    orig_course_code = orig_course_code[:separator_index-1]
    return orig_course_code

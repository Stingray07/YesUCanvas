def get_all_pending_assignments(courses):
    assignments = {}
    for course_key, course_value in courses.items():
        assignments[course_value['course_name']] = course_value['pending_assignments']

    return assignments


def get_announcement(courses, course_key):
    if course_key not in courses:
        return None

    return courses[course_key]['latest_announcement']


def get_teacher(courses, course_key):
    if course_key not in courses:
        return None

    return courses[course_key]['teacher']


def get_all_course_names(courses):
    names = []
    for _, course_value in courses.items():
        names.append(course_value['course_name'])

    return names


def get_course_code(orig_course_code):
    separator_index = orig_course_code.index("|")
    orig_course_code = orig_course_code[:separator_index-1]
    return orig_course_code

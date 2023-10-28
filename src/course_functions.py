from helper import format_data


def get_all_pending_assignments(courses):
    if not courses:
        return None

    assignments = {}
    for course_key, course_value in courses.items():
        if courses[course_key].get('course_name'):
            assignments[course_value['course_name']] = course_value['pending_assignments']
        else:
            for assignment_id, assignment_value in course_value['pending_assignments'].items():
                assignments['Course Not Found'] =

    return assignments


def get_all_due_today(assignments):
    if not assignments:
        return None

    due_today = {}

    for course_key, course_value in assignments.items():
        if not course_value:
            continue

        for assignment_id, assignment_value in course_value.items():
            if assignments[course_key][assignment_id]['due_today']:
                due_today[assignment_id] = assignment_value

    return due_today


def get_all_course_names(courses):
    if not courses:
        return None

    names = []
    for _, course_value in courses.items():
        if course_value.get('course_name'):
            names.append(course_value['course_name'])

    return names


def get_announcement(courses, course_key):
    if course_key not in courses:
        return None

    if not courses[course_key].get('latest_announcement'):
        return None

    return courses[course_key]['latest_announcement']


def get_teacher(courses, course_key):
    if course_key not in courses:
        return None

    if not courses[course_key].get('teacher'):
        return None

    return courses[course_key]['teacher']


def get_course_code(orig_course_code):
    if not orig_course_code:
        return None

    separator_index = orig_course_code.index("|")
    orig_course_code = orig_course_code[:separator_index-1]
    return orig_course_code.upper()


def get_section(courses, course_key):
    if course_key not in courses:
        return None

    if not courses[course_key].get('original_name'):
        return None

    sep_found = False
    section = ''
    for c in courses[course_key]['original_name']:
        if c == '|' and not section:
            sep_found = True
            continue
        elif c == '|' and section:
            return section

        if sep_found and c != ' ':
            section += c

    return section

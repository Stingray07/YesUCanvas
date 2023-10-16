from helper import format_data
import os
import requests
from decorators import handle_req_errors
from dotenv import load_dotenv

load_dotenv()
COURSES_URL = 'https://uc-bcf.instructure.com/api/v1/courses'
ANNOUNCEMENTS_URL = 'https://uc-bcf.instructure.com/api/v1/announcements'
CALENDAR_URL = 'https://uc-bcf.instructure.com/api/v1/calendar_events'
ACTIVE_ENROLLMENT_STATE = 'active'
API_KEY = os.getenv("API_KEY")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}


@handle_req_errors
def get_current_courses_name(page_number, per_page):
    params = {
        'enrollment_state': ACTIVE_ENROLLMENT_STATE,
        'page': page_number,
        'per_page': per_page
    }

    courses = {}
    response = requests.get(COURSES_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    for item in data:
        course_name = item.get('name', None)
        course_id = item.get('id', None)
        original_name = item.get('original_name', None)

        if course_name.isupper():
            orig_course_code = item.get('course_code', None)
            course_code = get_course_code(orig_course_code)

            courses[course_code] = {
                'course_name': course_name,
                'course_id': course_id,
                'original_name': original_name,
            }

    return courses


@handle_req_errors
def get_latest_announcement(course):
    context_code = f'course_{course["course_id"]}'
    params = {
        'context_codes[]': [context_code],
        'latest_only': True
    }

    response = requests.get(ANNOUNCEMENTS_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()
    markdown_message = data[0]['message']

    return markdown_message


@handle_req_errors
def get_pending_assignments(course):
    course_id = course['course_id']
    ASSIGNMENT_URL = f'{COURSES_URL}/{course_id}/assignments'
    pending_assignments = {}

    params = {
        'include[]': ['submission']
    }

    response = requests.get(ASSIGNMENT_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    course_name = course['course_name']
    pending_assignments['course'] = course_name

    for assignment in data:
        due = assignment['due_at']
        description = assignment['description']
        points = assignment['points_possible']
        name = assignment['name']
        assignment_id = assignment['id']
        status = assignment['submission']['submitted_at']
        if not status:
            pending_assignments[assignment_id] = {
                'name': name,
                'points': points,
                'description': description,
                'due': due,
            }

    return pending_assignments


@handle_req_errors
def get_teacher(course):
    course_id = course['course_id']
    USER_URL = f'{COURSES_URL}/{course_id}/users'

    params = {
        'enrollment_type[]': ['teacher']
    }

    response = requests.get(USER_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()
    teacher = data[0]['name']

    return teacher


@handle_req_errors
def get_module(course):
    course_id = course['course_id']
    MODULES_URL = f"{COURSES_URL}/{course_id}/modules"
    modules = {}

    params = {
        'include[]': ['items']
    }

    response = requests.get(MODULES_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    items_list = []
    course_name = course['course_name']
    modules['course'] = course_name

    for module in data:
        name = module['name']
        module_id = module['id']
        items = module['items']

        for item in items:
            item_name = item['title']
            items_list.append(item_name)

        modules[module_id] = {
            'name': name,
            'items': items_list,
        }
        items_list = []

    return modules


def get_all_pending_assignments(courses):
    assignments = {}
    for course_name, course_id in courses.items():
        assignments[course_name] = get_pending_assignments(course_id)

    return assignments


def get_course_code(orig_course_code):
    separator_index = orig_course_code.index("|")
    orig_course_code = orig_course_code[:separator_index-1]
    return orig_course_code

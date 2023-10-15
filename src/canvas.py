import json
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
        # format_data(item)
        course_name = item.get('name')
        course_id = item.get('id')
        original_name = item.get('original_name')

        if course_name.isupper():
            # gets real shortened course code
            orig_course_code = item.get('course_code')
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
    print(context_code)
    params = {
        'context_codes[]': [context_code],
        'latest_only': True
    }

    response = requests.get(ANNOUNCEMENTS_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()
    html_message = data[0]['message']

    return html_message


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

    for assignment in data:
        assignment_due = assignment['due_at']
        assignment_description = assignment['description']
        assignment_points = assignment['points_possible']
        assignment_name = assignment['name']
        assignment_id = assignment['id']
        assignment_status = assignment['submission']['submitted_at']
        if not assignment_status:
            pending_assignments[assignment_id] = {
                'assignment_name': assignment_name,
                'assignment_points': assignment_points,
                'assignment_description': assignment_description,
                'assignment_due': assignment_due,
                'assignment_subject': course['course_name']
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

    params = {
        'include[]': ['items']
    }

    response = requests.get(MODULES_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    format_data(data)


def get_all_pending_assignments(courses):
    assignments = {}
    for course_name, course_id in courses.items():
        assignments[course_name] = get_pending_assignments(course_id)

    return assignments


def format_data(data):
    print(json.dumps(data, indent=4))


def get_course_code(orig_course_code):
    separator_index = orig_course_code.index("|")
    orig_course_code = orig_course_code[:separator_index-1]
    return orig_course_code

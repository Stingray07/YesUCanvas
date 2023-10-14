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


@handle_req_errors
def get_current_courses_name(page_number, per_page):
    params = {
        'enrollment_state': ACTIVE_ENROLLMENT_STATE,
        'page': page_number,
        'per_page': per_page
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    courses = {}
    response = requests.get(COURSES_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    for item in data:
        course_name = item.get('name')
        course_id = item.get('id')
        if course_name.isupper():
            courses[course_name] = course_id

    return courses


@handle_req_errors
def get_latest_announcement(course):
    params = {
        'context_codes[]': [course],
        'latest_only': True
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(ANNOUNCEMENTS_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    html_message = data[0]['message']

    return html_message


@handle_req_errors
def get_pending_assignments(course_id):
    assignment_url = f'{COURSES_URL}/{course_id}/assignments'
    pending_assignments = []
    params = {
        'include[]': ['submission']
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(assignment_url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    for assignment in data:
        assignment_name = assignment['name']
        assignment_status = assignment['submission']['submitted_at']
        if not assignment_status:
            pending_assignments.append(assignment_name)

    return pending_assignments


def get_all_pending_assignments(courses):
    assignments = {}
    for course_name, course_id in courses.items():
        assignments[course_name] = get_pending_assignments(course_id)

    return assignments


@handle_req_errors
def get_teacher(course_id):
    user_url = f'{COURSES_URL}/{course_id}/users'

    params = {
        'enrollment_type[]': ['teacher']
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(user_url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    return data[0]['name']


def format_data(data):
    print(json.dumps(data, indent=4))

def get_course_code(orig_course_code):
    pass

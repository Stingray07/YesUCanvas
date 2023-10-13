import json
import os
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()
COURSES_URL = 'https://uc-bcf.instructure.com/api/v1/courses'
ANNOUNCEMENTS_URL = 'https://uc-bcf.instructure.com/api/v1/announcements'
CALENDAR_URL = 'https://uc-bcf.instructure.com/api/v1/calendar_events'
ACTIVE_ENROLLMENT_STATE = 'active'
API_KEY = os.getenv("API_KEY")


def get_current_courses_name(page_number, per_page):
    params = {
        'enrollment_state': ACTIVE_ENROLLMENT_STATE,
        'page': page_number,
        'per_page': per_page
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.get(COURSES_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        courses = {}

        for item in data:
            course_name = item.get('name')
            course_id = item.get('id')
            if course_name.isupper():
                courses[course_name] = course_id

        return courses

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None


def get_latest_announcement(course):
    params = {
        'context_codes[]': [course],
        'latest_only': True
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(ANNOUNCEMENTS_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        html_message = data[0]['message']
        return html_message

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None


def get_assignments(page_number, per_page):
    my_date = date(2023, 9, 1)
    params = {
        'start_date': my_date
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(CALENDAR_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None

def format_data(data):
    print(json.dumps(data, indent=4))

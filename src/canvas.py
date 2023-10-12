import os
import requests
from dotenv import load_dotenv

load_dotenv()
COURSES_URL = 'https://uc-bcf.instructure.com/api/v1/courses'
ANNOUNCEMENTS_URL = 'https://uc-bcf.instructure.com/api/v1/announcements'
ACTIVE_ENROLLMENT_STATE = 'active'
API_KEY = os.getenv("API_KEY")


def get_current_courses_name(api_key, page_number, per_page):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    params = {
        'enrollment_state': ACTIVE_ENROLLMENT_STATE,
        'page': page_number,
        'per_page': per_page
    }
    try:
        response = requests.get(COURSES_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        courses = []

        for item in data:
            course_name = item.get('name')
            if course_name.isupper():
                courses.append(course_name)

        return courses

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None

# def get_latest_announcement(course, api_key):
#     context_code = [course]
#
#     params = {
#         'context_codes[]': context_code
#     }
#     headers = {
#         "Authorization": f"Bearer {api_key}"
#     }
#
#     response = requests.get(ANNOUNCEMENTS_URL, headers=headers, params=params)
#
#     if response.status_code != 200:
#         print(response.status_code)
#         return []
#
#     data = response.json()
#     return data
import canvas as cs
from course_functions import get_all_pending_assignments
from bot import run_bot


if __name__ == "__main__":
    courses = cs.get_current_courses()
    cs.format_data(get_all_pending_assignments(courses))
    # run_bot()





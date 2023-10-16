import canvas as cs
from helper import format_data

PAGINATION_PAGE_NUMBER = 1
PAGINATION_PER_PAGE = 20


if __name__ == "__main__":
    courses = cs.get_current_courses_name(per_page=PAGINATION_PER_PAGE, page_number=PAGINATION_PAGE_NUMBER)
    format_data(cs.get_module(courses["PE 4N"]))

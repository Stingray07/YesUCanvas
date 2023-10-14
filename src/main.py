import canvas as cs

PAGINATION_PAGE_NUMBER = 1
PAGINATION_PER_PAGE = 20


if __name__ == "__main__":
    print("Hello")
    courses = cs.get_current_courses_name(per_page=PAGINATION_PER_PAGE, page_number=PAGINATION_PAGE_NUMBER)
    cs.format_data(cs.get_teacher(courses['DESIGN AND ANALYSIS OF ALGORITHM']))


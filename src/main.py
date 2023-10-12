import canvas as cs
import os
from dotenv import load_dotenv

API_KEY = os.getenv("API_KEY")
load_dotenv()

if __name__ == "__main__":
    print("Hello")
    print(cs.get_current_courses_name(api_key=API_KEY, page_number=1, per_page=20))

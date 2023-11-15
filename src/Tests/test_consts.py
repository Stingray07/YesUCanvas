# course consts

COURSES_0 = {
    'COURSE KEY 1': {},
    'COURSE KEY 2': {}
}

COURSES_1 = {
    'COURSE KEY 1': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {},
        'original_name': ''
    }
}

COURSES_2 = {
    'COURSE KEY 1': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {},
        'original_name': ''
    },
    'COURSE KEY 2': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {},
        'original_name': ''
    }
}

COURSES_3 = {
    'COURSE KEY 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {
            'Assignment ID 1': {
                'name': 'Assignment Name 1',
                'points': 50,
                'description': 'Assignment Description 1',
                'due': 'October 17, 2023',
                'due_today': False
            }
        },
        'teacher': 'Teacher 1',
        'latest_announcement': 'Latest Announcement 1',
        'modules': {
            "Module ID 1": {
                "name": "Module Name 1",
                "items": ['Item 1', 'Item 2', 'Item 3']
            }
        },
        "original_name": "Course Key 1 | Section 1 | Course Name 1",
    }
}

COURSES_4 = {
    'COURSE KEY 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {
            'Assignment ID 1': {
                'name': 'Assignment Name 1',
                'points': 50,
                'description': 'Assignment Description 1',
                'due': 'October 17, 2023',
                'due_today': True
            }
        },
        'teacher': 'Teacher 1',
        'latest_announcement': 'Latest Announcement 1',
        'modules': {
            'Module ID 1': {
                'name': 'Module Name 1',
                'items': ['Item 1', 'Item 2', 'Item 3']
            }
        }
    },
    'COURSE KEY 2': {
        'course_name': 'Course Name 2',
        'pending_assignments': {
            'Assignment ID 2': {
                'name': 'Assignment Name 2',
                'points': 100,
                'description': 'Assignment Description 2',
                'due': 'October 18, 2023',
                'due_today': False
            }
        },
        'teacher': 'Teacher 2',
        'latest_announcement': 'Latest Announcement 2',
        'modules': {
            'Module ID 2': {
                'name': 'Module Name 2',
                'items': ['Item 4', 'Item 5', 'Item 6']
            }
        }
    }
}

COURSES_5 = {
    'COURSE KEY 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {
            'Assignment ID 1': {
                'name': 'Assignment Name 1',
                'points': 50,
                'description': 'Assignment Description 1',
                'due': 'October 17, 2023',
                'due_today': True
            },
            'Assignment ID 2': {
                'name': 'Assignment Name 2',
                'points': 100,
                'description': 'Assignment Description 2',
                'due': 'October 18, 2023',
                'due_today': False
            }
        },
        'latest_announcement': 'Latest Announcement 1',
        'modules': {
            'Module ID 1': {
                'name': ' Module Name 1',
                'items': ['Item 1', 'Item 2', 'Item 3']
            },
            'Module ID 2': {
                'name': 'Module Name 2',
                'items': ['Item 4', 'Item 5', 'Item 6']
            }
        },
        'teacher': 'Teacher 1'
    }
}


# assignments consts


ASSIGNMENTS_0 = {
    'Course Name 1': {},
    'Course Not Found': {}
}

ASSIGNMENTS_1 = {
    'Course Name 1': {
        'Assignment ID 1': {}
    }
}

ASSIGNMENTS_2 = {
    'Course Name 1': {
        'Assignment ID 1': {
            'name': 'Assignment Name 1',
            'points': 50,
            'description': 'Assignment Description 1',
            'due': 'October 17, 2023',
            'due_today': False
        }
    }
}

ASSIGNMENTS_3 = {
    'Course Name 1': {
        'Assignment ID 1': {
            'name': 'Assignment Name 1',
            'points': 50,
            'description': 'Assignment Description 1',
            'due': 'October 17, 2023',
            'due_today': True
        }
    },
    'Course Name 2': {
        'Assignment ID 2': {
            'name': 'Assignment Name 2',
            'points': 100,
            'description': 'Assignment Description 2',
            'due': 'October 18, 2023',
            'due_today': False
        }
    }
}

ASSIGNMENTS_4 = {
    'Course Name 1': {
        'Assignment ID 1': {
            'name': 'Assignment Name 1',
            'points': 50,
            'description': 'Assignment Description 1',
            'due': 'October 17, 2023',
            'due_today': True
        },
        'Assignment ID 2': {
            'name': 'Assignment Name 2',
            'points': 100,
            'description': 'Assignment Description 2',
            'due': 'October 18, 2023',
            'due_today': False
        }
    }
}

# expected messages consts

EXPECTED_SENT_ASSIGNMENTS_1 = [f"**NAME**: Assignment Name 1", f"**POINTS**: 50", f"**DUE**: October 17, 2023"]
EXPECTED_SENT_ASSIGNMENTS_2 = [f"**NAME**: Assignment Name 2", f"**POINTS**: 100", f"**DUE**: October 18, 2023"]
EXPECTED_SENT_ANM_1 = 'Latest Announcement 1'
EXPECTED_SENT_ANM_2 = 'Latest Announcement 2'
EXPECTED_SENT_SECTION_1 = f'**Section 1**'

# course consts

course_0 = {
    'COURSE KEY 1': {},
    'COURSE KEY 2': {}
}

course_1 = {
    'COURSE KEY 1': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {}
    }
}

course_2 = {
    'COURSE KEY 1': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {}
    },
    'COURSE KEY 2': {
        'course_name': '',
        'pending_assignments': {},
        'teacher': '',
        'latest_announcement': '',
        'modules': {}
    }
}

course_3 = {
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
        }
    }
}

course_4 = {
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

course_5 = {
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


assignments_0 = {
    'Course Name 1': {},
    'Course Not Found': {}
}

assignments_1 = {
    'Course Name 1': {
        'Assignment ID 1': {}
    }
}

assignments_2 = {
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

assignments_3 = {
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

assignments_4 = {
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

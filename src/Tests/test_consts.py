# course consts

course_0 = {
    'Course ID 1': {},
    'Course ID 2': {}
}

course_1 = {
    'Course ID 1': {
        'course_name': 'Course Name'
    }
}

course_2 = {
    'Course ID 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {}
    }
}

course_3 = {
    'Course ID 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {
            'Assignment ID 1': {
                'name': 'Assignment Name 1',
                'points': 50,
                'description': 'Assignment Description 1',
                'due': 'October 17, 2023',
                'due_today': False
            }
        }
    }
}

course_4 = {
    'Course ID 1': {
        'course_name': 'Course Name 1',
        'pending_assignments': {
            'Assignment ID 1': {
                'name': 'Assignment Name 1',
                'points': 50,
                'description': 'Assignment Description 1',
                'due': 'October 17, 2023',
                'due_today': True
            }
        }
    },
    'Course ID 2': {
        'course_name': 'Course Name 2',
        'pending_assignments': {
            'Assignment ID 2': {
                'name': 'Assignment Name 2',
                'points': 100,
                'description': 'Assignment Description 2',
                'due': 'October 18, 2023',
                'due_today': False
            }
        }
    }
}

course_5 = {
    'Course ID 1': {
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
        }
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

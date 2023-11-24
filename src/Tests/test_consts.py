# courses cache consts
COURSES_CACHE_1 = ['Course Name 1', 'Course Name 2']

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
                'due_today': True
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
        },
        "original_name": "Course Key 1 | Section 1 | Course Name 1"
    },
    'COURSE KEY 2': {
        'course_name': 'Course Name 2',
        'pending_assignments': {
            'Assignment ID 2': {
                'name': 'Assignment Name 2',
                'points': 100,
                'description': 'Assignment Description 2',
                'due': 'October 18, 2023',
                'due_today': True
            }
        },
        'teacher': 'Teacher 2',
        'latest_announcement': 'Latest Announcement 2',
        'modules': {
            'Module ID 2': {
                'name': 'Module Name 2',
                'items': ['Item 4', 'Item 5', 'Item 6']
            }
        },
        "original_name": "Course Key 2 | Section 2 | Course Name 2"
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
                'due_today': True
            }
        },
        'teacher': 'Teacher 1',
        'latest_announcement': 'Latest Announcement 1',
        'modules': {
            'Module ID 1': {
                'name': 'Module Name 1',
                'items': ['Item 1', 'Item 2', 'Item 3']
            },
            'Module ID 2': {
                'name': 'Module Name 2',
                'items': ['Item 4', 'Item 5', 'Item 6']
            }
        },
    }
}

COURSES_6 = {
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
                'due_today': True
            }
        },
        'teacher': 'Teacher 1',
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
        "original_name": "Course Key 1 | Section 1 | Course Name 1"
    },
    'COURSE KEY 2': {
        'course_name': 'Course Name 2',
        'pending_assignments': {
            'Assignment ID 3': {
                'name': 'Assignment Name 3',
                'points': 150,
                'description': 'Assignment Description 3',
                'due': 'October 19, 2023',
                'due_today': True
            },
            'Assignment ID 4': {
                'name': 'Assignment Name 4',
                'points': 200,
                'description': 'Assignment Description 4',
                'due': 'October 20, 2023',
                'due_today': True
            }
        },
        'teacher': 'Teacher 2',
        'latest_announcement': 'Latest Announcement 2',
        'modules': {
            'Module ID 3': {
                'name': ' Module Name 3',
                'items': ['Item 1', 'Item 2', 'Item 3']
            },
            'Module ID 4': {
                'name': 'Module Name 4',
                'items': ['Item 4', 'Item 5', 'Item 6']
            }
        },
        "original_name": "Course Key 2 | Section 2 | Course Name 2"
    }
}


# assignments consts


ASSIGNMENTS_0 = {
    'Course Not Found': {
        'Assignment ID 1': {
            'name': 'Assignment Name 1',
            'points': 50,
            'description': 'Assignment Description 1',
            'due': 'October 17, 2023',
            'due_today': True
        }
    }
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
            'due_today': True
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
            'due_today': True
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
            'due_today': True
        }
    }
}

ASSIGNMENTS_5 = {
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
            'due_today': True
        }
    },
    'Course Name 2': {
        'Assignment ID 3': {
            'name': 'Assignment Name 3',
            'points': 150,
            'description': 'Assignment Description 3',
            'due': 'October 19, 2023',
            'due_today': True
        },
        'Assignment ID 4': {
            'name': 'Assignment Name 4',
            'points': 200,
            'description': 'Assignment Description 4',
            'due': 'October 20, 2023',
            'due_today': True
        }
    }
}

ASSIGNMENTS_6 = {
    'Course Not Found': {
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
            'due_today': True
        }
    }
}

ASSIGNMENTS_7 = {
    'Course Not Found': {
        'Assignment ID 1': {
            'name': 'Assignment Name 1',
            'points': 50,
            'description': 'Assignment Description 1',
            'due': 'October 17, 2023',
            'due_today': True
        },
    },
    'Course Name 2': {
        'Assignment ID 2': {
            'name': 'Assignment Name 2',
            'points': 100,
            'description': 'Assignment Description 2',
            'due': 'October 18, 2023',
            'due_today': True
        }
    }
}

# ASSIGNMENT CONSTS
ASSIGNMENT_1 = {
    'name': 'Assignment Name 1',
    'points': 50,
    'description': 'Assignment Description 1',
    'due': 'October 17, 2023',
    'due_today': True
}

ASSIGNMENT_2 = {
    'name': 'Assignment Name 2',
    'points': 100,
    'description': 'Assignment Description 2',
    'due': 'October 18, 2023',
    'due_today': True
}

ASSIGNMENT_3 = {
    'name': 'Assignment Name 3',
    'points': 150,
    'description': 'Assignment Description 3',
    'due': 'October 19, 2023',
    'due_today': True
}

ASSIGNMENT_4 = {
    'name': 'Assignment Name 4',
    'points': 200,
    'description': 'Assignment Description 4',
    'due': 'October 20, 2023',
    'due_today': True
}

# MODULES CONSTS

MODULES_1 = {'Module ID 1': 'Module Name 1'}
MODULES_2 = {'Module ID 1': 'Module Name 1',
             'Module ID 2': 'Module Name 2'}

# expected messages consts
EXPECTED_SENT_COURSES_1 = [f'• **Course Name 1**', f'• **Course Name 2**']

EXPECTED_SENT_ASSIGNMENTS_0 = [f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1"]
EXPECTED_SENT_ASSIGNMENTS_1 = [f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1",
                               f"• **Assignment Name 2** \n(Course Name 1). \nID = Assignment ID 2"]
EXPECTED_SENT_ASSIGNMENTS_2 = [f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1",
                               f"• **Assignment Name 2** \n(Course Name 2). \nID = Assignment ID 2"]
EXPECTED_SENT_ASSIGNMENTS_3 = [f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1",
                               f"• **Assignment Name 2** \n(Course Name 1). \nID = Assignment ID 2",
                               f"• **Assignment Name 3** \n(Course Name 2). \nID = Assignment ID 3",
                               f"• **Assignment Name 4** \n(Course Name 2). \nID = Assignment ID 4"]


EXPECTED_SENT_ASSIGNMENT_1 = [f"**NAME**: Assignment Name 1", f"**POINTS**: 50", f"**DUE**: October 17, 2023"]
EXPECTED_SENT_ASSIGNMENT_2 = [f"**NAME**: Assignment Name 2", f"**POINTS**: 100", f"**DUE**: October 18, 2023"]


EXPECTED_SENT_ANM_1 = 'Latest Announcement 1'
EXPECTED_SENT_ANM_2 = 'Latest Announcement 2'
EXPECTED_SENT_SECTION_1 = f'**Section 1**'
EXPECTED_SENT_SECTION_2 = f'**Section 2**'

EXPECTED_SENT_MODULES_0 = [f"• **Module Name 1** \nID = Module ID 1"]
EXPECTED_SENT_MODULES_1 = [f"• **Module Name 1** \nID = Module ID 1",
                           f"• **Module Name 2** \nID = Module ID 2"]

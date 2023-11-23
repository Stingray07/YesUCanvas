import json


def format_data(data):
    print(json.dumps(data, indent=4))

mock = {
    "CCS5": {
        "course_name": "COMPUTER ARCHITECTURE AND ORGANIZATION",
        "course_id": 32713,
        "original_name": "CCS5 | CITCS 2B Group A | COMPUTER ARCHITECTURE AND ORGANIZATION",
        "latest_announcement": "<p>Hello everyone,</p><p>Fulbright Philippines is currently offering the <strong>Global Undergraduate Program</strong>, which allows students to take up a semester of non-degree academic study in the United States, either in August 2024 or January 2025.&nbsp;</p><p>If you are interested, kindly visit the post on the cloud for more details here:<br><a href=\"https://www.facebook.com/groups/theucloud/posts/2347540325434330\" target=\"_blank\">https://www.facebook.com/groups/theucloud/posts/2347540325434330</a></p><div class=\"x1e56ztr\"><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\">You are also invited to attend the Orientation for the Fulbright UGrad Scholarship Program on November 14, 2023 (Tuesday) at 3:00pm, online through Zoom. The meeting details are as follows:</span></div><ul><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Meeting Link:&nbsp;</strong><a class=\"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg\" role=\"link\" href=\"https://us06web.zoom.us/j/87092307914?pwd=i3lJMtZmN0gay17NoxAHzFH81DfM3q.1&amp;fbclid=IwAR2ksUp-Bovf8T85mCuJJVmN8DUtYhFIluIQPHscOWvodi3yc_QWrtZ-J18\" target=\"_blank\">https://us06web.zoom.us/j/87092307914...</a><br></span></em></li><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Meeting ID: </strong>870 9230 7914<br></span></em></li><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Passcode: </strong>482614</span></em></li></ul>",
        "pending_assignments": {
            "465598": {
                "name": "Module 5 - Quiz on Computer Instruction Cycles",
                "points": 30.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4><em><strong>Instructions for this Quiz:</strong></em></h4>\n<ol>\n<li>This is a<span>&nbsp;</span><strong>multiple-choice</strong><span>&nbsp;</span>quiz.</li>\n<li><strong>Read and understand the question and then choose the best answer from the given choices.</strong></li>\n<li><strong>You are only given one attempt for this quiz.</strong><span>&nbsp;</span>Make sure you have selected the correct answers before submitting the quiz.</li>\n</ol>"
            },
            "466568": {
                "name": "Module 6 - Quiz on Computer Arithmetic",
                "points": 50.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4><em><strong>Instructions for this Quiz:</strong></em></h4>\n<ol>\n<li>This is a<span>&nbsp;</span><strong>problem-solving</strong><span>&nbsp;</span>quiz.</li>\n<li><strong>Read and understand each question and solve for the data being asked for.</strong></li>\n<li><strong>Make sure to show your solutions for each question.</strong></li>\n<li><strong>You are only given one attempt for this quiz.</strong><span>&nbsp;</span>Make sure you have selected the correct answers before submitting the quiz.</li>\n</ol>"
            },
            "470773": {
                "name": "Creating your Methodology - CCS5",
                "points": 50.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4><em><strong>Instructions for the Methodology:</strong></em></h4>\n<ul>\n<li><strong>Team Creation</strong>\n<ul>\n<li><strong>You are to work with your research teams that you have form for this subject.</strong><span> Make sure that all members are contributing to your output.</span></li>\n<li><strong>Teams should resolve internal problems on their own when possible.</strong><span>&nbsp;</span>In the event of significant problems regarding team composition in the future, all members shall be asked individually about their opinions on it. Afterwards, a resolution will be given.</li>\n<li><strong>Team members who are not participating in the group activities will be removed from the group and are expected to create an entirely new research output.<span>&nbsp;</span></strong>This individual cannot go to other teams or will not form teams with other students removed from their group.</li>\n</ul>\n</li>\n<li><strong>Writing the Methodology</strong>\n<ul>\n<li><strong>You are going to write the methodology of your paper.&nbsp;</strong>This should include the various key parts that explain the processes involved in comparison and analysis of your chosen algorithms:\n<ul>\n<li><em>Research approach and method</em></li>\n<li><em>Locale and sampling</em></li>\n<li><em>Data gathering instrument</em></li>\n<li><em>Data gathering procedure</em></li>\n<li><em>Data analysis</em></li>\n</ul>\n</li>\n<li><strong>When writing your methodology, focus on the algorithms that you will be analyzing along with their features and the metrics that you will be using to measure their performance. </strong>As mentioned in previous discussions, for CCS5, focus not only on the raw performance of your chosen algorithms, but on their features and characteristics that could affect their usage and implementation. This can include backwards compatibility, ease of implementation, ease of use, hardware support, software support, and other features that might be relevant in the areas that the algorithms are used for.</li>\n<li><strong>Include the references for the methodology. </strong><span>Ensure that you follow the modified APA format for the references and place your reference list at the end of the methodology. </span>You must also follow the in-text citation format of the ACM style.\n<ul>\n<li><span>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum <strong>[1]</strong>.</span></li>\n<li><span><strong>[1] Brunero, S., Cowan, D., and Fairbrother, G. 2015. Reducing emotional distress in nurses using cognitive behavioral therapy: A preliminary program evaluation. Journal of Nursing Science, 5(2), 109-115. doi:10.1080/10723023487216</strong><br></span></li>\n</ul>\n</li>\n<li><strong>Make sure to follow the attached template for your output of this activity.<span>&nbsp;</span></strong><span>Make sure you name the file according to the following format - CCS5_Methodology-Lastname1_Lastname2_Lastname3 (e.g. CCS5_Methodology-Hanbal_Malabanan_Valdez).</span></li>\n</ul>\n</li>\n</ul>"
            }
        },
        "teacher": "Ibrahim Hanbal",
        "module": {
            "245606": {
                "name": "CCS5 Examinations",
                "items": [
                    "CCS5 - Midterm Examination"
                ]
            },
            "230624": {
                "name": "Final Project - Research Paper for CCS5",
                "items": [
                    "Final Project Tasks",
                    "Literature Review - CCS5",
                    "Creating your Introduction - CCS5",
                    "Creating your Methodology - CCS5",
                    "Final Project Resources",
                    "CCS5 - Literature Review Template.docx",
                    "Research Paper Template (ACM).docx",
                    "Parts of a Research Paper (ACM).pdf",
                    "Research Paper Template (ACM) - Introduction.docx",
                    "Research Paper Template (ACM) - Methodology.docx"
                ]
            },
            "225593": {
                "name": "Module 0 - Course Introduction and Overview of CCS5",
                "items": [
                    "Introduction to Course Content",
                    "F2F and ODL Guidelines",
                    "Meeting Schedule and Setup",
                    "Class Rules and Consultations",
                    "Module 0 - Tasks",
                    "Learning Contract - CCS5",
                    "Module 0 - Resources",
                    "0.0 - Course Overview for CCS5 - Computer Architecture and Organization.pdf"
                ]
            },
            "229307": {
                "name": "Module 1 - Fundamentals of Computer Design",
                "items": [
                    "Module 1 - Tasks",
                    "Module 1 - Quiz on the Fundamentals of Computer Design",
                    "Module 1 - Seatwork on Moore's Law",
                    "Module 1 - Resources",
                    "1.0 - Fundamentals of Computer Design.pdf"
                ]
            },
            "235257": {
                "name": "Module 2 - Computer Power and Integrated Circuits",
                "items": [
                    "Module 2 - Tasks",
                    "Module 2 - Quiz on Computer Power and Integrated Circuits",
                    "Extra Activity - Second Year Orientation",
                    "Module 2 - Resources",
                    "2.0 - Computer Power and Integrated Circuits.pdf",
                    "2.0 - Computer Power and Integrated Circuits Quiz - Answer Key.pdf"
                ]
            },
            "237536": {
                "name": "Module 3 - Computer Structure and Function",
                "items": [
                    "Module 3 - Tasks",
                    "Module 3 - Quiz on Computer Structure and Function",
                    "Module 3 - Resources",
                    "3.0 - Computer Structure and Function.pdf"
                ]
            },
            "238029": {
                "name": "Module 4 - Computer Memory",
                "items": [
                    "Module 4 - Tasks",
                    "Module 4 - Quiz on Computer Memory",
                    "Module 4 - Resources",
                    "4.0 - Computer Memory.pdf"
                ]
            },
            "241436": {
                "name": "Module 5 - Computer Instruction Cycles",
                "items": [
                    "Module 5 - Tasks",
                    "Module 5 - Quiz on Computer Instruction Cycles",
                    "Module 5 - Resources",
                    "5.0 - Computer Instruction Cycles.pdf",
                    "CCS5 - Module 5 Video Lecture"
                ]
            },
            "243035": {
                "name": "Module 6 - Computer Arithmetic",
                "items": [
                    "Module 6 - Tasks",
                    "Module 6 - Quiz on Computer Arithmetic",
                    "Module 6 - Resources",
                    "6.0 - Computer Arithmetic.pdf"
                ]
            }
        }
    },
    "CCS2": {
        "course_name": "DESIGN AND ANALYSIS OF ALGORITHM",
        "course_id": 32710,
        "original_name": "CCS2 | CITCS 2B Group A | DESIGN AND ANALYSIS OF ALGORITHM",
        "latest_announcement": "<p>Hello everyone,</p><p>Fulbright Philippines is currently offering the <strong>Global Undergraduate Program</strong>, which allows students to take up a semester of non-degree academic study in the United States, either in August 2024 or January 2025.&nbsp;</p><p>If you are interested, kindly visit the post on the cloud for more details here:<br><a href=\"https://www.facebook.com/groups/theucloud/posts/2347540325434330\" target=\"_blank\">https://www.facebook.com/groups/theucloud/posts/2347540325434330</a></p><div class=\"x1e56ztr\"><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\">You are also invited to attend the Orientation for the Fulbright UGrad Scholarship Program on November 14, 2023 (Tuesday) at 3:00pm, online through Zoom. The meeting details are as follows:</span></div><ul><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Meeting Link:&nbsp;</strong><a class=\"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg\" role=\"link\" href=\"https://us06web.zoom.us/j/87092307914?pwd=i3lJMtZmN0gay17NoxAHzFH81DfM3q.1&amp;fbclid=IwAR2ksUp-Bovf8T85mCuJJVmN8DUtYhFIluIQPHscOWvodi3yc_QWrtZ-J18\" target=\"_blank\">https://us06web.zoom.us/j/87092307914...</a><br></span></em></li><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Meeting ID: </strong>870 9230 7914<br></span></em></li><li class=\"x1e56ztr\"><em><span class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u\"><strong>Passcode: </strong>482614</span></em></li></ul>",
        "pending_assignments": {
            "465600": {
                "name": "Module 5 - Quiz on Analysis of Recursive Algorithms",
                "points": 100.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4><em><strong>Instructions for this Quiz:</strong></em></h4>\n<ol>\n<li>This is a<span>&nbsp;</span><strong>problem-solving</strong><span>&nbsp;</span>quiz.</li>\n<li><strong>Read and understand each question and solve for the data being asked for.</strong></li>\n<li><strong>Make sure to show your solutions for each question.</strong></li>\n<li><strong>You are only given one attempt for this quiz.</strong><span>&nbsp;</span>Make sure you have selected the correct answers before submitting the quiz.</li>\n</ol>"
            },
            "470774": {
                "name": "Creating your Methodology - CCS2",
                "points": 50.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4><em><strong>Instructions for the Methodology:</strong></em></h4>\n<ul>\n<li><strong>Team Creation</strong>\n<ul>\n<li><strong>You are to work with your research teams that you have form for this subject.</strong><span> Make sure that all members are contributing to your output.</span></li>\n<li><strong>Teams should resolve internal problems on their own when possible.</strong><span>&nbsp;</span>In the event of significant problems regarding team composition in the future, all members shall be asked individually about their opinions on it. Afterwards, a resolution will be given.</li>\n<li><strong>Team members who are not participating in the group activities will be removed from the group and are expected to create an entirely new research output.<span>&nbsp;</span></strong>This individual cannot go to other teams or will not form teams with other students removed from their group.</li>\n</ul>\n</li>\n<li><strong>Writing the Methodology</strong>\n<ul>\n<li><strong>You are going to write the methodology of your paper.&nbsp;</strong>This should include the various key parts that explain the processes involved in comparison and analysis of your chosen algorithms:\n<ul>\n<li><em>Research approach and method</em></li>\n<li><em>Locale and sampling</em></li>\n<li><em>Data gathering instrument</em></li>\n<li><em>Data gathering procedure</em></li>\n<li><em>Data analysis</em></li>\n</ul>\n</li>\n<li><strong>When writing your methodology, focus on the algorithms that you will be analyzing along with the metrics that you will be using to understand your chosen algorithm. </strong>As mentioned in previous discussions, for CCS2, focus on the raw performance of your chosen algorithms in different configurations. Do not just test your algorithms using one implementation (such as Java). Make use of different languages (e.g. Java, Python, C++, C#, etc.), data types (e.g. Arrays and Linked Lists), and versions (e.g. Python 2 vs Python 3) to get an in-depth view of the performance of the algorithms.</li>\n<li><strong>Include the references for the methodology. </strong><span>Ensure that you follow the modified APA format for the references and place your reference list at the end of the methodology. </span>You must also follow the in-text citation format of the ACM style.\n<ul>\n<li><span>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum <strong>[1]</strong>.</span></li>\n<li><span><strong>[1] Brunero, S., Cowan, D., and Fairbrother, G. 2015. Reducing emotional distress in nurses using cognitive behavioral therapy: A preliminary program evaluation. Journal of Nursing Science, 5(2), 109-115. doi:10.1080/10723023487216</strong><br></span></li>\n</ul>\n</li>\n<li><strong>Make sure to follow the attached template for your output of this activity.<span>&nbsp;</span></strong><span>Make sure you name the file according to the following format - CCS2_Methodology-Lastname1_Lastname2_Lastname3 (e.g. CCS2_Methodology-Hanbal_Malabanan_Valdez).</span></li>\n</ul>\n</li>\n</ul>"
            }
        },
        "teacher": "Ibrahim Hanbal",
        "module": {
            "245632": {
                "name": "CCS2 - Examinations",
                "items": [
                    "CCS2 - Midterm Examination"
                ]
            },
            "230625": {
                "name": "Final Project - Research Paper for CCS2",
                "items": [
                    "Final Project Tasks",
                    "Literature Review - CCS2",
                    "Creating your Introduction - CCS2",
                    "Creating your Methodology - CCS2",
                    "Final Project Resources",
                    "CCS2 - Literature Review Template.docx",
                    "Research Paper Template (ACM).docx",
                    "Parts of a Research Paper (ACM).pdf",
                    "Research Paper Template (ACM) - Introduction.docx",
                    "Research Paper Template (ACM) - Methodology.docx"
                ]
            },
            "225665": {
                "name": "Module 0 - Course Introduction and Overview of CCS2",
                "items": [
                    "Introduction to Course Content",
                    "F2F and ODL Guidelines",
                    "Meeting Schedule and Setup",
                    "Class Rules and Consultations",
                    "Module 0 - Tasks",
                    "Learning Contract - CCS2",
                    "Module 0 - Resources",
                    "0.0 - Course Overview for CCS2 - Design and Analysis of Algorithm.pdf"
                ]
            },
            "229387": {
                "name": "Module 1 - General Analysis of Algorithms",
                "items": [
                    "Module 1 - Tasks",
                    "Module 1 - Quiz on Time and Space Efficiency",
                    "Module 1 - Resources",
                    "1.0 - General Analysis of Algorithms.pdf",
                    "1.0 - General Analysis of Algorithms Quiz - Answer Key.pdf"
                ]
            },
            "235271": {
                "name": "Module 2 - Order of Growth",
                "items": [
                    "Module 2 - Tasks",
                    "Module 2 - Quiz on Order of Growth",
                    "Bonus Activity - Second Year Orientation",
                    "Module 2 - Resources",
                    "2.0 - Order of Growth.pdf",
                    "2.0 - Order of Growth Quiz - Answer Key.pdf"
                ]
            },
            "238722": {
                "name": "Module 3 - Additional Concepts in Analysis of Algorithms",
                "items": [
                    "Module 3 - Resources",
                    "3.0 - Additional Concepts in Analysis of Algorithms.pdf"
                ]
            },
            "237770": {
                "name": "Module 4 - Analysis of Non-Recursive Algorithms",
                "items": [
                    "Module 4 - Tasks",
                    "Module 4 - Quiz on Analysis of Non-Recursive Algorithms",
                    "Module 4 - Resources",
                    "4.0 - Analysis of Non-Recursive Algorithms.pdf",
                    "4.0 - Analysis of Non-Recursive Algorithms Quiz - Answer Key.pdf"
                ]
            },
            "242522": {
                "name": "Module 5 - Analysis of Recursive Algorithms",
                "items": [
                    "Module 5 - Tasks",
                    "Module 5 - Quiz on Analysis of Recursive Algorithms",
                    "Module 5 - Resources",
                    "5.0 - Analysis of Recursive Algorithms.pdf",
                    "CCS2 - Module 5 Video Lecture"
                ]
            }
        }
    },
    "SOC SCI 101N": {
        "course_name": "ETHICS",
        "course_id": 32785,
        "original_name": "SOC SCI 101N | CITCS 2B Group A | ETHICS",
        "latest_announcement": "<p>Good day class.</p><p>Kindly be reminded that your presentation regarding the film activity will be held tomorrow.</p><p>Please limit each group's presentation to 20 minutes max so we can cover every group within the meeting.</p><p>Thank you.</p>",
        "pending_assignments": {
            "443979": {
                "name": "Activity. R7. (MCQ + Modified T/F)",
                "points": 20.0,
                "due": None,
                "due_today": False,
                "description": "<p style=\"text-align: center;\"><strong>UNIVERSITY OF THE CORDILLERAS</strong><br><span>College of Arts and Sciences</span><br><span>Activity</span></p>\n<p style=\"text-align: center;\"><span><strong>Soc Sci 101N: Ethics<br></strong>Instructor: Brylle Garnet S. Daniel</span></p>\n<p><strong>INSTRUCTIONS:</strong></p>\n<p><strong><u>Honor Code</u></strong><strong>:&nbsp;You are NOT ALLOWED to OPEN other tabs or MINIMIZE your examination page once you have started taking the test. Canvas is logging your activities and your Instructor will be notified each time you leave the site. Any of these two actions will constitute CHEATING and can be used as ground for your scores to be discredited.</strong></p>\n<p><strong>I.&nbsp; MULTIPLE CHOICE.<span>&nbsp;</span><span>&nbsp;</span></strong>Analyze each question and choose the best answer among the given options by clicking your letter-answer.&nbsp;<span><br><strong>II.&nbsp;</strong></span><span><strong>MODIFIED TRUE OR FALSE.&nbsp;</strong>There are two statements listed for your assessment. Evaluate which of the statements are true and which of them are false. Click the letter-answer corresponding to your choice.</span></p>"
            }
        },
        "teacher": "Brylle Garnet Daniel",
        "module": {
            "223069": {
                "name": "Module 0. Course Overview",
                "items": [
                    "SS 101N. Syllabus.docx",
                    "Course Guidelines.docx",
                    "Trimestral Calendar. 1st Trimester SY 2023-2024.png",
                    "Student Orientation On The Use Of Digital Classroom"
                ]
            },
            "229228": {
                "name": "Module 1. Ethics, Relativism, & Egoism (Week 1-3)",
                "items": [
                    "Learning Targets",
                    "Module 1: Learning Outcomes and Performance Indicators-2",
                    "Lessons",
                    "R1. The Challenge of Cultural Relativism.docx",
                    "R2. Ethical Egoism.docx",
                    "Vid Lec -Introduction to Ethics.mp4",
                    "Vid Lec -Relativism and Egoism.mp4",
                    "Learning Task(s)",
                    "Activity R1-R2. (MCQ + Modified T/F)"
                ]
            },
            "229230": {
                "name": "Module 2. Morality, Religion, & The Social Contract (Week 4-5)",
                "items": [
                    "Learning Targets",
                    "Module 2: Learning Outcomes and Performance Indicators-2",
                    "Lessons",
                    "R3. Does Morality Depend on Religion.docx",
                    "R4. The Social Contract.docx",
                    "Vid Lec -Divine Command Theory.mp4",
                    "Vid Lec -Natural Law Theory.mp4",
                    "Vid Lec - The Social Contract.mp4",
                    "Learning Task(s)",
                    "Activity R3-R4. (MCQ + Modified T/F)"
                ]
            },
            "229232": {
                "name": "Module 3. Utilitarianism & Kant  (Week 6-7)",
                "items": [
                    "Learning Targets",
                    "Module 3: Learning Outcomes and Performance Indicators-2",
                    "Lessons",
                    "R5. Utilitarianism.docx",
                    "R6. Kantianism.docx",
                    "Vid Lec -Utilitarianism.mp4",
                    "Vid Lec -Kantianism.mp4",
                    "Learning Task(s)",
                    "Activity R5-R6. (MCQ + Modified T/F)"
                ]
            },
            "229234": {
                "name": "Midterm Examination (Week 8)",
                "items": []
            },
            "229236": {
                "name": "Module 4. Virtue Ethics, Feminism, & The Ideal Moral Theory (Week 9-11)",
                "items": [
                    "Learning Targets",
                    "Module 4: Learning Outcomes and Performance Indicators-2",
                    "Lessons",
                    "R7. Virtue Ethics.docx",
                    "R8. Feminism and the Ethics of Care.docx",
                    "R9. What Would a Satisfactory Moral Theory Be Like.docx",
                    "Learning Task(s)",
                    "Activity. R7. (MCQ + Modified T/F)"
                ]
            },
            "229238": {
                "name": "Module 5. Hypothetical and Contemporary Ethical Issues (Week 12-15)",
                "items": [
                    "Learning Targets",
                    "Module 5: Learning Outcomes and Performance Indicators-2",
                    "Lessons",
                    "Film: Would You Rather",
                    "R10. Applied Ethics - What Is Morality.docx",
                    "R11. Euthanasia.docx",
                    "R12. Death Penalty.docx",
                    "Learning Task(s)"
                ]
            },
            "229225": {
                "name": "Final Examination (Week 16)",
                "items": []
            },
            "228156": {
                "name": "Compilation of Readings & Materials (For Comprehensive Viewing)",
                "items": [
                    "SS101 R1. The Challenge of Cultural Relativism.docx",
                    "SS101 R2. Ethical Egoism.docx",
                    "SS101 R3. Does Morality Depend on Religion.docx",
                    "SS101 R4. The Social Contract.docx",
                    "SS101 R5. Utilitarianism.docx",
                    "SS101 R6. Kantianism.docx",
                    "SS101 R7. Virtue Ethics.docx",
                    "SS101 R8. Feminism and the Ethics of Care.docx",
                    "SS101 R9. What Would a Satisfactory Moral Theory Be Like.docx",
                    "SS101 R10. Applied Ethics - What Is Morality.docx",
                    "SS101 R11. Euthanasia.docx",
                    "SS101 R12. Death Penalty.docx"
                ]
            }
        }
    },
    "CCS12": {
        "course_name": "GRAPHICS DESIGN",
        "course_id": 32705,
        "original_name": "CCS12 | CITCS 2B Group A | GRAPHICS DESIGN",
        "latest_announcement": "<p>Good day everyone,</p><p>Please be informed that I am on official business on November 20 - 23, 2023. As such, a substitute instructor shall be coming in to facilitate your activities:</p><ul><li>Booth mockup layout</li><li>Booth mockup</li></ul><p>As such, you are requested to bring your electronic devices (i.e. laptops, tablets, iPad, etc.) so that you can continue to work on your activities during the 2:10pm - 3:30pm session at U701.</p><p>For your guidance. Please disseminate. Thank you.</p>",
        "pending_assignments": {
            "468445": {
                "name": "Lab Act 5: Booth Mockup",
                "points": 100.0,
                "due": "November 30, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4>Individually or in pairs, create a draft layout of the business / startup at an exhibit.</h4>\n<p><strong>User Story - Booth Mockup</strong></p>\n<ul>\n<li>An owner of a startup / business has been invited to exhibit their company at a Micro, Small, and Medium-Scale Enterprises Exhibit to be held at a convention hall. You were hired to design the booth.</li>\n<li>This exhibit is meant to show the MSMEs of the area. Though, selling products is also allowed.</li>\n<li>You are given a space of 3.5m x 2.5m, with walls at the back and sides. The walls have a height of 2.5m. You are not allowed to remove any of the walls or allowed to expand. You are also requested not to go beyond the space for mobility around the booths.</li>\n</ul>\n<p><strong>Booth Mockup Requirements</strong></p>\n<ul>\n<li>Limit your space to be around 3.5m x 2.5m x 2.5m.</li>\n<li>The following has to be present in the booth:\n<ul>\n<li>Two (2) tarpaulin stands</li>\n<li>Banner at the top of the booth that shows the company's name</li>\n<li>Products and services</li>\n<li>Company information at the walls</li>\n</ul>\n</li>\n<li>You are free to add the following hardware:\n<ul>\n<li>Chairs and tables</li>\n<li>Platforms to showcase your products and services</li>\n<li>Technological requirements (i.e. television, iPad dock, etc.)</li>\n</ul>\n</li>\n<li>Create a 3D model of the booth, complete with all of the graphic design materials and presentation.</li>\n<li>Please take note of the user experience of the booth as well. You are free to choose whether or not customers can enter your booth or not.</li>\n</ul>\n<p><strong>Output and Submission</strong></p>\n<ul>\n<li>Submit three (3) PNG files, that show the following dimensions:\n<ul>\n<li>Front</li>\n<li>3/4 or side</li>\n<li>Top</li>\n</ul>\n</li>\n<li>Make sure that the image is at least 1000px in height.</li>\n<li>Allow one person from your team to submit.</li>\n</ul>"
            },
            "469166": {
                "name": "Lab Act 6: Brand Book",
                "points": 100.0,
                "due": "December 09, 2023 03:59 PM",
                "due_today": False,
                "description": "<h4>Individually or in pairs, compile and improve all activities to develop the brand book for the startup / business (1 item, 100 pts.).</h4>\n<p><strong>About the Brand Book</strong></p>\n<ul>\n<li>The brand book is a comprehensive document of how organizations utilize their branding.</li>\n<li>It shall also serve as a compilation of all of the activities conducted during the course.</li>\n<li>For those with existing organizations, it is a way for your clientele to have a proper turnover with the branding assets.</li>\n</ul>\n<p><strong>Parts of the Brand Book</strong></p>\n<ul>\n<li>About the organization</li>\n<li>Organization logo\n<ul>\n<li>Combination, wordmark, and logotype</li>\n<li>Logo in different arrangements and colors</li>\n<li>Do's and don'ts in arranging and using the logo</li>\n</ul>\n</li>\n<li>Organization assets\n<ul>\n<li>Color scheme</li>\n<li>Fonts</li>\n<li>Icons and shape language</li>\n<li>Images</li>\n</ul>\n</li>\n<li>Graphic design outputs\n<ul>\n<li>Organization brochure</li>\n<li>Calling card</li>\n<li>Company banner</li>\n<li>Tarpaulin stand</li>\n<li>Website assets</li>\n<li>Website design</li>\n<li>Booth mockup photos</li>\n</ul>\n</li>\n</ul>\n<p><strong>Other Requirements</strong></p>\n<ul>\n<li>Please use the template placed here: <a class=\"inline_disabled\" href=\"https://docs.google.com/presentation/d/1j9whU_RYsPByN6VRRU7xE4XGPrQpCp9COdY9OHGAgwg/edit?usp=sharing\" target=\"_blank\">Brand Book Template</a></li>\n<li>Please take a look at other brand books / brand guidelines to see how it can look.</li>\n<li>You are free to change the branding of the slides, but please maintain the content requested.</li>\n</ul>\n<p><strong>Output and Submission</strong></p>\n<ul>\n<li>Submit as a PDF file.</li>\n<li>File name: <em>[TeamName] LabAct6.pdf</em></li>\n<li>Allow one member to submit on behalf of the team.</li>\n</ul>"
            }
        },
        "teacher": "Lovely Jenn Reformado",
        "module": {
            "223389": {
                "name": "Module 0 - Course Introduction and Overview",
                "items": [
                    "About the Course",
                    "Introduction to CCS12 Graphics Design",
                    "Examination Schedule",
                    "Assessment Details",
                    "Course Requirements",
                    "List of Software and Equipment",
                    "List of Required and Supplementary Readings",
                    "Intellectual Property and Use of AI Tools",
                    "Learning Modalities",
                    "Meeting Schedule - Group A",
                    "Guidelines for In-Person Attendance",
                    "Computer Laboratory Use and Guidelines",
                    "Link to Online Distance Learning Classes - CITCS 2B",
                    "Introductory Materials and Activities",
                    "Canvas LMS Walkthrough",
                    "0.1.1: Learning Contract",
                    "CCS12 Course Introduction and Orientation"
                ]
            },
            "226658": {
                "name": "Module 1 - Introduction to Graphics Design",
                "items": [
                    "1. Introduction to Graphics Design",
                    "1.1.1: Introduction to Graphics Design",
                    "1.1.2: Elements of Graphics Design",
                    "1.1.3: Principles of Graphics Design",
                    "1.1.4: Unit 1 Quiz",
                    "2. Establishment of Business / Startup",
                    "1.2.1: Creation of Teams",
                    "1.2.2: Establishment of Business / Startup",
                    "1.2.3: Commitment Letter Template"
                ]
            },
            "232116": {
                "name": "Module 2 - Introduction to Branding",
                "items": [
                    "1. Introduction to Branding",
                    "2.1.1: Introduction to Branding",
                    "2.1.2: IP Protection for Graphic Artists",
                    "2.1.3: Unit 2 Quiz",
                    "2. Branding Resources",
                    "2.2.1: Sample Output for Lab Act 1: Brand Book"
                ]
            },
            "233172": {
                "name": "Module 3 - Logo Design",
                "items": [
                    "1. Introduction to Logo Design",
                    "3.1.1: Introduction to Logo Design",
                    "3.1.2: Initial Logo Design",
                    "2. Logo Design Resources",
                    "3.2.1: Creating a Good Logo",
                    "3.2.2: Additional Logo Design Tips",
                    "3.2.3: Case Study: AirBNB Logo Redesign"
                ]
            },
            "236680": {
                "name": "Module 4: The Graphic Design Environment",
                "items": [
                    "1. The Graphic Design Environment",
                    "4.1.1: Introduction to the Graphic Design Environment",
                    "4.1.2: Unit 4 Quiz",
                    "2. Tutorials on Graphic Design Environments",
                    "4.2.1: Introduction to Adobe Illustrator",
                    "4.2.2: Introduction to Adobe Photoshop",
                    "4.2.3: Pen Tool in Adobe Illustrator",
                    "4.2.4: Case Study: Sketch to Vector Logo",
                    "3. Additional Resources",
                    "4.3.1: Photopea Link (Adobe Photoshop Alternate)"
                ]
            },
            "238402": {
                "name": "Module 5: Printed Materials",
                "items": [
                    "1. Printed Materials",
                    "5.1.1: Printed Materials",
                    "5.1.2: Organization Calling Card",
                    "2. Miscellaneous",
                    "5.2.1: Midterm Examination Guidelines"
                ]
            },
            "232119": {
                "name": "Laboratory Activities - Midterms",
                "items": [
                    "Lab Act 1: Brand Book",
                    "Lab Act 2: Final Organization Logo",
                    "Lab Act 3: Organization Brochure"
                ]
            },
            "239877": {
                "name": "Midterm Examination (October 18, 2023)",
                "items": [
                    "CCS12 Midterm Examination - Part 1",
                    "CCS12 Midterm Examination - Part 2",
                    "CCS12 Midterm Grades - CITCS 2B"
                ]
            },
            "241679": {
                "name": "Module 6: Digital Materials",
                "items": [
                    "1. Digital Materials",
                    "6.1.1: Introduction to Digital Materials",
                    "6.1.2: Introduction to UI/UX Design",
                    "6.1.3: Introduction to Website Design",
                    "2. Class Standing",
                    "6.2.1: Website Content",
                    "6.2.2: Website Assets"
                ]
            },
            "244258": {
                "name": "Module 7: Product Packaging Design",
                "items": [
                    "1. Introduction to Product Packaging Design",
                    "7.1.1: Introduction to Product Packaging Design",
                    "2. Other Resources",
                    "7.2.1: SketchUp for Web",
                    "7.2.2: SketchUp Guide Video",
                    "3. Class Standing",
                    "7.3.1: Graphic Design Textures",
                    "7.3.2: Booth Mockup Layout"
                ]
            }
        }
    },
    "CC5": {
        "course_name": "INFORMATION MANAGEMENT",
        "course_id": 32687,
        "original_name": "CC5 | CITCS 2B Group A | INFORMATION MANAGEMENT",
        "latest_announcement": "Good morning everyone!<div><br></div><div>Cheerleading competition will start by 10 so I am requiring everyone to please support our cheerleaders. Attach here a video of yourself/yourselves at uc gym then show any cheerleading performance for attendance. 15 seconds minimum will do. If by group, comment your names on the attached video.&nbsp;</div><div><br></div><div>See you on Saturday!</div>",
        "pending_assignments": {
            "472906": {
                "name": "6.3 - Employee_Job",
                "points": 50.0,
                "due": "November 25, 2023 03:59 PM",
                "due_today": False,
                "description": "<p><img src=\"https://uc-bcf.instructure.com/courses/32687/files/6664225/preview?verifier=AvxGYFxCSPMhOXC8GVua6XGO0GNwvOe6qj2vkVG6\" alt=\"image.png\" width=\"628\" height=\"353\" data-api-endpoint=\"https://uc-bcf.instructure.com/api/v1/courses/32687/files/6664225\" data-api-returntype=\"File\"> &nbsp;</p>\n<p><img src=\"https://uc-bcf.instructure.com/courses/32687/files/6664226/preview?verifier=LbTTUHu9Ae8t5qglNhp06asbS76ijYKKUyTfpZN5\" alt=\"image.png\" width=\"623\" height=\"334\" data-api-endpoint=\"https://uc-bcf.instructure.com/api/v1/courses/32687/files/6664226\" data-api-returntype=\"File\"></p>\n<p>&nbsp;</p>\n<p>With the above 2NF, using xampp, create the database with the given records and reference the appropriate foreign keys.</p>\n<p>For checking, i<span>nclude screenshots of codes and outputs. Do not screenshot the whole screen, just the code and output. Use ALIAS/AS. Submit in PDF.</span></p>\n<p>1-3. <span>Perform a query to show each table.&nbsp;</span></p>\n<p><span>4. Perform a query to show the employee_id, employee_name and home_state.</span></p>\n<p><span>5. Perform a query to show the employee_id, employee_name and job.</span></p>\n<p><span>6. Perform a query to show all records just as the second image above. Hint: You can use join command multiple time. For example:</span></p>\n<p><span class=\"kwd\">SELECT</span><span class=\"pln\"> column-names</span></p>\n<p><span class=\"kwd\">FROM</span><span class=\"pln\"> table1-name</span></p>\n<p><span class=\"kwd\">JOIN</span><span class=\"pln\"> table2-name </span><span class=\"kwd\">ON</span><span class=\"pln\"> column-name1 </span><span class=\"pun\">=</span><span class=\"pln\"> column-name2</span></p>\n<p><span class=\"kwd\">JOIN</span><span class=\"pln\"> table3-name </span><span class=\"kwd\">ON</span><span class=\"pln\"> column-name3 </span><span class=\"pun\">=</span><span class=\"pln\"> column-name4</span></p>\n<p><span class=\"kwd\">WHERE</span><span class=\"pln\"> condition;</span></p>\n<p>&nbsp;</p>"
            }
        },
        "teacher": "Charity Chinalpan",
        "module": {
            "228808": {
                "name": "Module 0 - Course Introduction",
                "items": [
                    "Roll Call Attendance",
                    "Schedule of Classes",
                    "First Trimester Calendar",
                    "Canvas LMS Walk-through"
                ]
            },
            "228809": {
                "name": "Module 1: Data and Information",
                "items": [
                    "Module 1 - Resources",
                    "1.1-Data and Information.pdf",
                    "Module 1 - Tasks",
                    "1.1-Entities Exercise",
                    "1.2 - Information Management"
                ]
            },
            "231160": {
                "name": "Module 2: Introduction to Data Modelling",
                "items": [
                    "Module 2 - Resources",
                    "2.1 - Entities and Attributes.pdf",
                    "2.2 - Data Modelling",
                    "2.3 - Recorded Lecture for Entity Relationships",
                    "Module 2 - Tasks",
                    "2.1 - Designing an ERD for Facebook Using Barker's Notation",
                    "2.2 - Facebook Entity Relationships",
                    "2.3 - Entity Relationship Diagram",
                    "2.4 - Multiple Relationships",
                    "Questions and Concerns?"
                ]
            },
            "233876": {
                "name": "Module 3: Introduction to ERDish",
                "items": [
                    "Module 3 - Resources",
                    "3.1-Relationships and ERD's.pdf",
                    "Module 3 - Tasks",
                    "3.1 - ERDish",
                    "3.2 - Credit Card Processes",
                    "3.3 - Student-Course Relationship",
                    "3.4 - Creating a Table"
                ]
            },
            "235993": {
                "name": "Module 4 - Super types, Sub types and Business ",
                "items": [
                    "Module 4 - Resources",
                    "4.1-Super types, Sub types and Business Rules.pdf",
                    "Module 4 - Tasks",
                    "On Paper - Creating subtype and supertype",
                    "On Paper - Unique vs Primary Keys"
                ]
            },
            "236526": {
                "name": "Midterm Laboratory",
                "items": [
                    "Resources",
                    "1.1-Basic SQL.pdf",
                    "2.1 -Creating Tables.pdf",
                    "Tasks",
                    "1.1-Basic SQL Exercise",
                    "2.1- Creating Tables using Live SQL",
                    "2.2 - Creating Table using Live SQL2",
                    "3.1-Midterm Project",
                    "1 - 3 . Quiz"
                ]
            },
            "234669": {
                "name": "Midterm Exam - October 17",
                "items": [
                    "CC5 Midterm Exam "
                ]
            },
            "242616": {
                "name": "Module 5 - Transferability",
                "items": [
                    "Resources",
                    "5.1-Transferability.pdf",
                    "Tasks",
                    "5.1 Sequence",
                    "5.2 - ERD",
                    "5.3 - Cardinality and Transferability",
                    "5.4 - CRUD Example"
                ]
            },
            "245964": {
                "name": "Module 6 - Normalization",
                "items": [
                    "Resources",
                    "6.1 - Creating Joint Table Recorded Lecture",
                    "6.2 - Normalization.pptx",
                    "6.3 - Normalization.pdf",
                    "Tasks",
                    "6.1 - Creating Relationship",
                    "6.2 - 3NF(Third Normal Form)",
                    "6.3 - Employee_Job"
                ]
            }
        }
    },
    "PE 4N": {
        "course_name": "PE",
        "course_id": 32769,
        "original_name": "PE 4N | CITCS 2B Group A | PHYSICAL EDUCATION 4",
        "latest_announcement": "<p>Same instruction, 8-9 members per group. 1 will upload the video ( your output). Dont forget to include the names of those who participated.</p><p>For the fun run. Please make sure to get your race bib and submit your waivers.</p><p>You should be at the lake drive at 530 am on saturday. See you!&nbsp;</p><p>Thank you. \u263a\ufe0f</p>",
        "pending_assignments": {
            "471911": {
                "name": "APPLICATION M9",
                "points": 40.0,
                "due": "November 22, 2023 03:59 PM",
                "due_today": False,
                "description": "<ul>\n<li>\n<span>Practice and familiarize yourselves on the proper execution of each exercise included in the&nbsp;</span>Tabata.</li>\n<li><span>Perform these exercises below following the pattern of 20 seconds exercise and 10 seconds rest.</span></li>\n<li><span class=\"OYPEnA text-decoration-none text-strikethrough-none\">Do the activity with precaution, careful not to incur any injury.</span></li>\n<li><span class=\"OYPEnA text-decoration-none text-strikethrough-none\">Take a video of yourself performing a complete set of exercises.</span></li>\n<li><span class=\"OYPEnA text-decoration-none text-strikethrough-none\">Do necessary edits on the video you took to make it more interesting.</span></li>\n<li><span class=\"OYPEnA text-decoration-none text-strikethrough-none\">After finishing the video, send it to the platform given by your teacher.</span></li>\n</ul>\n<p>&nbsp;</p>\n<p style=\"text-align: center;\"><iframe title=\"4-Minute Fat Burning Workout | Tabata for Beginners\" src=\"https://www.youtube.com/embed/aUYRVSNz_VY\" width=\"1000\" height=\"700\" allowfullscreen=\"allowfullscreen\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\"></iframe></p>"
            }
        },
        "teacher": "Hector Cajigan",
        "module": {
            "229002": {
                "name": "Module 0/Preliminaries: Course Information / Orientation",
                "items": [
                    "COURSE DESCRIPTION and OUTCOMES",
                    "Course Outline: MIDTERM (CHESS)",
                    "Academic Honor Pledge",
                    "Midterm Exam Week Schedule (Oct. 16 - Oct. 19, 2023)"
                ]
            },
            "229003": {
                "name": "MODULE 1 INTRODUCTION TO RECREATION ACTIVITIES",
                "items": [
                    "INTENDED LEARNING OBJECTIVES",
                    "ACTIVATE PRIOR KNOWLEDGE: QUIZ M1 ",
                    "ACQUIRING KNOWLEDGE",
                    "CONCEPT OF RECREATION.pdf",
                    "BRIEF HISTORY OF RECREATION.pdf",
                    "TYPES OF RECREATIONAL ACTIVITIES",
                    "ACTIVITY",
                    "APPLICATION",
                    "ANALYSIS"
                ]
            },
            "233137": {
                "name": "MODULE 2: Understanding OUTDOOR and ADVENTURE ACTIVITIES",
                "items": [
                    "INTENDED LEARNING OBJECTIVES-2",
                    "ACQUIRING KNOWLEDGE-2",
                    "Examples of Outdoor Activities in the Philippines.docx",
                    "ACTIVITY 2: Community Exploration Outdoor Activity ",
                    "APPLICATION: Beautiful Outdoor Activities",
                    "REFERENCES"
                ]
            },
            "234675": {
                "name": "Module 3: Outdoor Recreation (Knot tying)",
                "items": [
                    "Intended Learning Outcome",
                    "ACQUIRING KNOWLEDGE",
                    "Module 3 KNOT TYING.pdf",
                    "Module-3-Knot-Tying Types and Classification.pdf",
                    "M3 Acquire new knowledge",
                    "Knot Tying Demo Pics.docx",
                    "Application Module 3"
                ]
            },
            "236022": {
                "name": "WEEK 4: MODULE 4 - Family: Recreational Activity ",
                "items": [
                    "ILO M4",
                    "Activate Prior Knowledge M4",
                    "Acquire New Knowledge M4",
                    "Assessment M4",
                    "Application M4"
                ]
            },
            "238933": {
                "name": "Module 5: Team Building Activities",
                "items": [
                    "ILO m5",
                    "ACQUIRING KNOWLEDGE M5"
                ]
            },
            "242558": {
                "name": "Module 6: Running",
                "items": [
                    "Activate Prior Knowledge M6",
                    "ILO M6",
                    "Acquire new knowledge m6",
                    "Application M6"
                ]
            },
            "243924": {
                "name": "Module 7: Track events in Athletics",
                "items": [
                    "ILO M7",
                    "Acquire New Knowledge M7"
                ]
            },
            "244932": {
                "name": "Module 8 Road Running Events",
                "items": [
                    "Activate Prior Knowledge M8",
                    "ILO m8",
                    "Acquiring New Knowledge M8",
                    "Application M8"
                ]
            },
            "246184": {
                "name": "M9: Other forms of competitive running",
                "items": [
                    "Acquire New Knowledge M9",
                    "ILO M9",
                    "APPLICATION M9"
                ]
            }
        }
    },
    "CC24": {
        "course_name": "PROBABILITY THEORY",
        "course_id": 32684,
        "original_name": "CC24 | CITCS 2B Group A | PROBABILITY THEORY",
        "latest_announcement": "For our class,<br>You may go to the gym to watch the openning of the Intramurals and support CITCS.<br><br>\ud83e\udd16 \ud83d\udc7d \ud83d\udda5\ufe0f GO CITCS \ud83d\udda5\ufe0f \ud83d\udc7d \ud83e\udd16",
        "pending_assignments": {},
        "teacher": "Zen Lee Foryasen",
        "module": {}
    }
}

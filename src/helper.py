import json


def format_data(data):
    print(json.dumps(data, indent=4))

mock = {
    "CCS5": {
        "course_name": "COMPUTER ARCHITECTURE AND ORGANIZATION",
        "course_id": 32713,
        "original_name": "CCS5 | CITCS 2B Group A | COMPUTER ARCHITECTURE AND ORGANIZATION",
        "latest_announcement": "<p>Good day everyone,</p><p>I will not be able to attend our meeting later today as I am currently on leave for the next few days due to an event. I have posted instructions for an activity for this week under the <strong>Final Project module</strong> that you will be completing as a group for this week. You are to start <strong>writing the introduction </strong>for your research paper output. This will cover the <strong>Review of Related Literature (RRL) </strong>and the <strong>objectives of your paper</strong>. Please make sure that you work on the introduction with your groupmates so that you will lay the foundation for the basis of your study.</p><p>For CCS5, focus on the <strong>algorithm(s) that you will be analyzing and their performance metrics, as well as how these algorithms are used in real world contexts</strong>, such as what type of systems or applications are they best suited for. Make sure that you are set with your chosen performance metrics, and you are able to test the algorithms using these metrics on your own. <strong>You should be able to simulate, compute, or implement your chosen performance metrics in analyzing your chosen algorithms.</strong></p>",
        "pending_assignments": {
            "463898": {
                "name": "Creating your Introduction - CCS5",
                "points": 50.0,
                "description": "<h4><em><strong>Instructions for the Introduction:</strong></em></h4>\n<ul>\n<li><strong>Team Creation</strong>\n<ul>\n<li><strong>You are to work with your research teams that you have form for this subject.</strong><span> Make sure that all members are contributing to your output.</span></li>\n<li><strong>Teams should resolve internal problems on their own when possible.</strong><span>&nbsp;</span>In the event of significant problems regarding team composition in the future, all members shall be asked individually about their opinions on it. Afterwards, a resolution will be given.</li>\n<li><strong>Team members who are not participating in the group activities will be removed from the group and are expected to create an entirely new research output.<span>&nbsp;</span></strong>This individual cannot go to other teams or will not form teams with other students removed from their group.</li>\n</ul>\n</li>\n<li><strong>Data Gathering</strong>\n<ul>\n<li><strong>You are to create the introduction for your paper.&nbsp;</strong>This should include the key parts of the introduction, listed below:\n<ul>\n<li>Background of the study<br>\n<ul>\n<li><i>Introduction of the topic</i></li>\n<li><i>Research gaps</i></li>\n<li><i>Current body of knowledge</i></li>\n<li><i>How the study differs from other researches</i></li>\n</ul>\n</li>\n<li>Objectives<br>\n<ul>\n<li><em>General objectives</em></li>\n<li><em>Specific objectives</em></li>\n</ul>\n</li>\n<li>Significance of the study</li>\n</ul>\n</li>\n<li><strong>Include the references for the introduction. </strong><span>Ensure that you follow the modified APA format for the references and place your reference list at the end of the introduction</span>. You must also follow the in-text citation format of the ACM style.\n<ul>\n<li><span>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum <strong>[1]</strong>.</span></li>\n<li><span><strong>[1] Brunero, S., Cowan, D., and Fairbrother, G. 2015. Reducing emotional distress in nurses using cognitive behavioral therapy: A preliminary program evaluation. Journal of Nursing Science, 5(2), 109-115. doi:10.1080/10723023487216</strong><br></span></li>\n</ul>\n</li>\n<li><strong>Make sure to follow the attached template for your output of this activity.<span>&nbsp;</span></strong><span>Make sure you name the file according to the following format - CCS5_Introduction-Lastname1_Lastname2_Lastname3 (e.g. CCS5_Introduction-Hanbal_Malabanan_Valdez).</span></li>\n</ul>\n</li>\n</ul>",
                "due": "November 04, 2023 03:59 PM",
                "due_today": False
            },
            "465598": {
                "name": "Module 5 - Quiz on Computer Instruction Cycles",
                "points": 30.0,
                "description": "<h4><em><strong>Instructions for this Quiz:</strong></em></h4>\n<ol>\n<li>This is a<span>&nbsp;</span><strong>multiple-choice</strong><span>&nbsp;</span>quiz.</li>\n<li><strong>Read and understand the question and then choose the best answer from the given choices.</strong></li>\n<li><strong>You are only given one attempt for this quiz.</strong><span>&nbsp;</span>Make sure you have selected the correct answers before submitting the quiz.</li>\n</ol>",
                "due": "November 18, 2023 03:59 PM",
                "due_today": False
            }
        },
        "teacher": "Ibrahim Hanbal",

        "module": {
            "230624": {
                "name": "Final Project - Research Paper for CCS5",
                "items": [
                    "Final Project Tasks",
                    "Literature Review - CCS5",
                    "Creating your Introduction - CCS5",
                    "Final Project Resources",
                    "CCS5 - Literature Review Template.docx",
                    "Research Paper Template (ACM).docx",
                    "Parts of a Research Paper (ACM).pdf",
                    "Research Paper Template (ACM) - Introduction.docx"
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
        "latest_announcement": "<p>Good day everyone,</p><p>I will not be able to attend our meeting later today as I am currently on leave for the next few days due to an event. I have posted instructions for an activity for this week under the <strong>Final Project module</strong> that you will be completing as a group for this week. You are to start <strong>writing the introduction </strong>for your research paper output. This will cover the <strong>Review of Related Literature (RRL) </strong>and the <strong>objectives of your paper</strong>. Please make sure that you work on the introduction with your groupmates so that you will lay the foundation for the basis of your study.</p><p>For CCS2, focus on the <strong>algorithm(s) that you will be analyzing and their performance metrics, as well as different comparisons of their performance metrics in different scenarios</strong>, such as when the algorithm is implemented in one programming language compared to another programming language. You can check the possible avenues of comparing the performance of an algorithm by checking the slides in Module 3. <strong>Make sure that you are able to utilize your chosen performance metrics in order to analyze the performance of your chosen algorithms.</strong></p>",
        "pending_assignments": {
            "463899": {
                "name": "Creating your Introduction - CCS2",
                "points": 50.0,
                "description": "<h4><em><strong>Instructions for the Introduction:</strong></em></h4>\n<ul>\n<li><strong>Team Creation</strong>\n<ul>\n<li><strong>You are to work with your research teams that you have form for this subject.</strong><span> Make sure that all members are contributing to your output.</span></li>\n<li><strong>Teams should resolve internal problems on their own when possible.</strong><span>&nbsp;</span>In the event of significant problems regarding team composition in the future, all members shall be asked individually about their opinions on it. Afterwards, a resolution will be given.</li>\n<li><strong>Team members who are not participating in the group activities will be removed from the group and are expected to create an entirely new research output.<span>&nbsp;</span></strong>This individual cannot go to other teams or will not form teams with other students removed from their group.</li>\n</ul>\n</li>\n<li><strong>Writing the Introduction</strong>\n<ul>\n<li><strong>You are to choose a minimum of two (2) algorithms to focus on for your study.&nbsp;</strong>Take note that for the two algorithms chosen, you will be doing an in-depth analysis of the features, characteristics, and performance of the chosen algorithms, focusing on the performance of the chosen algorithms. Make sure to not only compare the raw performance of the algorithms (e.g. time and space efficiency) but also the performance of the algorithms in different contexts (e.g. time efficiency in Java compared to Python).</li>\n<li><strong>You are to create the introduction for your paper.&nbsp;</strong>This should include the key parts of the introduction, listed below:\n<ul>\n<li>Background of the study<br>\n<ul>\n<li><i>Introduction of the topic</i></li>\n<li><i>Research gaps</i></li>\n<li><i>Current body of knowledge</i></li>\n<li><i>How the study differs from other researches</i></li>\n</ul>\n</li>\n<li>Objectives<br>\n<ul>\n<li><em>General objectives</em></li>\n<li><em>Specific objectives</em></li>\n</ul>\n</li>\n<li>Significance of the study</li>\n</ul>\n</li>\n<li><strong><span>When writing your introduction, focus on the </span>algorithm(s) that you will be analyzing and their performance metrics, as well as different comparisons of their performance metrics in different scenarios<span>, such as when the algorithm is implemented in one programming language compared to another programming language. </span></strong>You can check the possible avenues of comparing the performance of an algorithm by checking the slides in Module 3.&nbsp;Make sure that you are able to utilize your chosen performance metrics in order to analyze the performance of your chosen algorithms.</li>\n<li><strong>Include the references for the introduction. </strong><span>Ensure that you follow the modified APA format for the references and place your reference list at the end of the introduction</span>. You must also follow the in-text citation format of the ACM style.\n<ul>\n<li><span>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum <strong>[1]</strong>.</span></li>\n<li><span><strong>[1] Brunero, S., Cowan, D., and Fairbrother, G. 2015. Reducing emotional distress in nurses using cognitive behavioral therapy: A preliminary program evaluation. Journal of Nursing Science, 5(2), 109-115. doi:10.1080/10723023487216</strong><br></span></li>\n</ul>\n</li>\n<li><strong>Make sure to follow the attached template for your output of this activity.<span>&nbsp;</span></strong><span>Make sure you name the file according to the following format - CCS2_Introduction-Lastname1_Lastname2_Lastname3 (e.g. CCS2_Introduction-Hanbal_Malabanan_Valdez).</span></li>\n</ul>\n</li>\n</ul>",
                "due": "November 04, 2023 03:59 PM",
                "due_today": False
            },
            "465600": {
                "name": "Module 5 - Quiz on Analysis of Recursive Algorithms",
                "points": 100.0,
                "description": "<h4><em><strong>Instructions for this Quiz:</strong></em></h4>\n<ol>\n<li>This is a<span>&nbsp;</span><strong>problem-solving</strong><span>&nbsp;</span>quiz.</li>\n<li><strong>Read and understand each question and solve for the data being asked for.</strong></li>\n<li><strong>Make sure to show your solutions for each question.</strong></li>\n<li><strong>You are only given one attempt for this quiz.</strong><span>&nbsp;</span>Make sure you have selected the correct answers before submitting the quiz.</li>\n</ol>",
                "due": "November 18, 2023 03:59 PM",
                "due_today": False
            }
        },
        "teacher": "Ibrahim Hanbal",
        "module": {
            "230625": {
                "name": "Final Project - Research Paper for CCS2",
                "items": [
                    "Final Project Tasks",
                    "Literature Review - CCS2",
                    "Creating your Introduction - CCS2",
                    "Final Project Resources",
                    "CCS2 - Literature Review Template.docx",
                    "Research Paper Template (ACM).docx",
                    "Parts of a Research Paper (ACM).pdf",
                    "Research Paper Template (ACM) - Introduction.docx"
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
        "latest_announcement": "<p>Good morning class.</p><p>We conduct our class today asynchronously. Everyone is instructed to watch the film Would You Rather. It is available under module 5.</p><p>Note of the ethical dilemmas presented in the film in relation to all the moral theories we have previously discussed. An activity will be given next week about the film.&nbsp;</p><p>The members of Reading 9 will be reciting this coming Monday (Nov. 6, 2023), so please be ready.</p><p>Thank you.</p>",
        "pending_assignments": {},
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
                    "Learning Task(s)"
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
        "latest_announcement": "",
        "pending_assignments": {},
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
            "241684": {
                "name": "Laboratory Activities - Finals",
                "items": [
                    "Lab Act 4: Organization Website"
                ]
            }
        }
    },
    "CC5": {
        "course_name": "INFORMATION MANAGEMENT",
        "course_id": 32687,
        "original_name": "CC5 | CITCS 2B Group A | INFORMATION MANAGEMENT",
        "latest_announcement": "Face to face quiz shall start by 10:15. Please dont be late.",
        "pending_assignments": {},
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
                    "Tasks"
                ]
            }
        }
    },
    "PE 4N": {
        "course_name": "PE",
        "course_id": 32769,
        "original_name": "PE 4N | CITCS 2B Group A | PHYSICAL EDUCATION 4",
        "latest_announcement": "<p>Good morming everyone! Please be in your proper attire today. Mode of Learning will be F2F. See you! \u263a\ufe0f</p>",
        "pending_assignments": {},
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
            }
        }
    },
    "CC24": {
        "course_name": "PROBABILITY THEORY",
        "course_id": 32684,
        "original_name": "CC24 | CITCS 2B Group A | PROBABILITY THEORY",
        "latest_announcement": "",
        "pending_assignments": {},
        "teacher": "Zen Lee Foryasen",
        "module": {}
    }
}

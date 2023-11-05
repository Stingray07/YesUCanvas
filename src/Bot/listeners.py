from src.Canvas.consts import help_message
from src.Canvas import course_functions as cf
from html2text import html2text
from src.helper import format_data


async def listen_to_help(message):
    if message.content.startswith('!help'):
        await message.channel.typing()
        await message.channel.send(help_message)


async def listen_to_courses(message, courses, cache):
    if message.content.startswith('!courses'):
        await message.channel.typing()
        if not cache:
            all_courses = cf.get_all_course_names(courses=courses)
            for course in all_courses:
                cache.append(course)
            print('Cached Courses from courses listener')

        for course in cache:
            await message.channel.typing()
            await message.channel.send(course)

    return cache


async def listen_to_assignments(message, courses, cache):
    if message.content.startswith('!all_assignments'):
        await message.channel.typing()
        if not cache:
            cache = cf.get_all_pending_assignments(courses=courses)
            print('Cached Assignments from assignments listener')
            format_data(cache)

        await send_assignments_messages(message=message, pending_assignments=cache)

    return cache


async def listen_to_assignment(message, cache):
    if message.content.startswith('!asm '):
        await message.channel.typing()
        assignment_id = message.content[5:]
        assignment = cf.get_assignment(assignments=cache, assignment_id=assignment_id)

        print(assignment_id)
        format_data(cache)

        for key, value in assignment['assignment_id']:
            await message.channel.typing()
            message_str = f"{key} = {value}"
            await message.channel.send(message_str)


async def listen_to_teacher(message, courses):
    if message.content.startswith('!teacher '):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        teacher = cf.get_teacher(courses=courses, course_key=course_key)

        if not teacher:
            message_str = "Course Not Found"
        else:
            message_str = f"{teacher}"

        await message.channel.send(message_str)


async def listen_to_announcement(message, courses):
    if message.content.startswith('!anm '):
        await message.channel.typing()
        course_key = message.content[5:].upper()
        announcement = cf.get_announcement(courses=courses, course_key=course_key)

        if not announcement:
            message_str = "Course Not Found"
        else:
            announcement = html2text(announcement)
            message_str = f"{announcement}"

        await message.channel.send(message_str)


async def listen_to_section(message, courses):
    if message.content.startswith('!section '):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        section = cf.get_section(courses=courses, course_key=course_key)

        if not section:
            message_str = "Section Not Found"
        else:
            message_str = f"{section}"

        await message.channel.send(message_str)


async def listen_to_due_today(message, pending_assignments, courses, cache):
    if message.content.startswith('!due_today'):
        await message.channel.typing()

        if not pending_assignments:
            pending_assignments = cf.get_all_pending_assignments(courses=courses)
            print("Cached Assignments from due_today listener")
            format_data(pending_assignments)

        if not cache:
            cache = cf.get_all_due_today(pending_assignments)
            print('Cached Due Today from due_today listener')
            if not cache:
                await message.channel.send('No Due Today')
                return

        format_data(cache)
        for assignment in cache:
            await message.channel.typing()
            message_str = f"• {cache[assignment]['name']}. ID = {assignment}"
            await message.channel.send(message_str)

    return cache


async def send_assignments_messages(message, pending_assignments):
    for course, assignments in pending_assignments.items():
        await message.channel.typing()
        for assignment_id, assignment_info in assignments.items():
            message_str = f"• **{assignment_info['name']}** \n({course}). \nID = {assignment_id}"
            await message.channel.send(message_str)

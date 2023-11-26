import discord

from src.Canvas import consts as const
from src.Canvas import course_functions as cf
from html2text import html2text
from src.helper import format_data


async def listen_to_help(message):
    if message.content == const.HELP_COMMAND_PREFIX:
        await message.channel.typing()
        await message.channel.send(const.HELP_MESSAGE)


async def listen_to_courses(message, courses, cache):
    if message.content == const.COURSES_COMMAND_PREFIX:
        await message.channel.typing()

        if not courses:
            await message.channel.send('COURSES NOT FOUND')
            return cache
        if not cache:
            all_courses = cf.get_all_course_names(courses=courses)
            for course in all_courses:
                cache.append(course)
            print('Cached Courses from courses listener')

        for course in cache:
            await message.channel.typing()
            await message.channel.send(f"• **{course}**")

    return cache


async def listen_to_assignments(message, courses, cache):
    if message.content == const.ASSIGNMENTS_COMMAND_PREFIX:
        await message.channel.typing()
        if not cache:
            cache = cf.get_all_pending_assignments(courses=courses)
            print('Cached Assignments from assignments listener')

        await send_assignments_messages(message=message, pending_assignments=cache)

    return cache


async def listen_to_assignment(message, courses, cache):
    if message.content.startswith(const.ASSIGNMENT_COMMAND_PREFIX):
        format_data(cache)
        await message.channel.typing()
        if not cache:
            cache = cf.get_all_pending_assignments(courses=courses)

        assignment_id = message.content[5:].strip()
        assignment = cf.get_assignment(assignments=cache, assignment_id=assignment_id)
        description = None

        if not assignment:
            await message.channel.send('ID NOT FOUND')
            return cache

        for key, value in assignment.items():
            await message.channel.typing()
            if key not in ['description', 'due_today']:
                await message.channel.send(f"**{key.upper()}**: {value}")
            else:
                description = discord.Embed(
                    title='**DESCRIPTION**',
                    description=html2text(assignment['description'])
                )

        await message.channel.send(embed=description)

    return cache


async def listen_to_teacher(message, courses):
    if message.content.startswith(const.TEACHER_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[9:].upper().strip()
        teacher = cf.get_teacher(courses=courses, course_key=course_key)

        if not teacher:
            message_str = "Course Code Not Found"
        else:
            message_str = f"**{teacher}**"

        await message.channel.send(message_str)


async def listen_to_announcement(message, courses):
    if message.content.startswith(const.ANNOUNCEMENT_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[5:].upper().strip()
        announcement = cf.get_announcement(courses=courses, course_key=course_key)

        if not announcement:
            message_str = "Course Code Not Found"
        else:
            message_str = f"{announcement}"

        message_str = html2text(message_str)
        embed = discord.Embed(
            description=f"{message_str}"
        )

        await message.channel.send(embed=embed)


async def listen_to_section(message, courses):
    if message.content.startswith(const.SECTION_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[9:].upper().strip()
        section = cf.get_section(courses=courses, course_key=course_key)

        if not section:
            message_str = "**Section Not Found**"
        else:
            message_str = f"**{section}**"

        await message.channel.send(message_str)


async def listen_to_due_today(message, cache, courses):
    if message.content == const.DUE_TODAY_COMMAND_PREFIX:
        await message.channel.typing()

        if not cache:
            cache = cf.get_all_pending_assignments(courses=courses)
            print("Cached Assignments from due_today listener")

        no_due_today = await send_assignments_messages_due_today(message=message, pending_assignments=cache)

        if no_due_today:
            await message.channel.send('No Due Today')

    return cache


async def listen_to_modules(message, courses):
    if message.content.startswith(const.MODULES_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[9:].upper().strip()
        modules = cf.get_all_modules_from_course_key(courses=courses, course_key=course_key)

        if not modules:
            await message.channel.send("COURSE NOT FOUND")
            return

        for module_id, module_name in modules.items():
            message_str = f"• **{module_name}** \nID = {module_id}"
            await message.channel.send(message_str)


async def send_assignments_messages(message, pending_assignments):
    for course, assignments in pending_assignments.items():
        await message.channel.typing()
        for assignment_id, assignment_info in assignments.items():
            message_str = f"• **{assignment_info['name']}** \n({course}). \nID = {assignment_id}"
            await message.channel.send(message_str)


async def send_assignments_messages_due_today(message, pending_assignments):
    no_due_today = True

    for course, assignments in pending_assignments.items():
        await message.channel.typing()
        for assignment_id, assignment_info in assignments.items():
            if assignment_info.get('due_today'):
                no_due_today = False
                message_str = f"• **{assignment_info['name']}** \n({course}). \nID = {assignment_id}"
                await message.channel.send(message_str)

    return no_due_today

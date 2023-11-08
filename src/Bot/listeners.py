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
            return []

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
            format_data(cache)

        await send_assignments_messages(message=message, pending_assignments=cache)

    return cache


async def listen_to_assignment(message, cache):
    if message.content.startswith(const.ASSIGNMENT_COMMAND_PREFIX):
        await message.channel.typing()
        assignment_id = message.content[5:]
        assignment = cf.get_assignment(assignments=cache, assignment_id=assignment_id)

        if not assignment:
            await message.channel.send('ID NOT FOUND')
            return

        description = None

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


async def listen_to_teacher(message, courses):
    if message.content.startswith(const.TEACHER_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        teacher = cf.get_teacher(courses=courses, course_key=course_key)

        if not teacher:
            message_str = "Course Not Found"
        else:
            message_str = f"**{teacher}**"

        await message.channel.send(message_str)


async def listen_to_announcement(message, courses):
    if message.content.startswith(const.ANNOUNCEMENT_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[5:].upper()
        announcement = cf.get_announcement(courses=courses, course_key=course_key)

        if not announcement:
            message_str = "Course Not Found"
        else:
            announcement = html2text(announcement)
            message_str = f"{announcement}"

        embed = discord.Embed(
            description=f"{message_str}"
        )

        await message.channel.send(embed=embed)


async def listen_to_section(message, courses):
    if message.content.startswith(const.SECTION_COMMAND_PREFIX):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        section = cf.get_section(courses=courses, course_key=course_key)

        if not section:
            message_str = "**Section Not Found**"
        else:
            message_str = f"**{section}**"

        await message.channel.send(message_str)


async def listen_to_due_today(message, pending_assignments, courses, cache):
    if message.content == const.DUE_TODAY_COMMAND_PREFIX:
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
            message_str = f"• **{cache[assignment]['name']}**. \nID = {assignment}"
            await message.channel.send(message_str)

    return cache


async def send_assignments_messages(message, pending_assignments):
    for course, assignments in pending_assignments.items():
        await message.channel.typing()
        for assignment_id, assignment_info in assignments.items():
            message_str = f"• **{assignment_info['name']}** \n({course}). \nID = {assignment_id}"
            await message.channel.send(message_str)

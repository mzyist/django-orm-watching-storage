from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at:
        duration_time = localtime(visit.leaved_at) - visit.entered_at
    else:
        duration_time = localtime() - visit.entered_at
    return duration_time


def format_duration(duration_time):
    duration_formatted = str(duration_time).split('.')[0]
    return duration_formatted

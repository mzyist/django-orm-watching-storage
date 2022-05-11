from django.utils.timezone import localtime

from datacenter.get_duration_info import format_duration, get_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    duration_seconds = duration.seconds
    sus_seconds = minutes * 60
    return duration_seconds > sus_seconds


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    this_passcard_visits = []
    selected_passcard_visits = Visit.objects.filter(passcard__owner_name=passcard)
    for visit in selected_passcard_visits:
        suspicious_flag = is_visit_long(visit)
        entered_at = localtime(visit.entered_at)
        duration = format_duration(get_duration(visit))
        visitor = {
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': suspicious_flag
        }
        this_passcard_visits.append(visitor)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

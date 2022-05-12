from django.utils.timezone import localtime

from datacenter.get_duration_info import format_duration, get_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    serialized_active_visits = []
    for visit in active_visits:
        who_entered = Passcard.objects.get(visit__entered_at=visit.entered_at)
        entered_at = localtime(visit.entered_at)
        duration = format_duration(get_duration(visit))
        visitor = {
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration
        }
        serialized_active_visits.append(visitor)
    context = {
        'non_closed_visits': serialized_active_visits,
    }
    return render(request, 'storage_information.html', context)

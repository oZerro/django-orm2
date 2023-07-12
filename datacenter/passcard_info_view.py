from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import format_duration
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits_passcard = Visit.objects.filter(passcard=passcard.id)

    this_passcard_visits = []

    for visit in all_visits_passcard:
        duration = visit.get_duration()
        is_strange = duration > 3600
        passcard_visit = {
            'entered_at': f'{visit.entered_at.strftime("%d-%B-%Y %H:%M")}',
            'duration': f'{format_duration(duration)}',
            'is_strange': f'{is_strange}'
        }
        this_passcard_visits.append(passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = (minutes % 60) // 60
    return f'{hours}ч : {minutes}мин : {seconds}сек'


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        duration = visit.get_duration()
        format_time = format_duration(duration)

        info_non_closed_visits = {
            'who_entered': f'{visit.passcard.owner_name}',
            'entered_at': f'{visit.entered_at.strftime("%d-%B-%Y %H:%M")}',
            'duration': f'{format_time}',
        }
        non_closed_visits.append(info_non_closed_visits)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

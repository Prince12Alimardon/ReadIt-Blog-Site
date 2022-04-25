from django.shortcuts import render

from team.models import Team


def team_view(request):

    members = Team.objects.all()

    context = {
        'members': members
    }
    return render(request, 'team/index.html', context)

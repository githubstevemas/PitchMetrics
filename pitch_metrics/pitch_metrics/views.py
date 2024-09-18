from django.shortcuts import render

from graphs.generate import genre_chart_view


def index(request):

    chart1 = genre_chart_view(request)

    return render(request, 'pitch_metrics/index.html', {
        'chart1': chart1,
    })

from django.shortcuts import render


def index(request):

    return render(request, 'pitch_metrics/index.html')

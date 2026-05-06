from django.shortcuts import render
from .models import SensorData

def dashboard(request):
    latest = SensorData.objects.order_by('-timestamp').first()
    recent = SensorData.objects.order_by('-timestamp')[:50]

    context = {
        'latest': latest,
        'recent': recent,
    }
    return render(request, 'monitor/dashboard.html', context)

def api_latest(request):
    from django.http import JsonResponse
    latest = SensorData.objects.order_by('-timestamp').first()
    history = list(
        SensorData.objects.order_by('-timestamp')[:30].values(
            'id', 'temperature', 'pressure', 'status', 'timestamp'
        )
    )
    history.reverse()

    if latest:
        return JsonResponse({
            'latest': {
                'temperature': latest.temperature,
                'pressure': latest.pressure,
                'status': latest.status,
                'timestamp': latest.timestamp,
            },
            'history': history,
            'alerts_count': SensorData.objects.filter(
                temperature__gt=80
            ).count() + SensorData.objects.filter(status='ERROR').count(),
            'total_count': SensorData.objects.count(),
        })
    return JsonResponse({'latest': None, 'history': [], 'alerts_count': 0, 'total_count': 0})

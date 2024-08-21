# reservations/views.py
from django.shortcuts import render
from .models import Reservation
import json
from django.http import JsonResponse  # JsonResponse를 사용하기 위해 추가
import traceback  # 예외 처리를 위한 traceback 모듈 import
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation

def calendar_view(request):
    # 예약 데이터를 데이터베이스에서 가져옵니다.
    reservations = Reservation.objects.all()

    # 이벤트 데이터를 JSON 형식으로 변환합니다.
    events = [
        {
            'title': reservation.title,
            'start': reservation.start.isoformat(),
            'end': reservation.end.isoformat()
        }
        for reservation in reservations
    ]

    # 템플릿에 이벤트 데이터를 전달합니다.
    return render(request, 'reservations/calendar.html', {'reservations': json.dumps(events)})

@csrf_exempt
def save_event(request):
    print("save_event function called")  # 디버깅용 로그 추가
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            start = request.POST.get('start')
            end = request.POST.get('end')

            if not all([title, start, end]):
                return JsonResponse({'status': 'Invalid data'}, status=400)

            event = Reservation(title=title, start=start, end=end)
            event.save()

            return JsonResponse({'status': 'Event saved!'})
        else:
            return JsonResponse({'status': 'Invalid request'}, status=400)
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        return JsonResponse({'status': 'Internal server error'}, status=500)

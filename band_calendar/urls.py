# band_calendar/urls.py

from django.contrib import admin
from django.urls import path
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', views.calendar_view, name='calendar'),  # 기존 calendar 경로
    path('', views.calendar_view, name='home'),  # 루트 URL에 대한 경로 추가
    path('save-event/', views.save_event, name='save_event'),
]

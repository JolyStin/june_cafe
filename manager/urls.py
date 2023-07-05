from django.urls import path
from .views import booking_list
app_name = 'manager'

urlpatterns = [
    path('bookings/', booking_list, name='table_bookings'),
]

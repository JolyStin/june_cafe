from django.shortcuts import render
from main_page.models import Booking
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.groups.filter(name='manager').exists())
def booking_list(request):
    bookings = Booking.objects.filter(is_processed=False)
    return render(request, 'booking_list.html', context={'bookings': bookings})

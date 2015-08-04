from django.shortcuts import render
from django.http import HttpResponse
from apps.hello.models import UserProfile, Request
from django.core import serializers


def contacts(request):
    user_data = UserProfile.objects.all().first()
    if not user_data:
        return HttpResponse('User not found')
    return render(request, 'contacts.html', {'user': user_data})


def requests(request):
    r = Request.objects.all()
    if request.is_ajax():
        return HttpResponse(serializers.serialize('json', r),
                            content_type='application/json')
    return render(request, 'requests.html', {'last_requests': r})

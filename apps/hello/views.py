from django.shortcuts import render
from django.http import HttpResponse
from apps.hello.models import UserProfile


def contacts(request):
    user_data = UserProfile.objects.all().first()
    if not user_data:
        return HttpResponse('User not found')
    return render(request, 'contacts.html', {'user': user_data})

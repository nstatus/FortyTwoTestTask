from django.shortcuts import render
from apps.hello.models import UserProfile


def contacts(request):
    user_data = UserProfile.objects.all().first()
    return render(request, 'contacts.html', {'user': user_data})

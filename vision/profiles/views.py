from django.shortcuts import render
from profiles.models import Profile

def profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    return render(request,'profiles/profile.html', {'profile': profile})

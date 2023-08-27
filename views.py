from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementsForm
from django.urls import reverse
from app_advertisements.models import Advertisements
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db import connection


User = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisements.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements,
               'title': title,
               }
    return render(request, 'index.html', context)


def advertisement_detail(request, pk):
    advertisement = Advertisements.objects.get(id=pk)
    context = {
        'advertisement': advertisement,
    }
    return render(request, 'advertisement.html', context)


def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count('advertisements')).order_by('adv_count')
    context = {
        'users': users,
    }
    return render(request, 'top-sellers.html', context)


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(** form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementsForm()
        context = {'form': form}
        return render(request, 'advertisement-post.html', context)


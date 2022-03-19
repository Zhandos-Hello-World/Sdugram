from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from telegrambot.sendMessage import sendTelegram
import telebot


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = AdForm()
    return render(request, 'image_app.html', {'form': form})


def success(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Ads = Ad.objects.all()
        size = len(Ads)
        Ads = Ad.objects.get(pk=size)
        sendTelegram(tg_name=Ads.name, tg_phone=Ads.phone, tg_desc=Ads.description, tg_location=Ads.location, tg_img=Ads.ad_img)

    # element = Order(order_name = name, order_phone = phone)
    # element.save()
    # img = 'order_img/' + img;
    return render(request, 'thanks.html', {'ads': Ads
                                           })
   # return HttpResponse('Successfully uploaded to Moderation')

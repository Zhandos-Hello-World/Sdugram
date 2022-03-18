from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telegrambot.sendMessage import sendTelegram
from grid_panel.models import Advt
from signUp.models import Account


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    advt_list = Advt.objects.all()
    paginator = Paginator(advt_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for i in advt_list:
        print(i)
    # pc_1 = PriceCard.objects.get(pk=1)
    # pc_2 = PriceCard.objects.get(pk=2)
    # pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()

    first_name = "Login"
    last_name = ""

    for i in Account.objects.all():
        if i.status == "True":
            first_name = i.firstName
            last_name = i.lastName
            break

    dict_obj = {'slider_list': slider_list,
                # 'pc_1': pc_1,
                # 'pc_2': pc_2,
                # 'pc_3': pc_3,
                'page_obj': page_obj,
                'price_table': price_table,
                'form': form,
                'advt_list': advt_list,
                'firstName': first_name,
                'lastName': last_name}
    if first_name == "Login":
        dict_obj.pop("firstName")

    return render(request, './index.html', dict_obj)


def Adboard(request):
    advt_list = Advt.objects.all()
    dict_obj = {'advt_list': advt_list}
    return render(request, './grid.html', dict_obj)


def thanks_page(request):
    form = OrderForm(request.POST, request.FILES)
    # img = request.POST['img']
    if form.is_valid():
        form.save()
        # Get the current instance object to display in the template
    name = request.POST['name']
    phone = request.POST['phone']

    # element = Order(order_name = name, order_phone = phone)
    # element.save()
    # img = 'order_img/' + img;
    sendTelegram(tg_name=name, tg_phone=phone)

    return render(request, './thanks.html', {'name': name,
                                             'phone': phone}
                  )

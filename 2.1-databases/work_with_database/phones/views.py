from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def phones_for_context(phones_object):
    """Функция для распаковки объектов из БД для последующей передачи в context"""
    sorted_phones = []
    for phone in phones_object:
        inner_dict = {}
        inner_dict['name'] = phone.name
        inner_dict['price'] = phone.price
        inner_dict['image'] = phone.image
        inner_dict['slug'] = phone.slug
        inner_dict['release_date'] = phone.release_date
        inner_dict['lte_exists'] = phone.lte_exist
        sorted_phones.append(inner_dict)
    return sorted_phones


def show_catalog(request):
    template = 'catalog.html'
    parameter = request.GET.get('sort')
    if parameter == 'name':
        phones = Phone.objects.order_by('name')
        phones_list = phones_for_context(phones)
    elif parameter == 'min_price':
        phones = Phone.objects.order_by('price')
        phones_list = phones_for_context(phones)
    elif parameter == 'max_price':
        phones = Phone.objects.order_by('price').reverse()
        phones_list = phones_for_context(phones)
    else:
        phones = Phone.objects.all()
        phones_list = phones_for_context(phones)
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    phones_list = phones_for_context(phones)
    print(slug)
    context = {'phone': phones_list[0]}
    return render(request, template, context)

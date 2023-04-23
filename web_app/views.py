import threading
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from mini_amazon.models import Order, Stock, Product
from mini_amazon.forms import OrderForm
from backend.backend import Backend


global backend
backend = Backend()


def register(request):
    form = UserCreationForm
    context = {
        'form': form
    }

    return render(request, "registration/register.html", context)


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('/index')


def home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def cart(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, 'cart.html', {})


def about(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, 'about.html', {})


def checkout(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    form = OrderForm(initial={'user': request.user})
    context = {
        'form': form
    }
    return render(request, 'checkout.html', context)


def contact(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, 'contact.html', {})


def shop(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def men(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    products = Product.objects.filter(catalog=1)
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def women(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    products = Product.objects.filter(catalog=2)
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def children(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    products = Product.objects.filter(catalog=3)
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def thankyou(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    global backend
    data = request.POST.copy()
    pkgid = Order.objects.count()
    data['pkgid'] = str(pkgid)
    data['user'] = str(request.user.id)
    form = OrderForm(data or None)
    print(form)
    if not form.is_valid():
        print('invalid input')
        return redirect('/invalid')
    else:
        pid = int(form.data['pid'])
        whid = int(form.data['whid'])
        count = int(form.data['count'])
        if (count <= 0 or pid < 1 or pid > 4):
            print('invalid input')
            return redirect('/invalid')
        storage = Stock.objects.get(pid=pid).count
        if (count > storage):
            # not enough
            print('not enough stock')
            t1 = threading.Thread(
                target=backend.buy, args=(pid, whid, storage+count))
            t1.start()
            return redirect('/invalid')
        else:
            # enough stock
            print('start buying')
            form.save()
            entry = Stock.objects.get(pid=pid)
            entry.count -= count
            entry.save()
            t2 = threading.Thread(target=backend.pack, args=(pkgid,))
            t2.start()
            send_mail('Your order is confirmed!', 'Thank you for using Mini Amazon!', 'pcphd97@163.com',
                      [Order.objects.get(pkgid=pkgid).email], fail_silently=False)
            return render(request, 'thankyou.html', {})


def invalid(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    form = OrderForm(request.POST or None)
    context = {
        'msg': "Invalid input, please try again",
        'form': form
    }
    return render(request, 'checkout.html', context)


def orders(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    global backend
    backend.refresh()
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders
    }
    return render(request, "orders.html", context)


def search(request):
    text = request.GET['s']
    if text <= 'children':
        return redirect('/shop/children')
    elif text <= 'men':
        return redirect('/shop/men')
    else:
        return redirect('/shop/women')


def touch(request):
    email = request.GET['c_email']
    send_mail('Hello from Mini Amazon!', 'Thank you for contacting us, be in touch!', 'pcphd97@163.com',
              [email], fail_silently=False)
    return redirect('/index')

from django.shortcuts import render, redirect
from .models import top, clothes, game
import random
import logging

logger = logging.getLogger('django')

def test(request, *args, **kwargs):
    data = []
    for i in top.objects.all():
        try:
            if game.objects.filter(name = i.name):
                data.append(game.objects.filter(name = i.name)[0])
            else:
                q = clothes.objects.filter(name = i.name)[0]
                q.id *= -1
                data.append(q)
        except:
            pass #############
    return render(request, 'page/top_tovar.html', context = {'data':data})

def tovar(request, type = 'game', ids = 0, *args, **kwargs):
    if type == 'game':
        a = game.objects.filter(id = int(ids))[0]
        all = game.objects.all()
    elif type == 'clothes':
        a = clothes.objects.filter(id = int(ids))[0]
        all = clothes.objects.all()
    else: a = None
    if a:
        return render(request, 'page/tovar.html', context = {'data':a, 'all':[i for i in all if random.choice([True, False]) and i.id != a.id]})
    else:
        return redirect('/')

def like(request):
    end = []
    for i in request.COOKIES['a'].split(',')[:-1]:
        if int(i) < 0:
            a = clothes.objects.filter(id=int(i) * -1)[0]
            a.id *= -1
            end.append(a)
        else:
            end.append(game.objects.filter(id = int(i))[0])
    return  render(request, 'page/like.html', context = {'data':end})

def buy(request):
    end = []
    for i in request.COOKIES['b'].split(',')[:-1]:
        if int(i) < 0:
            a = clothes.objects.filter(id=int(i) * -1)[0]
            a.id *= -1
            end.append(a)
        else:
            end.append(game.objects.filter(id=int(i))[0])
    return render(request, 'page/buy.html', context={'data': end})
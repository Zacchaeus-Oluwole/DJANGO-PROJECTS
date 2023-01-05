from django.shortcuts import render,redirect
from .forms import PerpetratorForm
from .models import Perpetrator
from dataset.models import Dataset
from django.http import JsonResponse
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

# Create your views here.

def perpe(request):
    if request.method == "POST":
        form = PerpetratorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PerpetratorForm()
    return render(request,'index.html', {'form':form})


def show(request):
    perpetrators = Perpetrator.objects.all()
    return render(request,'show.html',{'perpetrators':perpetrators})

def edit(request, id = 1):
    perpetrator = Perpetrator.objects.get(id = id)
    return render(request, 'edit.html', {'perpetrator':perpetrator})

def search_offence(request):
    offence_i = request.GET.get('offence')

    payload = []

    if offence_i:
        dataset = Dataset.objects.all()
        data = set()
        qsN = len(offence_i)
        c = qsN
        for dat in dataset:
            i = str(dat)
            dN = len(i)
            vN = (dN-qsN) + 1
            for m in range(vN):
                result = i[m:c]
                c+=1
                if result.lower() == str(offence_i).lower():
                    data.add(i)
                if (m+1) == vN:
                    m = 0
                    c = qsN
                    break
        data_ls = list(data)
        for data_l in data_ls:
            offence_objs = Dataset.objects.filter(offence=data_l)
        
            for offence_obj in offence_objs:
                payload.append(offence_obj.offence)

    return JsonResponse({'statu' :200 , 'data' : payload})
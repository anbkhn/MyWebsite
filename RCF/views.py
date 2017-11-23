
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import  Relay,CTVT, Frq, CurrentRating, Power, Outline,InOut_1,InOut_2, InOut_3, InOut_4, InOut_5, InOut_6, InOut_7, InOut_8, Com_Port, Function, Protocol, Language
from itertools import chain

def index(request):
    relay_list_all = Relay.objects.all()

    context = {
        'relay_list_all':relay_list_all,
    }

    return render(request,'RCF/index.html',context)

def detail(request):

    ctvt_list_all = CTVT.objects.all()
    frq_list_all = Frq.objects.all()
    curent_rate_list_all = CurrentRating.objects.all()
    power_list_all = Power.objects.all()
    outline_list_all = Outline.objects.all()

    inout13_list_all = list(chain(InOut_1.objects.all(),InOut_2.objects.all()))
    inout12_list_all = list(chain(inout13_list_all,InOut_3.objects.all(),InOut_4.objects.all()))
    inout34_list_all = list(chain(inout12_list_all,InOut_5.objects.all(),InOut_6.objects.all(),InOut_7.objects.all()))
    inout11_list_all = list(chain(inout34_list_all,InOut_8.objects.all()))

    outline_select = request.POST.get('optoutline')

    comport_list_all = Com_Port.objects.all()
    func_list_all = Function.objects.all()
    protocol_list_all = Protocol.objects.all()
    lang_list_all = Language.objects.all()

    context = {

        'ctvt_list_all':ctvt_list_all,
        'frq_list_all': frq_list_all,
        'curent_rate_list_all': curent_rate_list_all,
        'inout13_list_all': inout13_list_all,
        'inout12_list_all': inout12_list_all,
        'inout34_list_all': inout34_list_all,
        'inout11_list_all': inout11_list_all,
        'power_list_all': power_list_all,
        'outline_list_all': outline_list_all,
        'comport_list_all': comport_list_all,
        'func_list_all': func_list_all,
        'protocol_list_all': protocol_list_all,
        'lang_list_all': lang_list_all,
        'outline_select': outline_select,
    }

    return render(request,'RCF/detail.html',context)
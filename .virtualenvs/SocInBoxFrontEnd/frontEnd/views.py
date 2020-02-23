

from django.shortcuts import render
import re, os, sys

import importlib.util
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django import forms
# from os.path.expanduser("~/SocInBox/scanning/portscanner.py") import portScanner
#from os.path.expanduser("~/SocInBox/scanning/portScanner.py") import portScanner
#mc = module_from_file("portScanner", "../scanning/portScanner.py")
#from sys.path.append('../../')
#from sys.path.insert(0, '../../scanning/portscanner') import portScanner
#import portScanner
#import testing.py
#import testing
from importlib import import_module
import frontEnd.testing
#import ...scanning.portScanner
#from frontEnd.portScanner import portScanner
from frontEnd.network import myNetwork
import frontEnd.portScanner

def index(request):
    return HttpResponse("Hello, world. Your at the front end")


#def temp(request):
#    template = loader.get_template('frontEnd/index.html')
#    context = {
#
#    }
#    return HttpResponse(template.render(context, request))
def temp(request):
    template = loader.get_template('frontEnd/index.html')
    context = {
        'buttonPressed': 'Empty',
        'ipNumber': 'Empty',
    }
    if request.method == 'POST':
        #nothing here
        print('this is a post')
        forms = request.POST
        print(forms)
        if 'buttonOne' in request.POST:
            print('button One pressed')
            myNetwork.callPrint("Smith")
            context['buttonPressed'] = 'button One'
            context['ipNumber'] = forms['ipInput']
            myNumberIp = forms['ipInput']
            myNetwork.callPrint(myNumberIp)
            host = myNumberIp
            portScanner.scan_ports(host, 2)
        elif 'buttonTwo' in request.POST:
            print('button Two pressed')
            context['buttonPressed'] = 'button Two'
            myNetwork.outDirCall()
        elif 'buttonThree' in request.POST:
            print('button Three pressed')
            context['buttonPressed'] = 'button Three'
        elif 'buttonFour' in request.POST:
            print('button Four pressed')
            context['buttonPressed'] = 'button Four'
        elif 'buttonFive' in request.POST:
            print('button Five pressed')
            context['buttonPressed'] = 'button Five'
        elif 'buttonSix' in request.POST:
            print('button Six pressed')
            context['buttonPressed'] = 'button Six'
        elif 'buttonSeven' in request.POST:
            print('button Seven pressed')
            context['buttonPressed'] = 'button Seven'
        elif 'buttonEight' in request.POST:
            print('button Eight pressed')
            context['buttonPressed'] = 'button Eight'
    else:
        print('get request')
        

    return HttpResponse(template.render(context, request))

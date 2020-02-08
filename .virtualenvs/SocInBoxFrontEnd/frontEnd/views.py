from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django import forms
#from ../../scanning/portScanner import TCP_connect

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
            context['buttonPressed'] = 'button One'
            context['ipNumber'] = forms['ipInput']
        elif 'buttonTwo' in request.POST:
            print('button Two pressed')
            context['buttonPressed'] = 'button Two'
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

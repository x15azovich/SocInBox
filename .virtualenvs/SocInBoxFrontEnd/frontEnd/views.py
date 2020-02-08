from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django import forms

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
    }
    if request.method == 'POST':
        #nothing here
        print('this is a post')
        forms = request.POST
        print(forms)
        if 'buttonOne' in request.POST:
            print('button One pressed')
            context['buttonPressed'] = 'button One'
        elif 'buttonTwo' in request.POST:
            print('button Two pressed')
        elif 'buttonThree' in request.POST:
            print('button Three pressed')
        elif 'buttonFour' in request.POST:
            print('button Four pressed')
        elif 'buttonFive' in request.POST:
            print('button Five pressed')
        elif 'buttonSix' in request.POST:
            print('button Six pressed')
        elif 'buttonSeven' in request.POST:
            print('button Seven pressed')
        elif 'buttonEight' in request.POST:
            print('button Eight pressed')
    else:
        print('get request')
        

    return HttpResponse(template.render(context, request))

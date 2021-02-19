from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.



def datetimeinfo(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    msg = '<h1> hello guest very </h1>'
    if h<12:
        msg = msg + "good morning"
    elif h<16:
        msg = msg + "good afternoon"
    else:
        msg = msg + "good night"
    msg = msg + "<hr> </hr>"
    msg = msg + "<h1> now server time is" +str(date) + "</h1>"


    return HttpResponse(msg)            



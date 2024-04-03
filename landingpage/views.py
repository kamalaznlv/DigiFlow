from django.shortcuts import render



def landingpage(request):
    return render(request, 'base.html', {})

# def getintouch(request):
#     return render(request, 'contact.html', {})
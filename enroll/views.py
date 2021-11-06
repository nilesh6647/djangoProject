from django.shortcuts import render
from .forms import advisorRegistration
# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = advisorRegistration(request.POST)
        print(fm)
        print(fm.cleaned_data)
    else:
        fm = advisorRegistration()
        print('its running...')

    return render(request, 'enroll/userregistration.html',
    {'form':fm})

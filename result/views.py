from django.shortcuts import render


# Create your views here.
def showresult(request):
    return render(request,'result/result.html')

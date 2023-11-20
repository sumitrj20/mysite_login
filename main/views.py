from django.shortcuts import render
from .forms import detail_emp

# Create your views here.
def home(request):
    form = detail_emp(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            form=detail_emp()
            
    else:
        form=detail_emp()
    return render(request,"contact.html",{"form":form})
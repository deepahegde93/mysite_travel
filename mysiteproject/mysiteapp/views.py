from django.shortcuts import render
from.models import Place

# Create your views here.
def site(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
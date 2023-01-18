from django.shortcuts import render
from .models import RemontAvto
from .forms import RemontAvtoForm



def index(request):
    rem = RemontAvto.objects.all()
    return render(request, "polls/index.html", {'title': 'СТО "Мустанг"', 'rem': rem})
def home_view(request):
    context = {}
    context['form'] = RemontAvtoForm()
    return render(request, "index.html", context)

def about(request):
    return render(request, "polls/about.html", {'title':'СТО "Мустанг"' })
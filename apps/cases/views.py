from django.http import HttpResponse
from django.shortcuts import (render,get_object_or_404, HttpResponseRedirect)
from apps.cases.models import Case
from apps.cases.forms import CasesForm
import datetime

# Create your views here.
def index(request):
  return HttpResponse("Cases")

def list(request):
    context = {}
    context["dataset"] = Case.objects.all()
    
    now = datetime.datetime.now()
    context["date_time"] =  now.strftime("%d/%m/%Y %H:%M:%S")
    
    return render(request, "cases/list.html", context)

def create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CasesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/cases/list/")
         
    context['form']= form
    return render(request, "cases/create.html", context)

def detail(request,id):
    context = {}
    context["data"] = Case.objects.get(id = id)
    return render(request, "cases/detail.html", context)

def update(request, id) :
    context = {}

    obj = Case.objects.get(id=id)

    # pass the object as instance in form
    form = CasesForm(request.POST or None, instance=obj)

    # add form dictionary to context
    #context["form"] = form
    context = {
        'form': form,
        'obj': obj,
    }

    return render(request, "cases/update.html", context)

def delete(request, id):
    context = {}
    obj = get_object_or_404(Case, id = str(id))
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/cases/list/")
 
    context = {
        'obj': obj,
    }
    return render(request, "cases/delete.html", context)

def updaterecord(request):
    first = request.POST['title']
    last = request.POST['theme']
    id = request.POST['id']
    member = Case.objects.get(id=id)
    member.title = first
    member.theme = last
    member.save()
    return HttpResponseRedirect("/cases/list/")
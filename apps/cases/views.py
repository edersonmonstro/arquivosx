from django.http import HttpResponse
from django.shortcuts import (render,get_object_or_404, HttpResponseRedirect)
from apps.cases.models import Case
from apps.cases.forms import CasesForm

# Create your views here.
def index(request):
  return HttpResponse("Cases")

def list(request):
    context = {}
    context["dataset"] = Case.objects.all()
    return render(request, "list.html", context)

def create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CasesForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create.html", context)

def detail(request,id):
    context = {}
    context["data"] = Case.objects.get(id = id)
    return render(request, "detail.html", context)

def update(request, id):
    context = {}
    #obj = get_object_or_404(CasosModel, id = id)
    obj = Case.objects.get(id=id)
    print(type(obj))
    # pass the object as instance in form
    form = CasesForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/cases/list/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update.html", context)

def delete(request, id):
    context = {}
    obj = get_object_or_404(Case, id = str(id))
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/cases/list/")
 
    return render(request, "delete.html", context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Vehicle

from vehicles.forms import VehicleForm
from core.section import Section
section = Section()
section.actionbar = True
section.breadcrumb = True

def index_view(request):
    
    section.page_title = "Vehicles"
    section.sidebar=False

    my_list = Vehicle.objects.all().order_by('year')
    context = {
        'section': section,
        'query_string': "",
        'my_list': my_list,
        'user': request.user,
        
    }
    
    return render(request, 'vehicles/index.html', context)

def add_view(request):
    section.page_title = "Add new vehicle"
    section.sidebar = False
    form = VehicleForm
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        
        # check whether it's valid:
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.save()
            return redirect(details_view, id=vehicle.number_plate)
        else:
            print(form.errors)
    context = {
        'section': section,
        'query_string': "",
        'form': form,
        'user': request.user,
    }
    
    return render(request, 'vehicles/add.html', context)

def details_view(request, id):
    vehicle = Vehicle.objects.get(id = id)
    section.page_title = vehicle.number_plate
    section.sidebar = True
    section.actionbar = True

    context = {
        'section': section,
        'query_string': "",
        'vehicle': vehicle,       
        'user': request.user,
        
    }
    return render(request, 'vehicles/details.html', context)
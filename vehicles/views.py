from django.shortcuts import render

from core.models import Vehicle
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

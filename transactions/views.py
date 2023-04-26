from django.shortcuts import render

from core.models import Transaction
from core.section import Section
section = Section()
section.actionbar = True
section.breadcrumb = True

def index_view(request):
    
    section.page_title = "Transactions"
    section.sidebar=False

    my_list = Transaction.objects.all().order_by('creation_date')
    context = {
        'section': section,
        'query_string': "",
        'my_list': my_list,
        'user': request.user,       
    }
    
    return render(request, 'transactions/index.html', context)

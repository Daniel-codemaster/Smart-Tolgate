from django.shortcuts import render, redirect
from .froms import AccountForm, DepositForm, OwnerForm

from core.models import Account, Owner
from core.section import Section
section = Section()
section.actionbar = True
section.breadcrumb = True

def index_view(request):
    
    section.page_title = "Accounts"
    section.sidebar=False
    section.actionbar = True

    my_list = Account.objects.all().order_by('owner')
    context = {
        'section': section,
        'query_string': "",
        'my_list': my_list,
        'user': request.user,       
    }
    
    return render(request, 'accounts/index.html', context)

def add_view(request):
    section.page_title = "Add new account"
    section.sidebar = False
   
    form = OwnerForm
    
    if request.method == 'POST':
        
        form = OwnerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            owner = form.save(commit=False)
            owner.save()

            account = Account.objects.create(balance=0, owner=owner)
           
            account.save()

            return redirect(details_view, id=account.id)
        else:
            print(form.errors)
    context = {
        'section': section,
        'query_string': "",
        'form': form,
        'user': request.user,
    }
    
    return render(request, 'accounts/add.html', context)

def details_view(request, id):
    account = Account.objects.get(id = id)
    owner = Owner.objects.get(id=account.owner.id)

    section.page_title = account.owner
    section.sidebar = True
    section.actionbar = True

    context = {
        'section': section,
        'query_string': "",
        'account': account, 
        'owner': owner,       
        'user': request.user,
        
    }
    return render(request, 'accounts/details.html', context)

def deposit_view(request, id):
    section.page_title = "Add new deposit"
    section.sidebar = False
   
    form = DepositForm
    account = Account.objects.get(id = id)
    
    if request.method == 'POST':
        
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.account = account
           
            deposit.save()

            account.balance += deposit.amount
            account.save()

            return redirect(details_view, id=account.id)
        else:
            print(form.errors)
    context = {
        'section': section,
        'query_string': "",
        'form': form,
        'account': account,
        'user': request.user,
    }
    
    return render(request, 'accounts/deposit.html', context)
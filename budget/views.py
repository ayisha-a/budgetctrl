from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,ExpenseCreateForm,DateSearchForm,CategoryCreateForm,ReviewExpenseForm
from django.contrib.auth import authenticate,login,logout
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
# Create your views here.

def signin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd = request.POST.get("password")
        # now we got unmae and password ,then we have to authenticate user

        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request,"budget/home.html")
        else:
            return render(request,"budget/login.html",{"message":"invalid password"})
    return render(request,"budget/login.html")
def signout(request):
    logout(request)
    return redirect("signin")

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"]=form
            return render(request, "budget/registration.html", context)
    return render(request,"budget/registration.html",context)

@login_required
def expense_create(request):
    form=ExpenseCreateForm(initial={"user":request.user})#loged superuser name will be set
    print("insidee")
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addexpens")
    return render(request,"budget/addexpense.html",context)

@login_required
def view_expense(request):
    form=DateSearchForm()
    context={}
    expenses=Expense.objects.filter(user=request.user)
    context["form"]=form
    context["expenses"]=expenses
    if request.method=="POST":
        form=DateSearchForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data.get("date")
            expenses=Expense.objects.filter(date=date,user=request.user)
            context["expenses"]=expenses
            return render(request, "budget/viewexpense.html", context)
    return render(request,"budget/viewexpense.html",context)

@login_required
def edit_expense(request,id):
    expense=Expense.objects.get(id=id)
    form=ExpenseCreateForm(instance=expense)
    context={}
    context['form']=form
    if request.method=="POST":
        form=ExpenseCreateForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect("viewexpense")
        else:
            form = ExpenseCreateForm(request.POST,instance=expense)
            context['form']=form
            return render(request, "budget/editexpense.html", context)
    return render(request,"budget/editexpense.html",context)

@login_required
def delete_expense(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect("viewexpense")


def create_category(request):
    form=CategoryCreateForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addexpens")
    return render(request,"budget/category.html",context)

def review_expense(request):
    form=ReviewExpenseForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ReviewExpenseForm(request.POST)
        if form.is_valid():
            from_date=form.cleaned_data.get("from_date")
            to_date = form.cleaned_data.get("to_date")
            total=Expense.objects.filter(date__gte=from_date,date__lte=to_date,user=request.user).aggregate(Sum("amount"))
            total=total["amount__sum"]
            context["total"]=total
            return render(request, "budget/reviewexpense.html", context)
    return render(request,"budget/reviewexpense.html",context)
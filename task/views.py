from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import toDo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from . forms import AddForm
# Create your views here.


def registerPage(request):
    form = CreateUserForm()


    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+user)
            return redirect('login')
    context = {'form':form}
    return render(request,"task/register.html",context)

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,"task/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('login')


# def index(request):
#     return render(request,"task/index.html")
@login_required(login_url='/login/')
def add(request):
    # obj = toDo()
    # obj.title = request.POST.get('title','Default')
    # obj.description = request.POST.get('msg','Default')
    # obj.status = False
    # obj.save()
    form = AddForm()
    if request.method == "POST":

        form = AddForm(request.POST)
        obj = toDo()
        # title = request.POST['title']
        # desc = request.POST['msg']
        if form.is_valid():
            user = request.user
            print(user)
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['msg']
            obj.status = False
            obj.user = user
            obj.save()
            return redirect('index')
        else:
            return render(request,'task/add.html',{'form':form})
    

    return render(request,'task/add.html',{'form':form})

@login_required(login_url='/login/')
def edit(request, pk):
    obj = toDo.objects.filter(user=request.user).get(pk=pk)
    print(obj.description)
    form = AddForm()
    dict_data = {
        'title':obj.title,
        'msg':obj.description,
    }
    form = AddForm(dict_data)
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['msg']
            obj.save()
            return redirect('detail',pk=pk)
        else:
            return render(request,'task/edit.html',{'form':form})
            
    return render(request, 'task/edit.html',{'form':form})
    

@login_required(login_url='/login/')
def dele(request,pk):
    obj = toDo.objects.filter(user=request.user).get(pk=pk).delete()
    return redirect('index')


class TaskList(ListView):
    model = toDo
    template_name = 'task/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        
        query = self.request.GET.get('search-area') or ''
        if query:
            #__icontains checks whether it is there in the queryset and startswith checks whether it startswith
            context['tasks'] = context['tasks'].filter(title__startswith=query)
        context['query'] = query
        return context


class TaskDetail(DetailView):
    model = toDo
    template_name = "task/taskdetail.html"
    context_object_name = 'task'

class TaskEdit(CreateView):
    pass
    
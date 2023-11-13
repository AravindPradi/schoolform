from django.contrib import auth
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Student, Branch
from .forms import StudentForm
from django.shortcuts import render,redirect

class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm  
    success_url = reverse_lazy('student_changelist')

def load_branches(request):
    college_id = request.GET.get('college')
    branches = Branch.objects.filter(college_id=college_id).order_by('name')
    return render(request, 'user/branch_dropdown_list_options.html', {'branches': branches})




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        cpassword = request.POST.get('cpassword','')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def submit(request):
    return render(request,'submit.html')
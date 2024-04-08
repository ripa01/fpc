from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Incorrect email or password!")
            return redirect('/login')

    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Succesfully log out")
    return redirect('/')



def about_view(request):
    return render(request, 'about.html')

# def news(request):
#     context = {
#         'news' : News.objects.all()
#     }
#     return render(request, 'news.html',context)


# classbased Views
class NewsListView(ListView):
    model = News
    template_name = 'news.html' 
    context_object_name = 'news'
    ordering = ['news_date']


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_details.html'


class NewsCreateView(CreateView):
    model = News
    fields = ['title','subtitle','news_image','content']
    template_name = 'news_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
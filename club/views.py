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


# classbased Views For News listview,detailsview,createview,updateview
class NewsListView(ListView):
    model = News
    template_name = 'news.html' 
    context_object_name = 'news'
    ordering = ['news_date']


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'object'  
    template_name = 'news_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent news items to the context
        context['recent_news'] = News.objects.order_by('-news_date')[:2]  
        return context


class NewsCreateView(CreateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent news items to the context
        context['recent_news'] = News.objects.order_by('-news_date')[:2]  
        return context
    
class NewsUpdateView(UpdateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent news items to the context
        context['recent_news'] = News.objects.order_by('-news_date')[:2]  
        return context  

   
 
    
    
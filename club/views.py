from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
    return redirect('/')



def about_view(request):
    return render(request, 'about.html')

# ALL NEWS VIEWS

class RecentNewsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_news'] = News.objects.order_by('-news_date')[:2]
        return context
    

class NewsListView(ListView):
    model = News
    template_name = 'news/news.html' 
    context_object_name = 'news'
    ordering = ['-news_date']


class NewsDetailView(RecentNewsMixin , DetailView):
    model = News
    context_object_name = 'news'  
    template_name = 'news/news_details.html'



class NewsCreateView(RecentNewsMixin, CreateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news/news_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class NewsUpdateView(RecentNewsMixin, UpdateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news/news_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news')


# ALL NOTICE VIEWS

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice.html' 
    context_object_name = 'notice'
    ordering = ['notice_date']


class NoticeDetailView(DetailView):
    model = Notice
    context_object_name = 'notice'  
    template_name = 'notice/notice_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent notice items to the context
        context['recent_notice'] = Notice.objects.order_by('-notice_date')[:2]  
        return context


class NoticeCreateView(CreateView):
    model = Notice
    context_object_name = 'notice'
    fields = ['title','content']
    template_name = 'notice/notice_create.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent notice items to the context
        context['recent_notice'] = Notice.objects.order_by('-notice_date')[:2]  
        return context

    

#   Club Committee 

class CommitteeListView(ListView):
    model = Committee
    template_name = 'committee/committee.html' 
    context_object_name = 'member'


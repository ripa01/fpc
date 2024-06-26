from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.core.mail import send_mail

# HOME

def home_view(request):
    recent_news = News.objects.order_by('news_date')[:2]  
    recent_event = Event.objects.order_by('-start_date')[:2]  
    return render(request, 'home.html', {'recent_news': recent_news , 'recent_event': recent_event})

# LOGIN & LOGOUT

def login_view(request):
     if not request.user.is_authenticated:      
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['psw']

            if not email.endswith("@uap-bd.edu"):
                messages.error(request, "Only valid uap-bd.edu accounts are accepted!")
                return redirect('/login')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Unknown email. Please contact administration.")
                return redirect('/login')
               
            if user.check_password(password):
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Incorrect password!")
                return redirect('/login')

     return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


# ABOUT

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
    ordering = ['news_date']


class NewsDetailView(RecentNewsMixin , DetailView):
    model = News
    context_object_name = 'news'  
    template_name = 'news/news_details.html'



class NewsCreateView(RecentNewsMixin, CreateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news/news_create.html'
    
    
class NewsUpdateView(RecentNewsMixin, UpdateView):
    model = News
    context_object_name = 'news'
    fields = ['title','subtitle','news_image','content']
    template_name = 'news/news_create.html'


class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news')



# ALL NOTICE VIEWS

class RecentNoticeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_notice'] = Notice.objects.order_by('-notice_date')[:2]
        return context

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice.html' 
    context_object_name = 'notice'
    ordering = ['-notice_date']


class NoticeDetailView(RecentNoticeMixin,DetailView):
    model = Notice
    context_object_name = 'notice'  
    template_name = 'notice/notice_details.html'


class NoticeCreateView(RecentNoticeMixin,CreateView):
    model = Notice
    context_object_name = 'notice'
    fields = ['title','content']
    template_name = 'notice/notice_create.html'

class NoticeUpdateView(RecentNoticeMixin, UpdateView):
    model = Notice
    context_object_name = 'notice'
    fields = ['title','content']
    template_name = 'notice/notice_create.html'    


class NoticeDeleteView(DeleteView):
    model = Notice
    context_object_name = 'notice'
    template_name = 'notice/notice_delete.html'
    success_url = reverse_lazy('notice')


# ALL EVENT VIEWS 
class RecentEventMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_event'] = Event.objects.order_by('start_date')[:2]
        return context
    

class EventListView(ListView):
    model = Event
    template_name = 'event/event.html' 
    context_object_name = 'event'
    ordering = ['-start_date']

class EventDetailView(RecentEventMixin , DetailView):
    model = Event
    context_object_name = 'event'  
    template_name = 'event/event_details.html'  

class EventCreateView(RecentEventMixin, CreateView):
    model = Event
    context_object_name = 'event'
    fields = ['title','subtitle','event_image','content', 'start_date' , 'end_date']
    template_name = 'event/event_create.html'


class EventUpdateView(RecentEventMixin, UpdateView):
    model = Event
    context_object_name = 'event'
    fields = ['title','subtitle','event_image','content', 'start_date' , 'end_date']
    template_name = 'event/event_create.html'

class EventDeleteView(DeleteView):
    model = Event
    context_object_name = 'event'
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('event')    
       


# Club Committee 

class CommitteeListView(RecentNewsMixin,ListView):
    model = Committee
    template_name = 'committee/committee.html' 
    context_object_name = 'member'


class CommitteeUpdateView(RecentNewsMixin, UpdateView):
    model = Committee
    context_object_name = 'member'
    fields = ['name','designation','semester','member_image']
    template_name = 'committee/edit_committee.html'



# contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,  # From email
                ['abc@gmail.com'],  # To email
                fail_silently=False,
            )
            # Optionally, you can redirect to a success page or display a message.
            # For simplicity, we'll just render the contact form again.
            form = ContactForm()  # Clear the form
            return render(request, 'contact.html', {'form': form, 'message_sent': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})







from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView) 
from .models import Stats,News,Leacher,Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse_lazy
import datetime 
# Create your views here.


class HomePageView(TemplateView):
    template_name='my_app/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['query_results'] = self.get_data()
        context['news_list'] = News.objects.filter(cur_date = datetime.date.today())
        return context

    def get_data(self):
        query_results = Stats.objects.all().last()
        return query_results


class AboutView(TemplateView):
    template_name = 'my_app/about.html'

class LeacherListView(ListView):
    model = Leacher

    def get_queryset(self):
        return Leacher.objects.filter(location=self.request.user.profile.location)

def signUp(request):
    if request.method == 'POST':
        form = forms.CustomProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('leacher_list')
    else:
        form = forms.CustomProfileForm()
    return render(request, 'registration/signup.html', {'form': form})

"""
# modified code
def donate(request):
    if request.method == 'POST':
        form = forms.UserDonateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            return redirect('leacher_list')
    else:
        form = forms.UserDonateForm()
    return render(request, 'my_app/donation_form.html',{'form':form})

"""
#extraa
@login_required
def donate(request,pk):
    prof = get_object_or_404(Profile,pk = pk)
    if request.method == 'POST':
        form = forms.UserDonateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.donator = prof
            user.save()
            return redirect('leacher_list')
    else:
        form = forms.UserDonateForm()
    return render(request,'my_app/donation_form.html',{'form':form})

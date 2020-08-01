from django.urls import path
from . import views
from .views import donate

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home_page'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('leachers/',views.LeacherListView.as_view(),name='leacher_list'),
    #change
    path('leachers/<int:pk>/donate',donate,name='donate'),
]

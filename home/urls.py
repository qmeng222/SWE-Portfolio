from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization:
admin.site.site_title = "Qingying"  # the tab
admin.site.site_header = "Login to Qingying's Portal."  # login head/tab
admin.site.index_title= "Welcome to Qingying's Portal!"  # login greeting

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('demos/', views.demos, name='demos'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]

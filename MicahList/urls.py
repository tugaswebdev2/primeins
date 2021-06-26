#from MTList import views as mtlist_views
#from MTList import urls as mtlist_urls
#from django.http import HttpResponse
#from django.contrib.auth import views as auth_views
from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from MTList import views


urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url(r'^MTList/new$', views.create_companyprofile, name='create_companyprofile'),    
    url(r'^MTList/(\d+)/$', views.view_list, name='view_list'),    
    url(r'^MTList/(\d+)/add_item$', views.new_item, name='new_item'),]
   
    #url('employed/', views.employed, name='employed'),
    #url('appointed/', views.appointed, name='appointed'),
    #url('abouts/', views.abouts, name='abouts'),
    #url('formed/', views.formed, name='formed'),
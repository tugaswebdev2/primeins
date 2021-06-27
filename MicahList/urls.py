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
    url('admin/', admin.site.urls),
    url('employed/', views.employed, name='employed'),
    url('appointed/', views.appointed, name='appointed'),
    url('abouts/', views.abouts, name='abouts'),
    url('formed/', views.formed, name='formed'),
    url(r'^new$', views.new_item, name='new_item'),   
     
    url(r'^(\d+)/view_list$', views.view_list, name='view_list'), 
    url(r'^(\d+)/add_item$', views.create_list, name='create_list'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$' , views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    ]

    #url(r'^MTList/', include(mtlist_urls)),
    #url('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_page'),    
    #url('admin/password_reset/done',auth_views.PasswordResetDoneView.as_view(),name=''),
    #url('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name=''),
    #url('reset/done/', auth_views.PasswordResetCompletedView.as_view(),name='')

from django.conf.urls import url , include
#from MTList import views as mtlist_views
#from MTList import urls as mtlist_urls

from django.contrib import admin
#from django.contrib.auth import views as auth_views
from MTList import views
#from django.urls import path
#from django.http import HttpResponse


urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^MTList/', include(mtlist_urls)),
    #url('admin/', admin.site.urls),
    #url('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_page'),    
    #url('admin/password_reset/done',auth_views.PasswordResetDoneView.as_view(),name=''),
    #url('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name=''),
    #url('reset/done/', auth_views.PasswordResetCompletedView.as_view(),name='')
    url(r'^MTList/new$', views.create_list, name='create_list'),    
    url(r'^MTList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^MTList/(\d+)/add_item$', views.new_item, name='new_item'),]
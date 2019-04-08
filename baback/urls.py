from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^horse/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^owners/$', views.owner, name='own_list'),
    url(r'^owners/(?P<pk>\d+)/$', views.own_detail, name='own_detail'),
    url(r'^owners/(?P<pk>\d+)/edit/$', views.owner_edit, name='owner_edit'),
    url(r'^owners/(?P<pk>\d+)/delete/$', views.own_delete, name='own_delete'),


    url(r'^colors/$', views.color, name='color_list'),
    url(r'^colors/(?P<pk>\d+)/$', views.color_detail, name='color_detail'),
    url(r'^colors/(?P<pk>\d+)/edit/$', views.color_edit, name='color_edit'),
    url(r'^colors/(?P<pk>\d+)/delete/$', views.color_delete, name='color_delete'),


    url(r'^gens/$', views.gen, name='gen_list'),
    url(r'^gens/(?P<pk>\d+)/$', views.gen_detail, name='gen_detail'),
    url(r'^gens/(?P<pk>\d+)/edit/$', views.gen_edit, name='gen_edit'),
    url(r'^gens/(?P<pk>\d+)/delete/$', views.gen_delete, name='gen_delete'),

    url(r'^labs/$', views.lab, name='lab_list'),
    url(r'^labs/(?P<pk>\d+)/$', views.lab_detail, name='lab_detail'),
    url(r'^labs/(?P<pk>\d+)/edit/$', views.lab_edit, name='lab_edit'),
    url(r'^labs/(?P<pk>\d+)/delete/$', views.lab_delete, name='lab_delete'),


    url(r'^owners/(?P<pk>\d+)/$', views.own_detail, name='own_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^own/new/$', views.own_new, name='own_new'),
    url(r'^genotype/new/$', views.gen_new, name='gen_new'),
    url(r'^color/new/$', views.color_new, name= 'color_new'),
    url(r'^lab/new/$', views.lab_new, name= 'lab_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    
    url(r'^user_list$', views.usr_list, name='usr_list'),

]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

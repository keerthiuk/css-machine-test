from django.urls import path
from . import views
app_name = 'common' # for redirection purpose

urlpatterns=[
    path('common_home',views.com_home, name='home'),
    path('common_about',views.com_about, name='about'),
    path('common_ourbrand',views.com_ourbrand, name='ourbrands'),
    path('common_jell',views.com_jell, name='jell'),
    path('common_con',views.com_con ,name='con'),

]
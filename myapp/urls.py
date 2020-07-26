from django.urls import path, re_path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'courses/<int:cour_id>/', views.coursedetail, name='coursedetail'),
    re_path(r'(?P<top_no>\d+)/', views.detail, name='detail'),
    path(r'courses/', views.courses, name='courses'),
    path(r'place_order/', views.place_order, name='place_order'),

]

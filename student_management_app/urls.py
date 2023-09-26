from django.urls import path
from student_management import views

urlpatterns = [
    path('Home/',views.HomeView),
    path('Home/register/',views.Register),
    path('Home/admin/',views.AdminLoginView),
    path('Home/user/',views.UserLoginView),
    path('Home/register/<int:id>/',views.update),
    path('home/details/<int:id>/',views.UserDetails),
    path('Home/admin/home/details/<int:id>/',views.UserDetails)
]

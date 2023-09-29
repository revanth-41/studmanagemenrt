from django.urls import path
from student_management_app import views

urlpatterns = [
    path('Home/',views.HomeView),
    path('Home/register/',views.Register),
    path('Home/admin/',views.AdminLoginView),
    path('Home/user/',views.UserLoginView),
    path('Home/register/<int:id>/',views.update),
    path('home/details/<int:id>/',views.UserDetails),
    path('Home/admin/home/details/<int:id>/',views.UserDetails),
    path('home/details/user/<int:id>/',views.adminUserDetails),
    path('home/details/',views.allUsersDetails),
    path('home/details/<int:id>/editprofilepic/',views.UpdateProfilePic),
    path('home/details/<int:id>/editblogcontent/',views.EditBlockContent),

]


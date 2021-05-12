from django.urls import path,include
from . import views
from .views import TaskList,TaskDetail
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(TaskList.as_view(),login_url='/login/'),name="index"),
    path('detail/<int:pk>/',login_required(TaskDetail.as_view(), login_url='/login/'),name="detail"),
    path('detail/<int:pk>/edit/',views.edit,name="edit"),
    path('detail/<int:pk>/delete/',views.dele,name="delete"),
    path('add/',views.add,name="add"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
]
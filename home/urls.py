from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home,name='home'),
    # path('save_question/',views.save_question, name='save_questions')
    # path("test/",views.ask_Question),
    # path("submitquestion/",views.submitquestion,name="questionsubmit"),
    path("register/",views.registerpage,name="register"),
    path("login/",views.login_view,name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("test/",views.test,name="test"),
    path("prevques/",views.prev_question,name="prevques"),
    path("result",views.result_view, name="result")
]

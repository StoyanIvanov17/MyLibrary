from django.urls import path

from library.lb_accounts import views

urlpatterns = [
    path('signin/', views.SignInUserView.as_view(), name='signin user'),
    path('signup/', views.SignUpUserView.as_view(), name='signup user'),
    path('signout/', views.signout_user, name='signout user'),
]
from .views import Home , PanelView
from django.urls import  path
from Home import views as accounts_views

urlpatterns = [
    path('', Home.as_view()),
    path('accounts/signup',accounts_views.signup, name='signup'),
    path('accounts/panel', PanelView.as_view())
]

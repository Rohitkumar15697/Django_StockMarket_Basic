from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/',views.logout_user, name='logout'),
    path('search/', views.search, name='search'),
    path('detail/<slug:slug>',views.detail.as_view(), name='detail'),
]

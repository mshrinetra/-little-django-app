from django.urls import path
from . import views


app_name = 'story'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='new'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit'),
    path('<int:pk>/del', views.DeleteView.as_view(), name='delete'),
]

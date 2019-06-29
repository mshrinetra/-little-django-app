from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # # Common View
    # path('', views.index, name='index'),
    # path('<int:question_id>/detail', views.details, name='details'),
    # path('<int:question_id>/results', views.result, name='results'),

    # Generic View
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailsView.as_view(), name='details'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),

    path('<int:question_id>/vote', views.vote, name='vote'),
]

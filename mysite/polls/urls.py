from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    path('<int:pk>', DetailView.as_view(), name='detail'),
    path('results/<int:pk>', ResultsView.as_view(), name='results'),
    path('vote/<int:question_id>', vote, name='vote'),
    path('', IndexView.as_view(), name='index'),

]

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.question_view, name='question_view'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.question_results, name='question_results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.question_vote, name='question_vote'),
]
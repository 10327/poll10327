from django.urls import path
from .views import PollList, PollDetail

urlpatterns = [
    #path('poll/', views.poll_list),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),
    path('option/<int:oid>/', PollVote.as_view(),)
    


]
from django.urls import path

from. import views


app_name = 'todo'

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('',views.TaskListView.as_view(),name='home'),
    path('cvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cvdetails'),
    path('cvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cvupdate'),
    path('cvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvdelete'),
]

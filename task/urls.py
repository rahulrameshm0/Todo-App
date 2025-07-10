from django.urls import path
from . import views
urlpatterns = [
    path('',views.sign_in, name='login'),
    path('signup/',views.signup, name='signup'),
    path('task',views.task, name='task'),
    path('add/',views.add_list, name='add'),
    path('delete/<int:id>/',views.deleteform, name='delete'),
    path('edit/<int:id>/',views.edit, name='edit'),
    # path('all_task/',views.all_tasks, name='all_task'),
    path('high_priority/',views.high_priority, name='high_priority'),
    path('medium_priority/',views.medium_priority, name='medium_priority'),
    path('low_priority/',views.low_priority, name='low_priority'),
    path('unmark_task/<int:id>/', views.unmark_task, name='unmark_task'),
    path('mark_complete/<int:id>/',views.mark_completed, name='mark_complete'),
]
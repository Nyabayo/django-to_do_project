from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/', views.update_task, name='update_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
]
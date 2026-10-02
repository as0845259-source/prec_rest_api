from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('newform/' , views.NewFormListCreate.as_view() , name= "newform-view-create"),
    path('delete/<int:id>/' , views.delete , name="delete"),
    path('edit/<int:id>/' , views.edit, name="edit")
]   

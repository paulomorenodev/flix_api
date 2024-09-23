from django.urls import path
from . import views # Outra maneira de importar as views que estão no mesmo diretório

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name ='actor-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
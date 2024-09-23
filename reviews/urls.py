from django.urls import path
from . import views # Outra maneira de importar as views que estão no mesmo diretório

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name ='review-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
from django.urls import path
from .views import test, tovar, like, buy

urlpatterns = [
    path('', test),
    path('<str:type>/<int:ids>/', tovar),
    path('<str:type>/-<int:ids>/', tovar),
    path('likes/', like),
    path('buy/', buy),
]

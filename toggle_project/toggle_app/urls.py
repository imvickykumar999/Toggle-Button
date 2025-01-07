from django.urls import path
from .views import toggle_button, index

urlpatterns = [
    path('', index, name='index'),
    path('toggle/<int:item_id>/', toggle_button, name='toggle_button'),
]

from django.urls import path

from . import views

app_name = "explore"

urlpatterns = [
    path('', views.explore_labels_view, name='explore'),
    path('<int:label_id>/', views.label_details_view, name='label_details'),
]

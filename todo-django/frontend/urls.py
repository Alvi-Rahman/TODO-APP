from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
    path('upload_to_firebase/', views.upload_to_firebase, name="upload_to_firebase"),
	path('get_from_firebase/', views.get_from_firebase, name="get_from_firebases"),
	path('delete_from_firebase/<str:pk>', views.delete_from_firebase,name="delete_from_firebase"),
]

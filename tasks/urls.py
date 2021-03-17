from django.urls import path, include
from .views import TaskGenericView, TaskAllGenericView


urlpatterns = [
    path('api/tasks', TaskAllGenericView.as_view(), name="list"),
    path('api/update/<int:id>/', TaskGenericView.as_view(), name="update"),
    path('api/delete/<int:id>/', TaskGenericView.as_view(), name="delete"),
    path('auth/', include("rest_framework.urls", namespace="rest_framework")),
]

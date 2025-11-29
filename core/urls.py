from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet, tasks_page
from django.urls import path

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
urlpatterns = [
    path("task-page/", tasks_page, name="tasks_page"),
]
import logging
from unicodedata import category

from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import timedelta

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def tasks_page(request):
    tasks = Task.objects.filter(user=request.user).select_related("category")
    category_param = request.GET.get("category")
    if category_param:
        tasks = tasks.filter(category_id=int(category_param))
    status_param = request.GET.get("status")
    if status_param == 'completed':
        tasks = tasks.filter(is_completed=True)
    elif status_param == 'active':
        tasks = tasks.filter(is_completed=False)
    deadline_param = request.GET.get("deadline")
    now = timezone.now()
    if deadline_param == 'overdue':
        tasks = tasks.filter(deadline__lt=now)
    elif deadline_param == 'today':
        tasks = tasks.filter(deadline__date=now.date())
    elif deadline_param == 'week':
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        tasks = tasks.filter(deadline__date__gte=start_of_week.date(), deadline__date__lte=end_of_week.date())
    sort_param = request.GET.get("sort")
    if sort_param == "deadline_asc":
        tasks = tasks.order_by("deadline")
    elif sort_param == "deadline_desc":
        tasks = tasks.order_by("-deadline")
    for task in tasks:
        task.is_overdue = (task.deadline < now and not task.is_completed)
    return render(request, "tasks_list.html", {"tasks": tasks, "now": timezone.now()})

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("django.request")

    def __call__(self, request):
        user_id = getattr(request.user, "id", None) if hasattr(request, "user") and request.user.is_authenticated else None
        path = request.path
        method = request.method
        self.logger.info(f"Request: user_id={user_id}, path={path}, method={method}")
        response = self.get_response(request)
        return response
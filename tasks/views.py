from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from django.utils.dateparse import parse_date
from django.db.models import Q

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["deadline", "created_at", "updated_at"]

    def get_queryset(self):
        qs = Task.objects.filter(user=self.request.user)
        completed = self.request.query_params.get("completed")
        deadline_before = self.request.query_params.get("deadline_before")
        deadline_after = self.request.query_params.get("deadline_after")
        search = self.request.query_params.get("search")

        if completed in ["true", "false"]:
            qs = qs.filter(completed=(completed == "true"))

        if deadline_before:
            d = parse_date(deadline_before)
            if d:
                qs = qs.filter(deadline__date__lte=d)

        if deadline_after:
            d = parse_date(deadline_after)
            if d:
                qs = qs.filter(deadline__date__gte=d)

        if search:
            qs = qs.filter(Q(title__icontains=search) | Q(description__icontains=search))

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

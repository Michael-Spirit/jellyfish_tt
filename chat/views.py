from django.shortcuts import render

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from chat.serializers import MessageSerializer
from chat.models import Message, User


class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    model = Message

    def get_queryset(self):
        return Message.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            data=serializer.validated_data,
            status=status.HTTP_201_CREATED
        )

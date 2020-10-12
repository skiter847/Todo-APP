from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = get_object_or_404(Todo, id=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    if request.method == 'PATCH':
        todo.isCompleted = not todo.isCompleted
        todo.save()
        return Response(status.HTTP_200_OK)

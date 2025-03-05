from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Todo


class TodoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({"todos": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Task created successfully!", "data": serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TodoDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response({"todo": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task updated successfully!", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()
        return Response({"message": "Task deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
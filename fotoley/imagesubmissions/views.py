# from django.shortcuts import render  #erase madbeku ansuthe
# from .models import Imagesubmissions
# from .serializers import ImagesubmissionSerializer
# from rest_framework import permissions
# from rest_framework import viewsets
# from rest_framework.parsers import MultiPartParser, FormParser
# # Create your views here.

# class ImagesubmissionsViewSet(viewsets.ModelViewSet):
#     queryset = Imagesubmissions.objects.order_by('-created_at')
#     serializer_class = ImagesubmissionSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [permissions.AllowAny]

# def perform_create(self, serializer):
#     serializer.save(creator=self.request.user)
from django.db.models import Q

from rest_framework.views import APIView
from .models import Imagesubmissions
from .serializers import ImagesubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

# from .pagination import CustomPagination


class ImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Imagesubmissions.objects.filter(uploader=request.user).order_by('-created_at')

        if not data.exists():
            return Response("You have not posted any images.")

        serializer = ImagesubmissionSerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        context = {"user": request.user}
        serializer = ImagesubmissionSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data, status=200)

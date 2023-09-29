from django.http import JsonResponse
from .models import Encroachment
from .serializers import EncroachmentSerializer
from rest_framework import viewsets,status

class encroachments(viewsets.ModelViewSet):
    queryset=Encroachment.objects.all()
    serializer_class=EncroachmentSerializer
    
    
    def list(self,request, *args, **kwargs):
        department_param=self.request.GET.get("department", default="NULL")
        status_param=self.request.GET.get("status", default="NULL")
        queryset=self.queryset
        
        if department_param != "NULL":
            field_name="encroachment_department"
            queryset=queryset.filter(**{f'{field_name}': department_param})
        
        if status_param != "NULL":
            field_name="encroachment_status"
            queryset=queryset.filter(**{f'{field_name}': status_param})
        
        serializer=self.get_serializer(queryset,many=True)
        return JsonResponse(serializer.data,safe=False)
    

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return JsonResponse(serializer.data,safe=False)
    

    def create(self, request, *args, **kwargs):
        print("I am inside Post Method")
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, safe=False)
    
    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data,safe=False)
        
    
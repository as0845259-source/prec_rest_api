from django.shortcuts import render ,  redirect  ,get_object_or_404
from rest_framework import generics , status 
from rest_framework.response import Response
from .models import NewForm
from .serializers import NewFormSerializer
from rest_framework.views import APIView


def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        data = {
            "title":title,
            "description" : description
        }
        
        NewForm.objects.create(
            title = title,
            description = description
        )  
        
    data = NewForm.objects.all()    
        
        
    return render(request, "index.html" , {'data' : data} )



class NewFormListCreate(generics.ListCreateAPIView):
    queryset = NewForm.objects.all()
    serializer_class = NewFormSerializer
    
    
def delete(request , id):
    data = get_object_or_404(NewForm , id=id)
    data.delete()
    return redirect('index')
    
def edit(request , id):
    data = get_object_or_404(NewForm , id=id)  
    if request.method == "POST":
        data.title = request.POST.get("title")
        data.description = request.POST.get("description")  
        data.save()
        return redirect('index')
    return render(request, "edit.html" , {'data' : data} )
    
       
    



    
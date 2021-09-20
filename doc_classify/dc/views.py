from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    
    if request.method  == 'POST':
      for x, uploadedFile in enumerate(request.FILES.getlist("document")):
        print(uploadedFile.name)
        print(uploadedFile.size)
        fs = FileSystemStorage()
        fs.save(uploadedFile.name, uploadedFile)
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")
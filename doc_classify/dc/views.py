from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.
def index(request):
    

    #uploading files code
    if request.method  == 'POST':
      for x, uploadedFile in enumerate(request.FILES.getlist("document")):
        print(uploadedFile.name)
        print(uploadedFile.size)
        fs = FileSystemStorage()
        fs.save(uploadedFile.name, uploadedFile)

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    today = datetime.datetime.now().date()
    context = {'allow':True,'Age':32,'Name':"","today":today,"dow":daysOfWeek}    
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")
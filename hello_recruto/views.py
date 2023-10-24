from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name", "Unknown")
    message = request.GET.get("message", "No message")
    return render(request,
                  'index.html',
                  context={'name': name, 'message': message}
                  )
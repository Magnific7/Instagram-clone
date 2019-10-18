from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Image,Profile

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'all_images/home.html', {"images":images})

def search_results(request):
    if 'user' in request.GET and request.GET['user']:
        search_term = request.GET.get('user')
        searched_user = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'all_images/search.html', {"message":message,"users":searched_user})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all_images/search.html', {"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/image.html", {"image":image})
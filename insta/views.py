from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Image,Profile
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})

def profile(request):
    profile = Image.display_user_images()
    return render(request, 'new_image.html', {"profile": profile})
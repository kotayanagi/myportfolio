from django.shortcuts import render, get_object_or_404

from .models import Photo

def photo(request):
    photos = Photo.objects
    return render(request, 'garrely.html', {'photos': photos})





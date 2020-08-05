from django.shortcuts import render
from . models import Image,location
from django.http import Http404

def home(request):
    
    images = Image.all_images()
    locations = location.all_locations()
    # print('Tooooooooom',images[0].image_url)
    return render(request,'home.html',{'images':images,'locations':locations})

def search_results(request):

    locations = location.all_locations()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{'message':message,'images':searched_images,'locations':locations})
    else:
        message = "You haven't searched for any item"
        return render(request, 'search.html',{'message':message,'locations':locations})

def images_by_location(request,id):
    locations = location.all_locations()
    selected_location = location.objects.get(id=id)
    images = Image.objects.filter(location = selected_location.id)
    return render(request,'location.html',{'locations':locations,'images':images,'location':selected_location})

def image_by_id(request,id):
    locations = location.all_locations()
    image = Image.objects.get(id=id)
    print('Toooooooooom',image.name)
    return render(request,'single_image.html',{'locations':locations,'image':image})

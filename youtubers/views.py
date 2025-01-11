from django.shortcuts import render , get_object_or_404
from .models import Youtuber
from django.core.paginator import Paginator

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    paginator = Paginator(tubers,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    city_search = Youtuber.objects.values_list('city', flat=True).distinct('city').order_by('city')
    camera_type_search = Youtuber.objects.order_by().values_list('camera_type',flat=True).distinct('camera_type').order_by('camera_type')
    category_search = Youtuber.objects.values_list('category',flat=True).distinct('category').order_by('category')

    data = {
        'tubers':page_obj,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search
    }
    return render(request,'youtubers/youtubers.html',data)

def youtubers_detail(request,id):
    tuber_detail = get_object_or_404(Youtuber , pk=id)
    data = {
        'tuber_detail':tuber_detail
    }
    return render(request,'youtubers/youtubers_detail.html',data)

def search(request):
    tubers = Youtuber.objects.all()

    city_search = Youtuber.objects.values_list('city',flat=True).distinct('city').order_by('city')
    camera_type_search = Youtuber.objects.order_by().values_list('camera_type',flat=True).distinct('camera_type').order_by('camera_type')
    category_search = Youtuber.objects.values_list('category',flat=True).distinct('category').order_by('category')
    #this gives us object means key value pair and directly gives you an array so you can loop throw in some places
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
                tubers = tubers.filter(name__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)
    data = {
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search
    }
    return render(request,'youtubers/search.html',data)
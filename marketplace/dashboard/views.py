from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

# Create your views here.
from item.models import Item

@login_required
def index(request):
    item = Item.objects.filter(created_by=request.user)
    
    return render(request, 'dashboard/index.html', {
        'items': item,
    })
    
    
    
    
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ToggleItem
from django.shortcuts import render

def toggle_button(request, item_id):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        item = get_object_or_404(ToggleItem, id=item_id)
        item.is_active = not item.is_active
        item.save()
        return JsonResponse({'success': True, 'is_active': item.is_active})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def index(request):
    items = ToggleItem.objects.all()
    return render(request, 'toggle_app/index.html', {'items': items})

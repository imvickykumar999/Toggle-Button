from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ToggleItem
from django.shortcuts import render
from firebase_admin import db
from firebase_admin import credentials
import firebase_admin, os

def toggle_button(request, item_id):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        item = get_object_or_404(ToggleItem, id=item_id)
        item.is_active = not item.is_active
        item.save()
        run(item.is_active)
        return JsonResponse({'success': True, 'is_active': item.is_active})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def index(request):
    items = ToggleItem.objects.all()
    return render(request, 'toggle_app/index.html', {'items': items})

def run(g):
    file = 'ideationology-4c639-firebase-adminsdk-5hfwu-29e74129a4.json'
    cred = credentials.Certificate(file)

    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, path)

    refv = db.reference('A/B/C/Switch')
    # g = refv.get()
    # if g == 1:
    #     g = 0
    # else:
    #     g = 1

    refv.set(g)
    return g

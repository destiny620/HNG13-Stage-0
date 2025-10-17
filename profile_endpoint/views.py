from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def me(request):
    # Fetch a random cat fact
    cat_fact = ""
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact", "")
    except Exception:
        cat_fact = "Could not fetch cat fact at this time."

    # Your profile info
    user = {
        "email": "destinyomorhienrhien1993@gmail.com",
        "name": "Destiny Omorhienrhien",
        "stack": "python/django"
    }

    data = {
        "status": "success",
        "user": user,
        "timestamp": timezone.now().isoformat(),
        "fact": cat_fact
    }
    return JsonResponse(data, content_type="application/json")
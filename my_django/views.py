"""
To render HTML webpages and other things
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # Django templates

    n = random.randint(1,20)
    article_obj = Article.objects.get(id=n)
    # We can add an API call to some rest API with python and python requests
    
    article_qs = Article.objects.all() # qs is query set

    context = {
        "object_list": article_qs,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "name": "Meher" # Replace with user's name
    }
    HTML_STRING = render_to_string("home-view.html",context=context)
    return HttpResponse(HTML_STRING)
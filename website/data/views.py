from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PagesLiked
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.

def getdata(request):

    context = {'request': request,
               'user': request.user}

    if request.user.is_authenticated:
        if request.user.social_auth.filter(provider='facebook'):
            pagesliked = PagesLiked.objects.all().filter(id2 = User.objects.get(username=request.user).id)
            context['pagesliked'] = pagesliked
            context['isfacebook'] = True
        else:
            context['isfacebook'] = False


    return render(request, 'data.html', context)


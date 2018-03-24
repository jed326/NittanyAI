from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from data.models import PagesLiked
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    context = {'request': request,
        'user': request.user}

    if request.user.is_authenticated:
        if request.user.social_auth.filter(provider='facebook'):
            print ('user is using Facebook Account!')
            id = User.objects.get(username=request.user).id
            social_user = request.user.social_auth.filter(
                provider='facebook',
            ).first()
            print("social_user: ", social_user.uid, social_user.extra_data['access_token'])


    return render(request, 'index.html', context)


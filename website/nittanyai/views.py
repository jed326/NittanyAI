from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from data.models import PagesLiked
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
import json
import urllib.request

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
            access_token = social_user.extra_data['access_token']
            has_next_page = True

            # construct the URL string
            base = "https://graph.facebook.com/v2.12"
            node = "/me/" + "?fields=likes%7Bname%2Cabout%2Cmission%2Cgeneral_info%7D"
            parameters = "&access_token=%s" % access_token
            url = base + node + parameters
            PagesLiked.objects.filter(id2 = int(id)).delete()
            while has_next_page:
                req = urllib.request.Request(url)
                response = urllib.request.urlopen(req).read().decode('utf8')
                data = json.loads(response)
                pagesliked = PagesLiked()
                pagesliked.id2 = id
                pagesliked.accesstoken = access_token

                if 'likes' in data.keys():
                    for pages in data['likes']['data']:
                        if ('about' in pages.keys()):
                            pagesliked.abouttext = pages['about']
                        if ('mission' in pages.keys()):
                            pagesliked.missiontext = pages['mission']
                        if ('name' in pages.keys()):
                            pagesliked.pagename = pages['name']
                        pagesliked.id2 = id
                        pagesliked.accesstoken = access_token
                        pagesliked.save()
                        pagesliked = PagesLiked()
                elif 'data' in data.keys():
                    for pages in data['data']:
                        if ('about' in pages.keys()):
                            pagesliked.abouttext = pages['about']
                        if ('mission' in pages.keys()):
                            pagesliked.missiontext = pages['mission']
                        if ('name' in pages.keys()):
                            pagesliked.pagename = pages['name']
                        pagesliked.id2 = id
                        pagesliked.accesstoken = access_token
                        pagesliked.save()
                        pagesliked = PagesLiked()

                if 'likes' in data.keys():
                    if 'paging' in data['likes'].keys():
                        if ('next' in data['likes']['paging'].keys()):
                            url = data['likes']['paging']['next']
                elif 'paging' in data.keys():
                    if ('next' in data['paging'].keys()):
                        url = data['paging']['next']
                else:
                    has_next_page = False



    return render(request, 'index.html', context)


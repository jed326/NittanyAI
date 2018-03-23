from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.

def index(request):
    context = {'request': request,
        'user': request.user}
    return render(request, 'index.html', context)



from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET

@require_GET
def homepage(request):
    return render_to_response('homepage.html', {}, context_instance=RequestContext(request))


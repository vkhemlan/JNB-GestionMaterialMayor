from django.shortcuts import render_to_response
from django.template import RequestContext

def _index(request):
	return render_to_response('staff/index.html', {}, 
								context_instance=RequestContext(request))
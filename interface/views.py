from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from interface.utils import log
from django.contrib import auth

@login_required
def index(request):
	return render_to_response('registration/login.html', {}, 
								context_instance=RequestContext(request))

@login_required
def logout(request):
    request.flash['success'] = 'Ha salido exitosamente del sistema'
    log("User %s logged out" % request.user.username)
    auth.logout(request)
    return redirect('login')
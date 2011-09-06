from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from interface.utils import log
from django.contrib import auth
from interface.views_staff import _index as staff_index

@login_required
def index(request):
	if request.user.is_staff:
		return staff_index(request)

@login_required
def logout(request):
    request.flash['success'] = 'Ha salido exitosamente del sistema'
    log("User %s logged out" % request.user.username)
    auth.logout(request)
    return redirect('login')
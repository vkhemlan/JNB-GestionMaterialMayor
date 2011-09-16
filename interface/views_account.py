from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from interface.models import Region

@login_required
def refresh_base_data(request):
    if request.user.is_staff:
        Region.update_all()
    return HttpResponseRedirect('/')
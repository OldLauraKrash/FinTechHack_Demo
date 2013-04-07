# Create your views here.
#Customizing the Login and Logout View.
import json

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, HttpResponse,\
    HttpResponseServerError
from django.views.decorators.csrf import csrf_view_exempt

from accounts.models import  UserProfile, UserType
from django.views.decorators.cache import never_cache
from django.core.exceptions import ValidationError
import re
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


def apply_loan(request):
    if request.method == 'POST':
        print  'manav'
        pass
    return render_to_response('accounts/2-list.html', {'test': 'test'},context_instance=RequestContext(request))


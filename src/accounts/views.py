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
    #if request.method == 'POST':
    #    pass
    return render_to_response('accounts/2-list.html',context_instance=RequestContext(request))

def apply_loan_mock_2(request):
    #if request.method == 'POST':
    #    print  'manav'
    #    pass
    return render_to_response('accounts/4-list.html',context_instance=RequestContext(request))

def apply_loan_mock_3(request):
    #if request.method == 'POST':
    #    print  'manav'
    #    pass
    return render_to_response('accounts/5-list.html', context_instance=RequestContext(request))


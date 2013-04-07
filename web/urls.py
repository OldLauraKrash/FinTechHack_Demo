# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    (r'^accounts/', include('accounts.urls')),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/index.html', 'redirect_field_name': 'login'}),
    (r'^admin/', include(admin.site.urls)),
    # The static serve should go away for production
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),

   #(r'^bid/','bidborrow.views.bid'),
   #(r'^borrow/','bidborrow.views.borrow'),
   #(r'^decision/','bidborrow.views.decision'),
   #(r'^lender_transaction/','bidborrow.views.lender_transactions'),

)

urlpatterns += staticfiles_urlpatterns()


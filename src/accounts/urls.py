from django.conf.urls.defaults import patterns,url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    # Example:
    url(r'^apply_loan/$', 'apply_loan', name='apply-loan'),

)

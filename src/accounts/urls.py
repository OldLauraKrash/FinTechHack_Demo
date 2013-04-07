from django.conf.urls.defaults import patterns,url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    # Example:
    url(r'^apply_loan/$', 'apply_loan', name='apply-loan'),
    url(r'^apply_loan_step_2/$', 'apply_loan_mock_2', name='apply-loan-mock-2'),
    url(r'^success/$', 'apply_loan_mock_3', name='apply-loan-mock-3'),


)

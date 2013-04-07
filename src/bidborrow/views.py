# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from bidborrow.models import Bid
import json
import debit
import _keys

def bid(request):
    template = loader.get_template('bid.html')
    if request.GET:
        if 'decline' in request.GET:
            context = Context({'bidded':True })
            return HttpResponse(template.render(context))

        bid_item = Bid(amount=request.GET['amount'],
                   discount=request.GET['discount'],
                   repayment=request.GET['repayment'])
        bid_item.save()
        context = Context({'bidded':True })
        return HttpResponse(template.render(context))
    context = Context({'bidded':False })
    return HttpResponse(template.render(context))

def borrow(request):
    print "INBORROW"
    template = loader.get_template('borrow.html')
    context = Context({ })
    return HttpResponse(template.render(context))

def decision(request):
    try:
        debit.transfer_funds(0.02, _keys.lender_token, _keys.merchant_account, _keys.lender_pin)
        debit.transfer_funds(0.01, _keys.merchant_token, _keys.lender_account, _keys.merchant_pin)
        debit.transfer_funds(0.01, _keys.merchant_token, _keys.lender_account, _keys.merchant_pin)
    except Exception as E:
        print E
        return HttpResponse(json.dumps({"result": "fail"}))
    return HttpResponse(json.dumps({"result": "success"}))

def lender_transactions(request):
    template = loader.get_template('lender_transactions.html')
    t = debit.get_transactions(_keys.merchant_token)
    balance = 4.89
    for trans in t:
        if 'Matt' in trans['SourceName']:
            balance -= trans['Amount']
        else:
            balance += trans['Amount']
        trans['Balance'] = balance
    context = Context({'transactions': t, 'balance': 4.89})
    return HttpResponse(template.render(context))

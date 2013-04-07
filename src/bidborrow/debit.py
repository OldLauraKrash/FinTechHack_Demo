from dwolla import DwollaUser
from datetime import date
from pymongo import MongoClient
import _keys


def transfer_funds(amount, src_token, dest_id, src_pin):
    amount = 0.02
    user = DwollaUser(src_token)
    print "About to make transfer... Balance: %.2f" % user.get_balance()
    transaction_id = user.send_funds(amount, dest_id, src_pin)
    print "Transfer complete... Balance: %.2f" % user.get_balance()
    mongo = MongoClient()
    db = mongo.credit_exchange
    transactions = db.transactions
    transactions.save(user.get_transaction(transaction_id))

def get_transactions(token):
    user = DwollaUser(token)
    return user.get_transaction_list(date.today(), limit=100)

"""
# Disbursement
print "Funding Loan..."
transfer_funds(0.02, _keys.lender_token, _keys.merchant_account, _keys.lender_pin)

# Making Payment
print "Making Payment..."
transfer_funds(0.01, _keys.merchant_token, _keys.lender_account, _keys.merchant_pin)

# Making Payment
print "Making Payment..."
transfer_funds(0.01, _keys.merchant_token, _keys.lender_account, _keys.merchant_pin)

# Get # of transactions today's transactions
print len(get_transactions(_keys.lender_token))
"""





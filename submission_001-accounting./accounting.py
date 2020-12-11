from user import authentication
from user import __init__
import transactions.journal as journal
from transactions import __init__
from banking import __init__
import banking.fvb.reconciliation
import sys


if __name__ == "__main__":
    '''
    Main function reponsible to call other modules.
    '''
    for i in sys.argv[1:]:
        print(i)
    
    authentication.authenticate_user()
    journal.receive_income(100)
    journal.pay_expense(100)
    banking.fvb.reconciliation.do_reconciliation()

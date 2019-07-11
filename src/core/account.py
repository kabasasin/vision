class Account(object):
    account_id = None
    account_name = None


class DefaultAccount(Account):
    def __init__(self):
        self.account_id = ""
        self.account_name = "Default Account"


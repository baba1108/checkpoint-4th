class Account:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float =0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.solde_du_compte = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self.solde_du_compte+= amount
            print("Dépôt de", amount, "effectué. Nouveau solde :", self.solde_du_compte)
        else:
            print('le montant de dépot doit etre positive')
    def retirer(self, amount: float):
        if amount  > 0 and  amount <= self.solde_du_compte:
            self.solde_du_compte-= amount
            print('retrait de', amount,'effectué. Nouveau Solde :',self.solde_du_compte)
        else:
            print("Retrait échoué: montant invalide ou solde insuffisant.")

    def check_balance(self):
        return self.solde_du_compte

my_account = Account('account_holder', 'account_number')
my_account.deposit(1000.0)
my_account.retirer(200.0)
print('Solde actuel:', my_account.check_balance())


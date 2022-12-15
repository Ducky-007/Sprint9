# NOTES FROM SPRINT 9.2 GUIDED PROJECT VID (BELOW)=============================
'''

import pandas as pd

df = pd.DataFrame({
    'a':[1, 2, 3], 'b': [4, 5, 6]
})



build my class of type DataFrame
df holds a DataFrame 'object'
Thing that gets made from the class and stored to a variable
is called an object
When you create new object and save it to a varibale
 you have just 'instansiated' that object or an instance of that object

 
if __name__ == '__main__':

    # Variables that form part of an 'object' are called 'attributes'
    # we access them using 'dot-notation'
    # think of ATTRIBUTES as QUALITIES of that object
    # EXAMPLE:
    # print(df.shape)
    # print(df.dtypes)
    # print(df.index)
    # print(df.columns)


# Functions that form part of an 'object' are called 'methods'
# think of METHODS as CAPABILITIES of that object
    print(df.head())
    print(df.info())
    print(df.value_counts())
    print(df.describe())
    print(df.isnull().sum())
    
    # a method associated with a Pandas 'Series' object 
    # aka 'column' so COLUMN == SERIES
    # which lives inside of a dataframe 
    print(df['a'].value_counts())

'''
class Wallet:
    '''
    Wallet docstring
    '''
    # first thing to run when we make a new class
    # outline required user-provided input values here
    # parameters with default values assigned are OPTIONAL
    def __init__(self, initial_amount=0):
        # save the user-provided inital amount as an attribute
        # (remember attribute as qualities)
        # self refers to whatever object I'm working with 
        self.balance = initial_amount

    # spend cash METHOD (remember METHODS() as CAPILBILITIES)
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'Not enough money :('
        else:
            self.balance = self.balance - amount
            return f'Remaining Balance: ${self.balance}'

    # add cash METHOD (remember method == capabilities)
    def add_cash(self, amount):
        self.balance = amount + self.balance
        return f'New Balance: ${self.balance}'


    # __repr__
    # Changes how the object looks when it's printed out
    # The presence of the self keyword allows me to access or
    # modify the class attributes within this function
    def __repr__(self):
        return f'Wallet Balance of: ${self.balance} '

if __name__ == '__main__':
    wallet1 = Wallet(50)
    print(wallet1.balance)
    
 

    

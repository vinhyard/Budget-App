import math
import matplotlib.pyplot as plt; plt.rcdefaults()


import numpy as np

import matplotlib.pyplot as plt
class Category:

    def __init__(self, name):

        self.self = self
        self.name = name
#transaction ledger to store 
        self.ledger = []




#returns the categegory along with the transaction ledger

    def __str__(self):



        
        print(f'***************{self.name}***************')

        final_align = ''

    #iterates over ledger 
        for i in range(len(self.ledger)):
          #list_of_values is the values associated with each iterable.
          #list_of_value[-1] is the description while list_of_value[0] is the amount of each transaction
            list_of_values = list(self.ledger[i].values())

        #append description and corresponding amount together and create a new line after each transaction
            final_align = final_align + str(list_of_values[-1][:24])  + "{:>10}".format(str(list_of_values[0])) + "\n"
        #return the total balance
        total_balance = str(sum([self.ledger[i]["amount"] for i in range(len(self.ledger))]))

        return final_align + "\n" + "Total: " + total_balance

    def deposit(self,amount,description='No description'):
        #add a transaction to the ledger. Includes an amount and a description of transaction
        self.ledger.append({"amount": amount,"description":description})

    def check_funds(self, amount):
 #check to see if the amount in parameter is larger than the balance

        if amount > sum([self.ledger[i]["amount"] for i in range(len(self.ledger))]):
       
            return True

        else:

            return False

    def withdraw(self, amount, description='No description'):
        total = 0
        #check the total balance 
        for i in range(len(self.ledger)):
            total += self.ledger[i]["amount"]
        #check to see if total balance is larger than amount withdrawn
        sufficient_funds_check = total - amount

        if sufficient_funds_check >= 0:

        #add withdraw to ledger if user has enough funds
            self.ledger.append({"amount": -1 * amount, "description":description})
            print("Withdraw Successful")
            return True
        else:
            print("Insufficient Funds")

            return False

    def get_balance(self):


        #returns the total balance
        return sum([self.ledger[i]["amount"] for i in range(len(self.ledger))])


    def transfer(self, amount, category):


        #transfer funds from one category to another
        transfer_process = self.withdraw(amount, 'Transfer to ' + str(category.name))


        if transfer_process == True:
            deposit_transfer = category.deposit(amount, f"Transfer from {self.name}")
            print("Transfer Complete!")
            return True

        else:
            print("Transfer Failed!")
            return False

  
    

    

  

  


def create_spend_chart(categories):

    store_spent = 0
    #percentages of each categorie's spending
    store_spent_avg = []
    for i in range(len(categories)):

        for t in range(len(categories[i].ledger)):

            if categories[i].ledger[t]["amount"] < 0:

                store_spent += (-1 * categories[i].ledger[t]["amount"])

                if t == len(categories[i].ledger) - 1:
                    print(store_spent)
                    store_spent_avg.append((store_spent/(categories[i].get_balance()+store_spent) * 100))

                    store_spent = 0


    
    objects = []


    for i in range(len(categories)):
        objects.append(categories[i].name)


        

    y_pos = np.arange(len(tuple(objects)))

    percentage_spent = list(map(lambda x: round(x, 2), store_spent_avg))

#plot a chart of the avg spent for each budget category
    plt.bar(y_pos, percentage_spent, align='center', alpha=0.5)

    plt.xticks(y_pos, objects)

    plt.ylabel('Percentage')
    plt.title('Percentage Spent By Category')

    plt.show()

    return "Done"  


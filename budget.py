
import math
import matplotlib.pyplot as plt; plt.rcdefaults()



import numpy as np
import csv
import matplotlib.pyplot as plt
import random
import string
import smtplib

from email.message import EmailMessage




class Category:

    def __init__(self, name):

        self.self = self
        self.name = name
#transaction ledger to store 
        self.ledger = []
        self.notes = []



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
        
    def make_note(self, note):


        self.notes.append(str(note))
   
        return "Noted"









#create a csv file of ledger transactions
def make_csv(category):
    #store csv file in ledger-data folder according to the category
    csv_file = open(f'ledger-data/{category.name}-ledger.csv','w')
    csv_writer = csv.writer(csv_file)


    for row in range(len(category.ledger)):


        x = list(category.ledger[row].values())
           
        y = [x[-1],"$" + str(x[0])]

        

        csv_writer.writerow(y)

    total_balance = ["Total: ", "$"+ str(category.get_balance())]
    csv_writer.writerow(total_balance)
    csv_file.close()



    return f'{category.name} CSV file successfully created'


  
    

def check_notes(category):

  
    print(f'Notes\n------------------')

    for i in range(len(category.notes)):

        print(str(i) +'. ' + str(category.notes[i]))
  
    return ""

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




#send 2fa email code
def get_email_code():



    code = ''

    code_length = random.randint(6, 10)

    for i in range(code_length):

        code += random.choice(string.ascii_letters + string.digits)

        
    return code

def send_email_code(recipient):






    email_code = get_email_code()

    msg = EmailMessage()


    msg["Subject"] = 'Email Verification Code'
    msg.add_header('Content-Type','text/html')

    msg['From'] = 'office.vinh@gmail.com'


    msg['To'] = 'vinhyard1@gmail.com'
    
    content = f'<p>Your email verification code is {email_code}</p>'
    msg.set_payload(content)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    try:

        server.login('skdlknkm@gmail.com','applesauce123')
     
    except:

        comment = 'Login Failed. Incorrect Username/Password'
        raise TypeError(comment)

    server.send_message(msg)

  

    server.quit()

    return "Message Sent"

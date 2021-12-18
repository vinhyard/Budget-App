# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
#from unittest import main










if __name__ == '__main__':


    food = budget.Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = budget.Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = budget.Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)
    clothing.withdraw(10)
    auto.withdraw(100, "testing testing")
    clothing.make_note("wabbabababba")


    a = budget.send_email_code()


    print(a)





    
    clothing.make_note("nanannaa")
    clothing.make_note("yehadklsjaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    budget.check_notes(clothing)
    budget.make_csv(auto)
    budget.make_csv(food)
    budget.make_csv(clothing)


    print(food)
    print(clothing)

    print(clothing.check_funds(1000000000000))

    print(create_spend_chart([food, clothing, auto]))
    
    # Run unit tests automatically
    #main(module='test_module', exit=False)



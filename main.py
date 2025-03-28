"""FEATURES(keep in mind, everuthing needs to be manually entered until we can integrate with a mock back account database):
  
    Add goal: set financial amount to be saved towards
  
    Add/Edit goal partition: Change the amount being set as the goal
  
    Delete Goal: Self-Explanatory
  
    Budget Check: Checking if you are within budget based on spending amount entered
  
    Account Amount Update: Update the total amount on the account
  
    View Account: Display the account with the total amount and goals/budgets(potentially both as dollar amounts and as percentages of the total)"""

user_base = []


class User:
    def __init__(self, amount, )
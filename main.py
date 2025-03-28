"""FEATURES(keep in mind, everuthing needs to be manually entered until we can integrate with a mock back account database):
  
    Add goal: set financial amount to be saved towards
  
    Add/Edit goal partition: Change the amount being set as the goal
  
    Delete Goal: Self-Explanatory
  
    Budget Check: Checking if you are within budget based on spending amount entered
  
    Account Amount Update: Update the total amount on the account
  
    View Account: Display the account with the total amount and goals/budgets(potentially both as dollar amounts and as percentages of the total)"""

# dictionary created as a place to store users. Might consider using a random number generator and associate a user's chosen name with the number
user_base = {}


class User:
    def __init__(self, account_total):
        # dictionary of goals to be updated with the user
        self.goals = {}
        
        self.total = account_total

    def add_goal(self, goal_name, goal_amount):
        self.goal_name = goal_name
        self.goal_amount = goal_amount
        
        # updating goal dictionary
        self.goals[goal_name] = goal_amount

    def edit_goal(self, goal_name, new_goal_amount):
        if self.goal_name in self.goals:
            self.goals[goal_name] = new_goal_amount
        else:
            print(f"Goal '{goal_name}' does not exist.")
    
    def delete_goal(self, goal_name):
        if self.goal_name in self.goals:
            del self.goals[goal_name]
        else:
            print(f"Goal '{self.goal_name}' does not exist")
    
    
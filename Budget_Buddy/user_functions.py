"""FEATURES(keep in mind, everuthing needs to be manually entered until we can integrate with a mock back account database):
  
    Add goal: set financial amount to be saved towards
  
    Add/Edit goal partition: Change the amount being set as the goal
  
    Delete Goal: Self-Explanatory
  
    Budget Check: Checking if you are within budget based on spending amount entered
  
    Account Amount Update: Update the total amount on the account
  
    View Account: Display the account with the total amount and goals/budgets(potentially both as dollar amounts and as percentages of the total)
    
    IMPORTANT: these are the main functions that I have tested and do work. Everything as far as the other folders and functions
    """

# dictionary created as a place to store users. Might consider using a random number generator and associate a user's chosen name with the number
# user_base = {}


class User:
    def __init__(self, account_total):
        # dictionary of goals to be updated with the user
        self.goals = {}
        
        self.account_total = float(account_total)

    def add_goal(self, goal_name, goal_amount):
        goal_name = goal_name.upper()
        self.goal_name = goal_name
        self.goal_amount = float(goal_amount)
        
        # updating goal dictionary
        self.goals[goal_name] = float(goal_amount)

    def update_goal(self, goal_name, new_goal_amount):
        goal_name = goal_name.upper()
        if self.goal_name in self.goals:
            self.goals[goal_name] = float(new_goal_amount)
        else:
            print(f"Goal '{goal_name}' does not exist.")
    
    def delete_goal(self, goal_name):
        goal_name = goal_name.upper()
        if self.goal_name in self.goals:
            del self.goals[goal_name]
        else:
            print(f"Goal '{self.goal_name}' does not exist")
    
    def view_goals(self):
        if not self.goals:
            print("No goals set.")
        else:
            print("Your Goals:")
            for goal_name, goal_amount in self.goals.items():
                print(f"{goal_name}: ${goal_amount:.2f}")

    def update_account_total(self, new_total):
        self.account_total = float(new_total)
        if self.account_total < 0:
            print(f"YOUR ACCOUNT IS IN THE NEGATIVES. T UP!")
    
    def view_full_account(self):
        print(f"Current Balance: ${self.account_total:.2f}")
        self.view_goals()

    def get_expendable_amount(self):
        budgeted = 0
        for goal_amount in self.goals.values():
            budgeted += goal_amount
        
        print(f"You have ${self.account_total - budgeted} left to budget.")

#code for testing
    #josh = User(5000)
    #josh.add_goal("tuition", 750)
    #josh.add_goal("car", 3000)
    #josh.add_goal("car insurance", 365)
    #josh.add_goal("phone", 50)
    #josh.update_goal("tuition", 500)
    #josh.delete_goal("tuition")
    #josh.view_goals()
    #josh.update_account_total(6000)
    #josh.view_full_account()
    #josh.get_expendable_amount()
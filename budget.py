class Category:
  def __init__(self, name):
    self.name = name
    self.amount = 0.0
    self.ledger = []

  def __str__(self):
    result = ""
    result += self.name.center(30, '*') + "\n"
    
    for l in self.ledger:
      result += l["description"][0:23].ljust(23, ' ')
      result += str("{:>7.2f}".format(l["amount"])) + "\n"
      
    result += "Total: " + str(self.amount)
    return result

  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.amount += amount

  def check_funds(self, amount):
    if amount > self.amount:
      return False
    else:
      return True
      
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -abs(amount), "description": description})
      self.amount -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.amount

  def transfer(self, amount, category):
    if self.withdraw(amount, "Transfer to " + category.name):
      category.deposit(amount, "Transfer from " + self.name)
      return True
        
    return False
    
    
    

def create_spend_chart(categories):
  return ""
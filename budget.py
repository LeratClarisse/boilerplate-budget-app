class Category:
  def __init__(self, name):
    self.name = name
    self.amount = 0.0
    self.ledger = []

  def __str__(self):
    result = self.name.center(30, '*') + "\n"
    
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

  def total_spent(self):
    total_spend = 0
    
    for l in self.ledger:
        if l["amount"] < 0:
            total_spend -= l["amount"]

    return total_spend
    
    

def create_spend_chart(categories):
  spend_by_category = []
  percentages = []
  names = []
  i = 0
  chart = "Percentage spent by category\n"

  for c in categories:
    spend_by_category.append(c.total_spent())
    
  total = sum(spend_by_category)

  for s in spend_by_category:
    percentages.append(s * 100 / total)
    
  chart = ["Percentage spent by category"]
  for i in range(0, 11):
    level = 10 * (10 - i)
    row = '{:>3}| '.format(level)
    for p in percentages:
        if p >= level:
            row += "o  "
        else:
            row += "   "
    chart.append(row)
    i += 1
    
  padding = " " * 4
  chart.append(padding + "-" * 3 * len(spend_by_category) + "-")

  for c in categories:
    names.append(c.name)
    
  biggest = max(map(len, names))
  for i in range(0, biggest):
    s = padding
    for name in names:
        s += " "
        s += name[i] if len(name) > i else " "
        s += " "

    chart.append(s + " ")

  return "\n".join(chart)
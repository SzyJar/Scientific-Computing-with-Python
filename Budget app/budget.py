class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  def deposit(self, amount, description = ''):
    self.ledger.append({"amount": amount,
                        "description": description})
    
  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1,
                          "description": description})
      return(True)
    else:
      return(False)

  def get_balance(self):
    balance = 0
    for i in range(len(self.ledger)):
      balance = balance + self.ledger[i]["amount"]
    return(balance)

  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1,
                          "description": f"Transfer to {destination.name}"})
      destination.ledger.append({"amount": amount,
                                 "description": f"Transfer from {self.name}"})
      return(True)
    else:
      return(False)
      
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return(True)
    else:
      return(False)
      
  def __repr__(self):
    output = ''
    for i in range(31):
      if i < 15-len(self.name) / 2 or i > 15 + len(self.name) / 2:
        output = output + '*'
      elif i == 15:
        output = output + self.name
        
    output = output + '\n'

    for row in range(len(self.ledger)):
      for i in range(30):
        if i < 23 and self.ledger[row]["description"][i:i+1] != '':
          output = output + self.ledger[row]["description"][i:i+1]
        elif i < 30 - len(str(format(self.ledger[row]["amount"], '.2f'))):
          output = output + ' '
      output = output + str(format(self.ledger[row]["amount"], '.2f')) + '\n'
    output = output + 'Total: ' + str(format(self.get_balance(), '.2f'))
    return(output)

def create_spend_chart(categories):
  moneySpent = []
  moneySpentTotal = 0
  percentSpent = []

  for instance in categories:
    moneySpent.append(0)
    for i in range(len(instance.ledger)):
      if instance.ledger[i]["amount"] < 0:
        moneySpent[-1] = moneySpent[-1] - instance.ledger[i]["amount"]
    moneySpentTotal = moneySpentTotal + moneySpent[-1]
    percentSpent.append(0)

  for i in range(len(percentSpent)):
    percentSpent[i] = moneySpent[i] / moneySpentTotal * 100

  output = 'Percentage spent by category\n'

  percent = 100
  while percent >= 0:
    if percent == 100:
      output = output + str(percent) + '|'
    elif percent > 0:
      output = output + ' ' + str(percent) + '|'
    elif percent == 0:
      output = output + '  ' + str(percent) + '|'
    for i in range(len(percentSpent)):
      if percentSpent[i] >= percent:
        output = output + ' o '
      else:
        output = output + '   '
    percent = percent - 10
    output = output + ' \n'
    
  output = output + '    -'
  lenght = 0
  
  for instance in categories:
    tmpLenght = 0
    output = output + '---'
    for i in instance.name:
      tmpLenght = tmpLenght + 1
    if tmpLenght > lenght:
      lenght = tmpLenght
      
  output = output + '\n'
  for i in range(lenght):
    output = output + '    '
    for instance in categories:   
      try:
        if instance.name[i] != '' and i > 0:
          output = output + ' ' + instance.name[i] + ' '
        else:
          output = output + ' ' + instance.name[i].upper() + ' '
      except:
        output = output + '   '
    if i < lenght - 1:
      output = output + ' \n'
    else:
      output = output + ' '
      
  return(output)
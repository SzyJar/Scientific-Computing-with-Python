import copy
import random

class Hat:

  def __init__(self, **objects):
    self.contents = []
    for i in range(len(objects)):
      for j in range(list(objects.values())[i]):
        self.contents.append(list(objects)[i])
    self.contentsBefore = copy.deepcopy(self.contents)

  def draw(self, number):
    removed = []
    for i in range(number):
      if len(self.contents) != 0:
        rand = random.randrange(len(self.contents))
        removed.append(self.contents.pop(rand))
    return(removed)

  def place_again(self):
    self.contents = copy.deepcopy(self.contentsBefore)
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  succes = 0
  expectedMatch = 0

  for h in range(len(expected_balls)):
    for i in range(list(expected_balls.values())[h]):
      expectedMatch = expectedMatch +1
      
  for exp in range(num_experiments):
    drawn = hat.draw(num_balls_drawn)
    match = 0
    for h in range(len(expected_balls)):
      for i in range(list(expected_balls.values())[h]):
        colorMatch = 0
        for j in range(len(drawn)):
          if drawn[j] == list(expected_balls)[h] and colorMatch < list(expected_balls.values())[h]:
            match = match + 1
            colorMatch = colorMatch + 1
            drawn[j] = ''
    if expectedMatch <= match:
      succes = succes + 1
    hat.place_again()
    
  return(succes / num_experiments)
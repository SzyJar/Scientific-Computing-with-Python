def arithmetic_arranger(problems, answers = 0):

  if len(problems) > 5:
    return "Error: Too many problems."
  
  number1 = ['','','','','']
  operator = ['','','','','']
  number2 = ['','','','','']
  answer = ['','','','','']
  line =['','','','']
  arranged_problems = ''

  for i in range(len(problems)):
    next = 0
    for j in problems[i]:
      if j != ' ' and next == 0:
        number1[i] = number1[i] + j
      if j != ' ' and next == 1:
        operator[i] = j
      if j != ' ' and next == 2:
        number2[i] = number2[i] + j
      if j == ' ':
        next = next+1
    
    if operator[i] != '+' and operator[i] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(number1[i]) > 4 or len(number2[i]) > 4:
      return("Error: Numbers cannot be more than four digits.")
    try:
      n = 0
      n = int(number1[i])
      n = int(number2[i])
    except:
      return("Error: Numbers must only contain digits.")
    
    if operator[i] == '+':
      answer[i] = int(number1[i]) + int (number2[i])
    elif operator[i] == '-':
      answer[i] = int(number1[i]) - int (number2[i])

  lenght = ['','','','','']   
  
  for i in range(len(problems)):
    lenght[i] = len(number1[i]) - len(number2[i])

    if lenght[i] < 0:
      for j in range(lenght[i]*-1+2):
        line[0] = line[0] + ' '
      line[0] = line[0] + number1[i]
      line[1] = line[1] + operator[i] + ' ' + number2[i]
      for j in range(len(number2[i])+2):
        line[2] = line[2] + '-'
      if answers == 1:
        for j in range(len(number2[i])+2-len(str(answer[i]))):
          line[3] = line[3] + ' '
        line[3] = line[3] + str(answer[i])
    elif lenght[i] == 0:
      line[0] = line[0] + '  ' + number1[i]
      line[1] = line[1] + operator[i] + ' ' + number2[i]
      for j in range(len(number2[i])+2):
        line[2] = line[2] + '-'
      if answers == 1:
        for j in range(len(number2[i])+2-len(str(answer[i]))):
          line[3] = line[3] + ' '
        line[3] = line[3] + str(answer[i])
    else:
      line[0] = line[0] + '  ' + number1[i]
      line[1] = line[1] + operator[i]
      for j in range(lenght[i]+1):
        line[1] = line[1] + ' '
      line[1] = line[1] + number2[i]
      for j in range(len(number1[i])+2):
        line[2] = line[2] + '-'
      if answers == 1:
        for j in range(len(number1[i])+2-len(str(answer[i]))):
          line[3] = line[3] + ' '
        line[3] = line[3] + str(answer[i])
    if i < len(problems)-1:
      line[0] = line[0] + '    '
      line[1] = line[1] + '    '
      line[2] = line[2] + '    '
      line[3] = line[3] + '    '

  arranged_problems = arranged_problems + line[0] + '\n'
  arranged_problems = arranged_problems + line[1] + '\n'
  arranged_problems = arranged_problems + line[2]
  if answers == 1:
    arranged_problems =arranged_problems + '\n' +  line[3]      
      
  return arranged_problems

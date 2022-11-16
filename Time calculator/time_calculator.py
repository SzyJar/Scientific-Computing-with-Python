def add_time(start, duration, day = 'none'):

  startHour = ''
  startMinute = ''
  startPeriod = ''
  
  next = 0
  for j in start:
    if j != ':' and next == 0:
      startHour = startHour + j
    if j != ' ' and next == 1:
      startMinute = startMinute + j
    if j != ' ' and next == 2:
      startPeriod = startPeriod + j
    if j == ' ' or j == ':':
      next = next+1
        
  if startPeriod == 'PM':
    startHour = str(int(startHour)+12)

  addHours = ''
  addMinutes = ''
  
  next = 0
  for j in duration:
    if j != ':' and next == 0:
      addHours = addHours + j
    if next == 1:
      addMinutes = addMinutes + j
    if j == ':':
      next = next+1

  hours = int(startHour) + int(addHours)
  minutes = int(startMinute) + int(addMinutes)
  days = 0
  
  while minutes >= 60:
    hours = hours + 1
    minutes = minutes - 60
  while hours >= 24:
    days = days + 1
    hours = hours - 24
  if hours >= 12:
    period = 'PM'
    hours = hours - 12
  else:
    period = 'AM' 
  if hours == 0:
    hours = 12
  
  if day != 'none':
    for i in range(len(day)):
      if i == 0:
        dayClean = day[i].upper()
      if i > 0:
        dayClean = dayClean + str(day[i].lower())
    if dayClean == 'Monday':
      startDay = 1
    elif dayClean == 'Tuesday':
      startDay = 2
    elif dayClean == 'Wednesday':
      startDay = 3
    elif dayClean == 'Thursday':
      startDay = 4
    elif dayClean == 'Friday':
      startDay = 5
    elif dayClean == 'Saturday':
      startDay = 6
    elif dayClean == 'Sunday':
      startDay = 7
    weekDay = (startDay + days) % 7
    if weekDay == 1:
      endDay = 'Monday'
    elif weekDay == 2:
      endDay = 'Tuesday'
    elif weekDay == 3:
      endDay = 'Wednesday'
    elif weekDay == 4:
      endDay = 'Thursday'
    elif weekDay == 5:
      endDay = 'Friday'
    elif weekDay == 6:
      endDay = 'Saturday'
    elif weekDay == 0:
      endDay = 'Sunday'

  if minutes < 10:
    minutes = '0' + str(minutes)
  newTime = f"{str(hours)}:{str(minutes)} {period}"
  if day != 'none':
    newTime = newTime + ', ' + endDay
  if days == 1:
    newTime = newTime + ' (next day)'
  if days > 1:
    newTime = newTime + ' (' + str(days) + ' days later)'

  return newTime
def add_time(start, duration, day = None):

  #get all numbers needed
  print(start)
  print(duration)
  starthour = int(start.split(':')[0])
  startmin = int(start.split(':')[1].split(' ')[0])
  AMorPM = start.split(':')[1].split(' ')[1]

  durationhour = int(duration.split(':')[0])
  durationmin = int(duration.split(':')[1])

  newhour = starthour + durationhour
  newmin = startmin + durationmin

  print(starthour ,startmin, AMorPM)
  print(durationhour, durationmin)
  print(newhour, newmin)

  ok = DayOfWeek("wEdneSday", 6)
  print(ok)

  return "endd"

def convert12to24():
  #convert 12hr time to 24 hr time
  return 1
def convert24to12():
  #convert 24hr to 12 hr time
  return 1

def durationmins():
  #get number of mins to count
  return 1 

def clock():
  #using 24h system add duration and return new time in 24hr 00:00 -> 23:59
  #when min is >59 then you add to the hour
  #if hour is >then 23 you make it 00
  return 1

def dayspassed():
  #number of days every 24->00 or every pm->am will be a single day
  return 1
def DayOfWeek(day, numberofdays):
  day = day.lower()
  dayslower = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  begin = dayslower.index(day)
  #newDay = dayslower[begin:numberofdays]
  #newDay = dayslower[begin:]+dayslower[-numberofdays:]
  indexofday = 5
  counter = 0
  #still trying to get day after number of days we get
  for i in range(begin, len(dayslower)):
    if counter == numberofdays:
      indexofday = i
      break
    if i == len(dayslower) - 1:
      i = -1
    counter += 1

  print("under")
  newDay = dayslower[indexofday]
  print(newDay)



  if newDay == "monday":
    return "Monday"

  elif newDay == "tuesday":
    return "Tuesday"

  elif newDay == "wednesday":
    return "Wednesday"

  elif newDay == "thursday":
    return "Thursday"

  elif newDay == "friday":
    return "Friday"

  elif newDay == "saturday":
    return "Saturday"

  elif newDay == "sunday":
    return "Sunday"
  #days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

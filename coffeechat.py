##Coffee chat scheduler is a program that schedules meetings of employees pairs
#An original solution with an O(n^2) time complexity - Anna Fulop


class Array(object):
  def __init__(self,capacity,fillValue=None): #review constructor
    self.items = list()
    for i in range(capacity): #0 to capacity - end not inclusive
      self.items.append(fillValue)
  def __len__(self):
    return(len(self.items))
  def __str__(self):
    return(str(self.items))
  def __iter__(self):
    return(iter(self.items)) #iterate over self
  def __getitem__(self, get_position):
    return(self.items[get_position])
  def __setitem__(self, overwritePosition, overwriting):
    self.items[overwritePosition] = overwriting
    

class Grid(object):
  '''Two dimensional array object'''
  def __init__(self, rows, columns, fillValue = None):
    self._data = Array(rows)
    for row in range (rows):
      self._data[row] = Array(columns, fillValue) #creates an array objects (columns) within array object (row)
  def getHeight(self):
    '''Returns the number of rows.'''
    return len(self._data)
  def getWidth(self):
    '''Returns the number of columns.'''
    return len(self._data[0])
  def __getitem__(self, index):
    '''Supports two-dimensional indexing with [row][column].'''
    return self._data[index]
  def __str__(self):
    '''Returns a string representation of the grid.'''
    result = ""
    for row in range (self.getHeight()):
      for col in range (self.getWidth()):
        result += str(self._data[row][col]) + " "
      result += "\n"
    return result


def determine_n():
  ''' User enters number of employees'''
  ERROR_MESSAGE = "Entry must be a positive, even number. Please try again."
  valid_number = False
  while valid_number == False:
    number_of_employees = input("How many employees do you want to schedule for coffee chats? ")
    try:
      number_of_employees = int(number_of_employees)
      if number_of_employees %2 == 0 and number_of_employees > 0:
        valid_number = True
      else:
        print(ERROR_MESSAGE)
    except:
      print(ERROR_MESSAGE)
  return number_of_employees


def generate_schedule():
  '''Generates schedule based on number of employees user entered'''
  number_of_employees = determine_n()
  NUMBER_OF_PAIRS = int(number_of_employees/2)
  odd_list = []
  even_list = []
  for employee in range (1,(number_of_employees+1)): #O(n) time complexity
    if employee % 2 == 1:
      odd_list.append(employee)
    else:
      even_list.append(employee)
  schedule = Grid(2,NUMBER_OF_PAIRS)
  
  #fills array
  position = 0 
  while position < (NUMBER_OF_PAIRS): # O(n)
    schedule[0][position] = odd_list[position]
    position += 1
  position =0
  while position < (NUMBER_OF_PAIRS): #O(n)
    schedule[1][position] = even_list[position]
    position += 1
  
  #The below block of code creates the schedule from the array
  NUMBER_OF_WEEKS_TO_SCHEDULE = number_of_employees - 1 #the number of unique pair sets is one less than the number of
  week_number = 1
  while week_number <= (NUMBER_OF_WEEKS_TO_SCHEDULE): #O(n)
    print(f'Week number {week_number}:')
    for n in range(NUMBER_OF_PAIRS):
      print(f'employee {schedule[0][n]} + employee {schedule[1][n]}')
    #shuffles the array critical points
    rotation_origin = schedule[0][1] # Holding for downwards rotation
    rotation_termination = schedule[1][NUMBER_OF_PAIRS - 1] #Holding for upwards rotation
    #shuffling first row
    row1_current_index = 1 # shuffling starts from index = 1 for top row to rotate about locked position
    while row1_current_index < NUMBER_OF_PAIRS-1: #O(n) time complexity; process terminates before reaching last index
      schedule[0][row1_current_index] = schedule[0][row1_current_index+1] #O(1)
      row1_current_index +=1
    schedule[0][NUMBER_OF_PAIRS-1] = rotation_termination #last index is assigned special upshifted rotation value
    #shuffling second row
    row2_current_index = NUMBER_OF_PAIRS - 1
    while row2_current_index > 0: #O(n) time complexity
      schedule[1][row2_current_index] = schedule[1][row2_current_index-1] #O(1)
      row2_current_index -= 1 #O(1)
    schedule[1][0] = rotation_origin #O(1)
    week_number += 1 #increment for outer loop

generate_schedule()

'''
sample output:
How many employees do you want to schedule for coffee chats? A
Entry must be a positive, even number. Please try again.
How many employees do you want to schedule for coffee chats? 3
Entry must be a positive, even number. Please try again.
How many employees do you want to schedule for coffee chats? -2
Entry must be a positive, even number. Please try again.
How many employees do you want to schedule for coffee chats? 24
Week number 1:
employee 1 + employee 2
employee 3 + employee 4
employee 5 + employee 6
employee 7 + employee 8
employee 9 + employee 10
employee 11 + employee 12
employee 13 + employee 14
employee 15 + employee 16
employee 17 + employee 18
employee 19 + employee 20
employee 21 + employee 22
employee 23 + employee 24
Week number 2:
employee 1 + employee 3
employee 5 + employee 2
employee 7 + employee 4
employee 9 + employee 6
employee 11 + employee 8
employee 13 + employee 10
employee 15 + employee 12
employee 17 + employee 14
employee 19 + employee 16
employee 21 + employee 18
employee 23 + employee 20
employee 24 + employee 22
Week number 3:
employee 1 + employee 5
employee 7 + employee 3
employee 9 + employee 2
employee 11 + employee 4
employee 13 + employee 6
employee 15 + employee 8
employee 17 + employee 10
employee 19 + employee 12
employee 21 + employee 14
employee 23 + employee 16
employee 24 + employee 18
employee 22 + employee 20
Week number 4:
employee 1 + employee 7
employee 9 + employee 5
employee 11 + employee 3
employee 13 + employee 2
employee 15 + employee 4
employee 17 + employee 6
employee 19 + employee 8
employee 21 + employee 10
employee 23 + employee 12
employee 24 + employee 14
employee 22 + employee 16
employee 20 + employee 18
Week number 5:
employee 1 + employee 9
employee 11 + employee 7
employee 13 + employee 5
employee 15 + employee 3
employee 17 + employee 2
employee 19 + employee 4
employee 21 + employee 6
employee 23 + employee 8
employee 24 + employee 10
employee 22 + employee 12
employee 20 + employee 14
employee 18 + employee 16
Week number 6:
employee 1 + employee 11
employee 13 + employee 9
employee 15 + employee 7
employee 17 + employee 5
employee 19 + employee 3
employee 21 + employee 2
employee 23 + employee 4
employee 24 + employee 6
employee 22 + employee 8
employee 20 + employee 10
employee 18 + employee 12
employee 16 + employee 14
Week number 7:
employee 1 + employee 13
employee 15 + employee 11
employee 17 + employee 9
employee 19 + employee 7
employee 21 + employee 5
employee 23 + employee 3
employee 24 + employee 2
employee 22 + employee 4
employee 20 + employee 6
employee 18 + employee 8
employee 16 + employee 10
employee 14 + employee 12
Week number 8:
employee 1 + employee 15
employee 17 + employee 13
employee 19 + employee 11
employee 21 + employee 9
employee 23 + employee 7
employee 24 + employee 5
employee 22 + employee 3
employee 20 + employee 2
employee 18 + employee 4
employee 16 + employee 6
employee 14 + employee 8
employee 12 + employee 10
Week number 9:
employee 1 + employee 17
employee 19 + employee 15
employee 21 + employee 13
employee 23 + employee 11
employee 24 + employee 9
employee 22 + employee 7
employee 20 + employee 5
employee 18 + employee 3
employee 16 + employee 2
employee 14 + employee 4
employee 12 + employee 6
employee 10 + employee 8
Week number 10:
employee 1 + employee 19
employee 21 + employee 17
employee 23 + employee 15
employee 24 + employee 13
employee 22 + employee 11
employee 20 + employee 9
employee 18 + employee 7
employee 16 + employee 5
employee 14 + employee 3
employee 12 + employee 2
employee 10 + employee 4
employee 8 + employee 6
Week number 11:
employee 1 + employee 21
employee 23 + employee 19
employee 24 + employee 17
employee 22 + employee 15
employee 20 + employee 13
employee 18 + employee 11
employee 16 + employee 9
employee 14 + employee 7
employee 12 + employee 5
employee 10 + employee 3
employee 8 + employee 2
employee 6 + employee 4
Week number 12:
employee 1 + employee 23
employee 24 + employee 21
employee 22 + employee 19
employee 20 + employee 17
employee 18 + employee 15
employee 16 + employee 13
employee 14 + employee 11
employee 12 + employee 9
employee 10 + employee 7
employee 8 + employee 5
employee 6 + employee 3
employee 4 + employee 2
Week number 13:
employee 1 + employee 24
employee 22 + employee 23
employee 20 + employee 21
employee 18 + employee 19
employee 16 + employee 17
employee 14 + employee 15
employee 12 + employee 13
employee 10 + employee 11
employee 8 + employee 9
employee 6 + employee 7
employee 4 + employee 5
employee 2 + employee 3
Week number 14:
employee 1 + employee 22
employee 20 + employee 24
employee 18 + employee 23
employee 16 + employee 21
employee 14 + employee 19
employee 12 + employee 17
employee 10 + employee 15
employee 8 + employee 13
employee 6 + employee 11
employee 4 + employee 9
employee 2 + employee 7
employee 3 + employee 5
Week number 15:
employee 1 + employee 20
employee 18 + employee 22
employee 16 + employee 24
employee 14 + employee 23
employee 12 + employee 21
employee 10 + employee 19
employee 8 + employee 17
employee 6 + employee 15
employee 4 + employee 13
employee 2 + employee 11
employee 3 + employee 9
employee 5 + employee 7
Week number 16:
employee 1 + employee 18
employee 16 + employee 20
employee 14 + employee 22
employee 12 + employee 24
employee 10 + employee 23
employee 8 + employee 21
employee 6 + employee 19
employee 4 + employee 17
employee 2 + employee 15
employee 3 + employee 13
employee 5 + employee 11
employee 7 + employee 9
Week number 17:
employee 1 + employee 16
employee 14 + employee 18
employee 12 + employee 20
employee 10 + employee 22
employee 8 + employee 24
employee 6 + employee 23
employee 4 + employee 21
employee 2 + employee 19
employee 3 + employee 17
employee 5 + employee 15
employee 7 + employee 13
employee 9 + employee 11
Week number 18:
employee 1 + employee 14
employee 12 + employee 16
employee 10 + employee 18
employee 8 + employee 20
employee 6 + employee 22
employee 4 + employee 24
employee 2 + employee 23
employee 3 + employee 21
employee 5 + employee 19
employee 7 + employee 17
employee 9 + employee 15
employee 11 + employee 13
Week number 19:
employee 1 + employee 12
employee 10 + employee 14
employee 8 + employee 16
employee 6 + employee 18
employee 4 + employee 20
employee 2 + employee 22
employee 3 + employee 24
employee 5 + employee 23
employee 7 + employee 21
employee 9 + employee 19
employee 11 + employee 17
employee 13 + employee 15
Week number 20:
employee 1 + employee 10
employee 8 + employee 12
employee 6 + employee 14
employee 4 + employee 16
employee 2 + employee 18
employee 3 + employee 20
employee 5 + employee 22
employee 7 + employee 24
employee 9 + employee 23
employee 11 + employee 21
employee 13 + employee 19
employee 15 + employee 17
Week number 21:
employee 1 + employee 8
employee 6 + employee 10
employee 4 + employee 12
employee 2 + employee 14
employee 3 + employee 16
employee 5 + employee 18
employee 7 + employee 20
employee 9 + employee 22
employee 11 + employee 24
employee 13 + employee 23
employee 15 + employee 21
employee 17 + employee 19
Week number 22:
employee 1 + employee 6
employee 4 + employee 8
employee 2 + employee 10
employee 3 + employee 12
employee 5 + employee 14
employee 7 + employee 16
employee 9 + employee 18
employee 11 + employee 20
employee 13 + employee 22
employee 15 + employee 24
employee 17 + employee 23
employee 19 + employee 21
Week number 23:
employee 1 + employee 4
employee 2 + employee 6
employee 3 + employee 8
employee 5 + employee 10
employee 7 + employee 12
employee 9 + employee 14
employee 11 + employee 16
employee 13 + employee 18
employee 15 + employee 20
employee 17 + employee 22
employee 19 + employee 24
employee 21 + employee 23
'''
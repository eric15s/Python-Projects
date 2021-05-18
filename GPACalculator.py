import time
def intro():
  total = 0
  temp = 0 #Temporary variable to check 
  gpa = { 'A+': 4.0,'A': 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0}
  print("Welcome to your grade calcualator") #Dictionary to represent the values for each grade letter
  classTotal = input("How many courses are you taking: ") #Input to collect the number of classes
  
  #Checking the input of the classTotal variable
  if(classTotal.isdigit() == False):
    print("I dont understand that please try again.")
    print("Resetting in: ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("")
    intro()
  #While loop to make sure we dont surpass the input of number of classes  
  while temp < float(classTotal):
    
    enter = input("Enter your first grade (capitalized Ex: A-, B+, C, ...): ")
    if(enter in gpa):
      total += gpa[enter] # Adding the value to total from the input key
      temp += 1 #adding 1 to our temporary variable to stay under the condition of the while loop
    #Checking for the correct input  
    else:
      print("I dont understand that please try again.")
      print("Resetting in: ")
      print("3")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("1")
      time.sleep(1)
      print("")
      intro()
      
  avg = total / float(classTotal) #Calculating the average GPA
  print("Your GPA is: " + str(avg))
intro()



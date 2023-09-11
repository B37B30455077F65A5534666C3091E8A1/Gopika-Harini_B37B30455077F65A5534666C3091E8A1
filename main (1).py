def CheckLeap(Year):
  #checking if the given year is leap year
  if((Year % 400 == 0)or
    (year % 100 != 0)and
    (year % 4 == 0)):
    print("Given year is a leap year");
    #else it is not a leap year
  else:
    print("Given year is not a leap year")
    #taking an input year from user
    year=int(input("Enter the number:"))
    #printing result
    CheckLeap(year)
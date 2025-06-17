
Workday_Value = int( input ("Enter in the numeric value of "
                       "the workday you wish to translate: "))

if Workday_Value == 1:
    print("Monday")
elif Workday_Value == 2:
    print("Tuesday")
elif Workday_Value == 3:
    print("Wednesday")
elif Workday_Value == 4:
    print("Thursday")
elif Workday_Value == 5:
    print("Friday")
elif Workday_Value == 0 or Workday_Value == 6 or Workday_Value ==7:
    print("Workday is a weekend!")
else:
    print("The workday is invalid")


# Jeremy Durdel
# Chapter 3 Lab 1
# 06/17/2025

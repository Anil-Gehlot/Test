
year=int(input("Enter the year : "))

if (year%100==0 and year%400==0) or (year%4==0 and year%100 !=0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")
   # ------------------------------------
    ##4 se h to 100 se ni hona chiye
    ###4,400,100 teeno se ho to leap yaer

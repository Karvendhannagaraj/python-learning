# Python program to get
# date handleing
  
  
# Import datetime class from datetime module
from datetime import datetime,timedelta
import time


## variable declartion and current date time get
now = datetime.now()

print("now = ", now)
print(now.strftime("%Y-%m-%d %H:%M:%S %p"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S %p"))
print(now.strftime("%Y/%m/%d %H:%M:%S %p"))
print(now.strftime("%H:%M:%S %p"))
print(now.strftime("%H:%M:%S"))


#add +5 day
dt = datetime.today() + timedelta(5)
print("plus Days: ",dt.strftime("%d-%m-%Y %H:%M:%S %p"))


#subtract  +5 day
dt = datetime.today() + timedelta(5)
print("plus Days: ",dt.strftime("%d-%m-%Y %H:%M:%S %p"))

#human readable datetime


# current datetime ,year,month,day split

# using now() to get current time 
current_time = datetime.now() 
    
# Printing attributes of now().

# Python 3 as it won't work with 2.7. end parameter in print()
print ("Year : ", end = "") 
print (current_time.year) 
    
print ("Month : ", end = "") 
print (current_time.month) 
    
print ("Day : ", end = "") 
print (current_time.day)


print("Name : ",end="")
a="Karvendhan"
print(a)

# Datetime format

"""%a  Locale’s abbreviated weekday name.
%A  Locale’s full weekday name.      
%b  Locale’s abbreviated month name.     
%B  Locale’s full month name.
%c  Locale’s appropriate date and time representation.   
%d  Day of the month as a decimal number [01,31].    
%f  Microsecond as a decimal number [0,999999], zero-padded on the left
%H  Hour (24-hour clock) as a decimal number [00,23].    
%I  Hour (12-hour clock) as a decimal number [01,12].    
%j  Day of the year as a decimal number [001,366].   
%m  Month as a decimal number [01,12].   
%M  Minute as a decimal number [00,59].      
%p  Locale’s equivalent of either AM or PM.
%S  Second as a decimal number [00,61].
%U  Week number of the year (Sunday as the first day of the week)
%w  Weekday as a decimal number [0(Sunday),6].   
%W  Week number of the year (Monday as the first day of the week)
%x  Locale’s appropriate date representation.    
%X  Locale’s appropriate time representation.    
%y  Year without century as a decimal number [00,99].    
%Y  Year with century as a decimal number.   
%z  UTC offset in the form +HHMM or -HHMM.
%Z  Time zone name (empty string if the object is naive).    
%%  A literal '%' character."""


# epoch method


print ("Time in seconds since the epoch: %s" %time.time())


 

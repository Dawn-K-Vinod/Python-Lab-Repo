from datetime import datetime

#current date and time
current=datetime.now()
print(current)

#Format 1 [YYYY-MM-DD HH:MM:SS]
print(current.strftime("%Y-%m-%d-%H-%M-%S"))

#Format 2 [MM/DD/YYYY]
print(current.strftime("%m/%d/%Y"))

#Format 3 [Day, Month DD, YYYY]
print(current.strftime("%A,%B %d,%Y"))

#Format 4 [Day, Month DD, YYYY HH:MM:SS AM/PM]
print(current.strftime("%A,%B %d,%Y %H:%M:%S %p"))

#Format 5 [Thu-Jul-11 10:26:23 IST 2024]
print(current.strftime("%a-%b-%d %H:%M:%S IST %Y"))

#Format 6 [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]
print(current.strftime("%a-%b-%d %H:%M:%S IST %Y"))

#Date
print(current.strftime("%d"))

#Time
print(current.strftime("%H:%M:%S"))

#Month
print(current.strftime("%B"))

#Year
print(current.strftime("%Y"))



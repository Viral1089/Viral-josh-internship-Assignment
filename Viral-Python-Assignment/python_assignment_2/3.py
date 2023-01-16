"""Develop a module over datetime library for calculating difference between 2 given time and date."""

import datetime 

date1 = "2000-10-15"
date2 = "2023-01-16"
time1 = "09:00:00"
time2 = "12:33:00"

def time_difference(date1,time1,date2,time2):
  datetime1 = datetime.datetime.strptime(date1+" "+time1,"%Y-%m-%d %H:%M:%S")
  datetime2 = datetime.datetime.strptime(date2+" "+time2,"%Y-%m-%d %H:%M:%S")
  result = datetime2 - datetime1
  return result

diff = time_difference(date1,time1,date2,time2)
print(diff)
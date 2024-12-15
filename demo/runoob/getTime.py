import time
import datetime
from calendar import calendar
from datetime import timedelta

#
# # 先获得时间数组格式的日期
# threeDatAgo = (datetime.datetime.now()-datetime.timedelta(days = 3))
#
# # 转换为时间戳
# timeStamp =int(time.mktime(threeDatAgo.timetuple()))
#
# # 转换为其他字符串格式
# otherStyleTime = threeDatAgo.strftime("%Y-%m-%d %H:%M:%S")
# print(otherStyleTime)
#

#
# timeStamp = 2557502800
# dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
# threeDayAgo = dateArray - datetime.timedelta(days = 3)
# print(threeDayAgo)

localtime = time.localtime(time.time())#time.struct_time(tm_year=2024, tm_mon=11, tm_mday=27, tm_hour=14, tm_min=32, tm_sec=5, tm_wday=2, tm_yday=332, tm_isdst=0)
print(localtime)

#获取时间戳
localtime2 = time.time()
print(localtime2)
print(type(localtime2))

localtime = time.localtime(1732689433)
print(localtime)

localtime2 = time.localtime(time.time())
print(localtime2)

print(timedelta.min)
print(timedelta.max)
#print(timedelta.total_seconds(timedelta.min))
#print(timedelta.total_seconds(timedelta.max))
year = timedelta(days = 365)
print(year)
year2 = timedelta(weeks=40,days=84,hours=23,minutes=50,seconds=600)
print(year2)
year3 = datetime.date(2024,11,27)
print(year3)

ten_years = 10 * year
print(ten_years)

nine_year = ten_years - year
print(nine_year)

three_years = nine_year / 3
print(three_years)

abs_date = abs(three_years-year)
print(abs_date)

day = calendar.month(2024,11)
print(day)
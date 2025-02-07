import datetime
print("Enter date in the past: ")
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

T = datetime.datetime.today()
P = datetime.datetime(y, m, d)
R = T - P
print(R.days, "days have passed")
import datetime
sagat = int(input("Enter the number of hourse? "))
T = datetime.datetime.today()
H = datetime.timedelta(hours = sagat)
R = T + H
print("Date after", sagat, "hourse:", R.strftime("%d.%m.%Y %X"))
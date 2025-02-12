import datetime
time = datetime.datetime.today()
duyn = datetime.timedelta(days = 1)
y = time - duyn
t = time + duyn

with open("Sene.txt", "w") as date:
    date.write(y.strftime("%d.%m.%y\t" "%A\n"))
    date.write(time.strftime("%d.%m.%y\t" "%A\n"))
    date.write(t.strftime("%d.%m.%y\t" "%A\n"))
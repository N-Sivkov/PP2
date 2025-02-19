import datetime as dt


a = dt.datetime.today()

#1
a1 = a - dt.timedelta(days=5)
print(a1.strftime("%d.%m.%Y"))
print()

#2
a21, a22 = a - dt.timedelta(days=1), a + dt.timedelta(days=1)
print(a21.strftime("%d.%m.%Y"), a.strftime("%d.%m.%Y"), a22.strftime("%d.%m.%Y"))
print()

#3
a3 = a.replace(microsecond=0)
print(a3.strftime("%d.%m.%Y %H:%M:%S:%f"))
print()

#4
a41, a42 = dt.datetime(1, 1, 1, 14, 28, 44), dt.datetime(1, 1, 1, 12, 12, 12)
a43 = a41 - a42
print(a43.total_seconds())
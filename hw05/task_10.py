import datetime

a = ['poezd1', 'poezd2', 'poezd3']
b = {'poezd1': '#1, Prague 19:00, Glubokoe 08:00',
     'poezd2': '#2, Moscow-21:00, Saint-Petersburg-10:00',
     'poezd3': '#3, Glubokoe-15:00, Polotsk-13:00'}


t1 = datetime.time(08, 00)
t2 = datetime.time(19, 00)
t3 = t2 - t1
print(t3.seconds)

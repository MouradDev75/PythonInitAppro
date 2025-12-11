# Pour manipuler les dates en Python, on utilise le package datetime
# 3 classes à importer: date, datetime, timedelta

from datetime import date, datetime, timedelta

print(">>>>>>>>>>>>>>> Date:")

today = date.today()
print("date.today():", today)

before = date(2019,12,15)
print(before)

print(f"{today.year} {today.month} {today.day}")

print(">>>>>>>>>>>>>>>>> datetime:")

now = datetime.now()
print("datetime.now():", now)

other = datetime(2011,5,29,15,44,59)
print(other)

print(">>>>>>>>>>> formattage de dates:")

# Conversion de date en str

year = now.strftime("%Y")
print(year)

month = now.strftime("%m")
print(month)

day = now.strftime("%d")
print(day)

# lien doc: https://strftime.org/

print(now.strftime("%d/%m/%Y - %H:%M:%S"))

# Conversion d'une str en date

chaine = "23/12/1989 15h00"

my_datetime = datetime.strptime(chaine, "%d/%m/%Y %Hh%M")
print(my_datetime)

print(">>>>>>>>>>>>> timedelta:")

interval = timedelta(days=5) # pas de mois ni d'années

print(now - interval)

# exemple de planification de tâche:

now = datetime.now()
interval = timedelta(seconds=3)

heure_debut = now + interval

while now < heure_debut:
    now = datetime.now()


print(">>>>>> tâche exécutée........")